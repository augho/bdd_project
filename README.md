# BDD1 Projet

Ce projet permet de traduire l'algèbre relationnel en requêtes SQL, il a été réalisé par Augustin Houba
dans le cadre du cours de BDD1.

## Fonctionnement:
J'ai fait le choix d'imposer la création d'un modèle lorsque l'on veut instancier une relation
afin de simplifier la vérification de validité des requêtes. \
Pour la traduction, je fais un appel de la méthode _get_query()_ qui va être appelée
récursivement par toutes les sous-classes de Relation (càd les classes du package SPJRUD).
Cette méthode renvoie à chaque fois sous forme de string la traduction en requête SQL.
cela donne un résultat avec des subqueries imbriquées du genre
````sql
SELECT * FROM (SELECT * FROM (SELECT * FROM (...)));
````

Cette query est ensuite exécutée sur la base de donnée sqlite avec la méthode _cursor.execute()_ .\
Pour ce qui est de la vérification des requêtes, il s'agit aussi d'une méthode qui va être appelée
récursivement par toutes les sous-classes de Relation: _is_valid()_.
Cette méthode va s'assurer que les différents critères soient respectés (liste des critères en commentaire dans
le code au dessus de chaque méthode _is_valid()_).
- Si critères respectés, renvoie _True_
- Si pas, print une erreur dans la console et renvoie _False_

## Utilisation de l'outil:

### Exécution:
Pour lancer le programme il suffit d'appeler la fonction _run()_ dans le fichier _main.py_

````python
# db_name is the name of the database file
# algebra_query is the construction with the SPJRUD algebra
# save is optional and indicates whether you want your results to be stored in a table or not
# name is optional but must be provided when save is set to True as it is the name of the table
# in which your query will be stored
def run(db_name, algebra_query, save=False, name=''):
````
### Base de données:

#### -Classe _Attribute_:
Constructeur: 
```python
def __init__(self, name, data_type):
```
Le paramètre _data_type_ doit être parmi les constantes de la classe Attribute
````python
INTEGER = 'integer'
TEXT = 'text'
NULL = 'null'
REAL = 'real'
BLOB = 'blob'
````

Exemple:
````python
name = Attribute('name', Attribute.TEXT)
````
#### -Classe _Relation_:
Constructeur:
```python
# db_name est le nom du fichier qui contient la BDD 
# schema est une liste contenant les attributs de la table SQL à laquelle
# la relation fait référence
def __init__(self, name, db_name, schema):
```

Exemple:
```python
DB = 'test.db'
pay = Attribute('pay', Attribute.INTEGER)
first = Attribute('first', Attribute.TEXT)
last = Attribute('last', Attribute.TEXT)

employees = Relation('employees', DB, [first, last, pay])
```

#### -Classe _Operation_:
Constructeur:
```python
# a est un objet de la classe attribut
# b doit respecter: typeof(b) in [Attribute, str, int, float] or b is None  
# et matcher le data_type de a (voir Attribute.same_data_type pour plus de détails)
def __init__(self, a, operation, b):
```

Le paramètre _operation_ doit être parmi les constantes de la classe Operation
````python
EQUAL = '='
GT = '>'
LT = '<'
GTE = '>='
LTE = '<='
D = '!='
````

Exemple:
```python
pay = Attribute('pay', Attribute.INTEGER)

op = Op(pay, Op.EQUAL, 50000)
```



### Algèbre relationnel:
Les classes ici présentes héritent toutes de Relation (Différence hérite de Union qui
hérite de Relation)
#### -Classe _Select_:
Constructeur: 
```python
# relation est un objet de la classe Relation
# op est un objet de la classe Operation
def __init__(self, relation, op):
```

Exemple:

````python
# σ(pay=50000)[employees]
s = Select(employees, Op(pay, Op.EQUAL, 50000))
````

Pattern de traduction:
```sql
# σ(op.a [=, <, >, ...] op.b)[relation]
SELECT DISTINCT * FROM relation WHERE op.a [=, <, >, ...] op.b
```

#### -Classe _Project_:
Constructeur: 
```python
# relation est un objet de la classe Relation
# attributes est une liste d'Attribute sur lesquels on va projeter la table
def __init__(self, relation, attributes):
```
Exemple:

````python
# π(pay, last)[employees]
p = Project(employees, [pay, last])
````

Pattern de traduction:
```sql
# π(attribute_0, ...,  attribute_n)[relation]
SELECT DISTINCT attributes[0], ..., attributes[n] FROM relation
```

#### -Classe _Join_:
Pour le join, je commence par établir une liste des attributs communs entre les 2 relations pour savoir
quelles colonnes je devrai préciser dans le *USING* et aussi pour établir le schéma de la relation
qui va découler de cette requête \
Constructeur: 
```python
# rel_a et rel_b sont des objets de la classe Relation
def __init__(self, rel_a, rel_b):
```
Exemple:

````python
# employees ⋈ departments
j = Join(employees, departments)
````

Pattern de traduction:
```sql
/# rel_a ⋈ rel_b
SELECT * FROM rel_a JOIN rel_b USING (common_attribute1, common_attribute2, ...)
```

#### -Classe _Rename_:
Pour le rename je commence par créer une table temporelle qui est une copie de la relation.
Ensuite je renomme la colonne concernée et je retourne comme query SELECT * de la nouvelle table construite.
Le nom de cette table est un uuid ou j'ai rajouté une string devant pour éviter que le nom commence par un nombre.
C'est à cause de cette manipulation que je dois passer le _cusor_ en paramètre dans toutes les méthodes
_get_query()_ car comme la table est temporelle elle se détruit en même temps que la connexion établie
avec la base de donnée \
Constructeur: 
```python
# relation est un objet de la classe Relation
# attribute_to_change est un attribut appartenant à relation
# new_name est une string
def __init__(self, relation, attribute_to_change, new_name):
```

Exemple:

````python
#  ρ(employee_nb → employee_count)[departments]
r = Rename(departments, employee_nb, 'employee_count')
````

Pattern de traduction:
```sql
#ρ(a → b)[relation]
CREATE TEMPORARY TABLE new_table AS SELECT * FROM relation;
ALTER TABLE new_table RENAME COLUMN a TO b;

# returned query
SELECT * FROM new_table
```

#### -Classe _Union_:
Constructeur: 
```python
# rel_a et rel_b sont des objets de la classe Relation
def __init__(self, rel_a, rel_b):
```
Exemple:

````python
#  employees ∪ contractors
u = Union(employees, contractors)
````

Pattern de traduction:
```sql
# rel_a ∪ rel_b
(SELECT * FROM rel_a) UNION (SELECT * FROM rel_b)
```


#### -Classe _Difference_:
Constructeur: 
```python
# rel_a et rel_b sont des objets de la classe Relation
def __init__(self, rel_a, rel_b):
```

Exemple:

````python
# employees - contractors
d = Difference(employees, contractors)
````

Pattern de traduction:
```sql
# rel_a - rel_b
(SELECT * FROM rel_a) EXCEPT (SELECT * FROM rel_b)
```

## Points à améliorer

##### Mon utilisation de git:
Comme j'ai réalisé le projet seul je n'ai pas vraiment fait de commits régulier, bonne utilisation de branche,
push régulier, etc

##### Messages d'erreurs:

Mes messages d'erreurs ne sont pas de la plus grande précision. Cependant ils m'ont tout de même été utiles lors
de mes tests de l'outil.
