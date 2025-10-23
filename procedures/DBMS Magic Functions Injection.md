---
id: f6678452-8492-432f-b89d-9dfea07d5cb2
name: DBMS Magic Functions Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.373100+00:00'
updated_at: '2023-04-10T20:22:26.967698+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[DBMS Magic functions]]'
- '[[Hibernate Query Language Injection]]'
---

# DBMS Magic Functions Injection

## Summary

DBMS Magic Functions Injection is a technique used to exploit vulnerabilities in the Hibernate Query Language (HQL) by injecting DBMS Magic Functions. This technique allows an attacker to execute arbitrary SQL commands on the backend database. DBMS Magic Functions are a set of functions that are sp

## Description

# Description

DBMS Magic Functions Injection is a technique used to exploit vulnerabilities in the Hibernate Query Language (HQL) by injecting DBMS Magic Functions. This technique allows an attacker to execute arbitrary SQL commands on the backend database. DBMS Magic Functions are a set of functions that are specific to a particular database management system (DBMS) and can be used to perform various operations such as retrieving the current user, database version, and executing system commands. The successful exploitation of this technique can lead to data exfiltration, privilege escalation, and complete compromise of the target system.

 

## Requirements

1. Access to the target system

1. Knowledge of the HQL syntax

1. Knowledge of the target database management system and its specific DBMS Magic Functions

 

## Defense

1. Use parameterized queries instead of concatenating user input with SQL queries

1. Implement input validation and sanitization to prevent the injection of malicious code

1. Regularly update and patch the software and database management system to mitigate known vulnerabilities

 

## Objectives

1. To execute arbitrary SQL commands on the backend database

1. To retrieve sensitive information from the database

1. To escalate privileges on the target system

 

# Instructions

1. The query_to_xml function in PostgreSQL converts the result of an SQL query into an XML document. The function takes a single argument, which is the SQL query to be executed. The result of the query is returned as an XML document.

 



**Code**: [[query_to_xml(&#39;Arbitrary SQL&#39;)]]



> This function can be useful when you need to generate an XML document from the result of a SQL query. The resulting XML document can be used as input for other applications or as a standalone document. The argument to the function should be a valid SQL query that returns a result set.

2. The array_upper() function returns the length of the specified array. In this command, we are using the xpath() and query_to_xml() functions to create an array and then retrieve its length.

 

The 'array_upper' function takes two arguments: the array and the dimension to return the upper boundary for. In this case, we are passing the result of the 'xpath' function, which searches an XML document for a specified node or nodes and returns the matching nodes as an array. The 'query_to_xml' function is used to generate an XML document from a SQL query. In this case, the query 'select 1 where 1337>1' returns a single row with a value of 1, which is then converted to an XML document. The 'array_upper' function is then used to retrieve the length of the resulting array, which is 1 in this case.

3. To generate XML from SQL in Oracle, use the built-in function DBMS_XMLGEN.getxml(). This function takes a SQL query as an argument and returns the resultset in XML format.

 



**Code**: [[DBMS_XMLGEN.getxml(&#39;SQL&#39;)]]



> The getxml() function can be used to generate XML data from any SQL query. The XML generated can be used for a variety of purposes such as data exchange between systems or for web services. The function can be customized to include additional options such as formatting, namespaces, and XSLT transformations.

4. To check if a condition is true in Oracle DB, run the following command:
NVL(TO_CHAR(DBMS_XMLGEN.getxml('select 1 where <<condition>>')),'1')!='1'
Replace <<condition>> with the condition you want to check.

 



**Code**: [[NVL(TO_CHAR(DBMS_XMLGEN.getxml('select 1 where 133]]



> This command uses the DBMS_XMLGEN.getxml function to execute a select statement with the condition provided. If the condition is true, the select statement will return a row with the value 1. The NVL function is used to convert the result of DBMS_XMLGEN.getxml to a string, which is then compared to the string '1'. If the condition is true, the result will be '1' and the != operator will return false, so the whole expression will return false. If the condition is false, the result will be null and the != operator will return true, so the whole expression will return true.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[DBMS Magic functions]]
- [[Hibernate Query Language Injection]]


