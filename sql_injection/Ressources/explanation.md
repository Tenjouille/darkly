# THE SQL INJECTION
*When your daily adrenaline injection is not enough for you to feel alive ⚡️*

## What is it ??

With the SQL Injection, you can exploit a non protected SQL query to access unallowed columns, tables or even entire databases.

## How does it work ?

In a lot of case, in the back-end side, this breach is due to a non protected variable which will be concatenated to a SQL Query.

*Exemple : `SELECT username FROM users WHERE username = '$var';`.*

From this point, you can use the UNION keyword to add more SELECT to the query and potentially access to the common information_schema database, containing meta data about all other db's, and then access unwanted data.

## The BlackBox Test

To spot a SQL INJECTION breach, you can enter in text inputs something like `' OR 1=1` ou `0 OR 1=1`

## How do you counter it ?

Like the most part of known web breaches, the best way to avoid an SQL injection is to control the variables you give to a SQL Query. If you need to filter throught an int-type value, refuse any undigit values, if you look for a string, use a whitelist of the words you can use, or a blacklist of the words you can not use. 