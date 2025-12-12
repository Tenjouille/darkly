# Steps

### 1. Check if there is a breach to exploit 
`0 OR 1=1`

The result displays every lines, so there is a weakness.

### 2. Add a valid Select

Every line displayed has 2 columns : First name & Surname. If we want to add an UNION SELECT, it needs to have the exact same amount of column.

We try `0 UNION SELECT 1, 2` and it returned the values 1 and 2. Every other number of argument Selected would return `The used SELECT statements have a different number of columns` error.

### 3. List Every Databases and their Tables

`0 UNION SELECT table_schema, table_name FROM information_schema.tables`

Got us every databases connected to this server and their linked tables. We easily find the one we are looking for : Member_Sql_Injection with its unique table : users

### 4. List Every Tables and their Columns

`0 UNION SELECT table_name, column_name FROM information_schema.columns`

Basically the same process

### 5. Find out the member's username and password

Now that we have the database/table/columns's names, we can associate them in our requests to get the flag :

To identify the flag :
`0 UNION SELECT user_id, first_name FROM Member_Sql_Injection.users`

And to get its confidentials values : `0 UNION SELECT Commentaire, countersign FROM Member_Sql_Injection.users WHERE user_id = 5`