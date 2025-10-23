---
id: 2264e573-2557-4b4b-868d-0ff34c9c53f1
name: PostgreSQL XML Data Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.772926+00:00'
updated_at: '2023-04-10T20:23:15.528759+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[PostgreSQL injection]]'
- '[[PostgreSQL XML helpers]]'
commands:
- '[[Convert query result to XML]]'
- '[[Convert Query to XML]]'
- '[[Dump current database to XML]]'
- '[[Dump current database to XML schema]]'
- '[[Limit Results]]'
---

# PostgreSQL XML Data Exfiltration

## Summary

PostgreSQL injection is a technique used by attackers to exploit vulnerabilities in a PostgreSQL database to gain unauthorized access to sensitive data. This procedure specifically focuses on using PostgreSQL's XML helpers to exfiltrate data from the database. By exporting user data as XML and usin

## Description

# Description

PostgreSQL injection is a technique used by attackers to exploit vulnerabilities in a PostgreSQL database to gain unauthorized access to sensitive data. This procedure specifically focuses on using PostgreSQL's XML helpers to exfiltrate data from the database. By exporting user data as XML and using the XML Query Exporter command, an attacker can extract sensitive information from the database. The Limit Exfiltration Technique command can be used to ensure that the amount of data exfiltrated remains within a certain limit. Dumping the entire database to XML can also be used as a technique for exfiltrating large amounts of data. This technique can be used to steal sensitive information such as user credentials, financial information, and intellectual property.

 

## Requirements

1. Access to a vulnerable PostgreSQL database

1. Knowledge of PostgreSQL XML helpers

1. Authentication credentials for the database

 

## Defense

1. Implement least privilege access controls to restrict access to sensitive data

1. Regularly monitor and audit database activity to detect and respond to suspicious behavior

1. Use parameterized queries to prevent SQL injection attacks

 

## Objectives

1. Extract sensitive information from a PostgreSQL database

1. Steal user credentials and financial information

1. Exfiltrate intellectual property

 

# Instructions

1. This command exports PostgreSQL user data as an XML file. The 'query_to_xml' function is used to execute the query 'select * from pg_user' and return the results as an XML row. The 'true' arguments indicate that the XML should include the column names and that the row should be indented for readability. The empty string argument is used to specify the XML root element name.

 



**Code**: [[select query_to_xml('select * from pg_user',true,t]]



> The 'select' statement with the 'query_to_xml' function is used to generate an XML file from the results of the 'select * from pg_user' query. The 'true' arguments indicate that the XML should include the column names and that the row should be indented for readability. The empty string argument is used to specify the XML root element name. This command can be useful for exporting PostgreSQL user data in a format that can be easily consumed by other systems.



**Command** ([[Convert query result to XML]]):

```bash
select * from pg_user
```



2. This command exports data from a database query to an XML file.

 



**Code**: [[query_to_xml]]



> The 'query_to_xml' command takes a SQL query as input and exports the results to an XML file. The command accepts the following arguments:

- '-q': the SQL query to be executed
- '-f': the name of the output file (including the path)

For example, the following command exports the results of the 'SELECT * FROM customers' query to an XML file named 'customers.xml':

query_to_xml -q 'SELECT * FROM customers' -f '/path/to/customers.xml'

Note that the XML file will have a root element named 'resultset', and each row of the resultset will be represented by a 'row' element with child elements corresponding to the columns of the row.



**Command** ([[Convert Query to XML]]):

```bash
SELECT * FROM users WHERE age > 30 FOR XML AUTO
```



3. The LIMIT command is used to restrict the number of results returned from a query. The command takes two arguments: the first argument specifies the starting point (offset) and the second argument specifies the maximum number of results to return (limit).

 



**Code**: [[LIMIT]]



> The LIMIT command is commonly used in combination with SELECT statements to retrieve a specific number of results from a database. By specifying a limit, the command can help prevent data exfiltration by limiting the amount of data that can be retrieved in a single query. This can be useful in situations where an attacker is attempting to exfiltrate sensitive data from a database, as it can help prevent the attacker from retrieving large amounts of data at once.



**Command** ([[Limit Results]]):

```bash
SELECT * FROM customers LIMIT 5;
```



4. The 'database_to_xml' command is used to dump the current database to an XML file. The first argument specifies whether to include the table schema in the output. The second argument specifies whether to include the column names in the output. The third argument specifies the name of the output file. The 'database_to_xmlschema' command is used to dump the current database to an XML schema file. The first argument specifies whether to include the table schema in the output. The second argument specifies whether to include the column names in the output. The third argument specifies the name of the output file.

 



**Code**: [[select database_to_xml(true,true,''); -- dump the ]]



> Example usage: 

select database_to_xml(true,true,'my_database.xml');

This will dump the current database to an XML file named 'my_database.xml', including the table schema and column names in the output.



**Command** ([[Dump current database to XML]]):

```bash
select database_to_xml(true,true,'');
```





**Command** ([[Dump current database to XML schema]]):

```bash
select database_to_xmlschema(true,true,'');
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Commands Used

- [[Convert query result to XML]]
- [[Convert Query to XML]]
- [[Dump current database to XML]]
- [[Dump current database to XML schema]]
- [[Limit Results]]

## Tags

- [[PostgreSQL injection]]
- [[PostgreSQL XML helpers]]


