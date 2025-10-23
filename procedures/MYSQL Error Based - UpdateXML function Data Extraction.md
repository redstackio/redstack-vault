---
id: dd513035-5bbf-46dc-a024-f9146aa45c89
name: MYSQL Error Based - UpdateXML function Data Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.474474+00:00'
updated_at: '2023-04-10T20:22:54.882488+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Data Obfuscation|T1001 - Data Obfuscation]]'
- '[[Password Policy Discovery|T1201 - Password Policy Discovery]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tags:
- '[[MYSQL Error Based]]'
- '[[MYSQL Error Based - UpdateXML function]]'
- '[[MYSQL Injection]]'
---

# MYSQL Error Based - UpdateXML function Data Extraction

## Summary

This procedure involves using the updatexml() function in MYSQL to extract data from a database through an SQL injection. This function is used to update an XML node, but can also be used to extract data by manipulating the XML structure of the query result. By injecting a specially crafted query, 

## Description

# Description

This procedure involves using the updatexml() function in MYSQL to extract data from a database through an SQL injection. This function is used to update an XML node, but can also be used to extract data by manipulating the XML structure of the query result. By injecting a specially crafted query, an attacker can extract data from the database. This technique can be used to extract sensitive information such as passwords, credit card details, and personal information.

Technical Explanation: The attacker injects an SQL query that includes the updatexml() function. This function manipulates the XML structure of the query result to extract data from the database. The attacker can use this technique to extract data from the database without knowing the exact structure of the database. 

Business Value: This technique can be used by attackers to gain access to sensitive information that can be used for financial gain or other malicious purposes.

 

## Requirements

1. Access to the MYSQL database

1. Knowledge of the database structure

1. Ability to inject SQL queries

 

## Defense

1. Use prepared statements or parameterized queries to prevent SQL injection attacks

1. Implement input validation to prevent malicious input from being accepted

1. Limit the privileges of database users to prevent unauthorized access

 

## Objectives

1. Extract sensitive information from the database

1. Gain unauthorized access to the database

 

# Instructions

1. This command can be used to extract data from a database using SQL injection. The command uses the updatexml function to inject SQL code into the database. The command can extract information such as the database version, schema names, table names, column names, and data information. The command should be modified to include the appropriate database and table names.

 



**Code**: [[AND updatexml(rand(),concat(CHAR(126),version(),CH]]



> The 'data_offset' parameter can be used to specify the offset of the data that needs to be extracted. The 'data_table' parameter should be replaced with the name of the table from which data needs to be extracted. The 'data_column' parameter should be replaced with the name of the column from which data needs to be extracted. The extracted data will be enclosed in '~' characters.

2. This command exploits a SQL injection vulnerability using the updatexml() function. The attacker can modify the SQL query to extract sensitive information from the database.

 



**Code**: [[' and updatexml(null,concat(0x0a,version()),null)-]]



> The 'updatexml()' function is used to modify the XML data in a database. An attacker can use this function to modify the SQL query to extract sensitive information from the database. In this example, the attacker is trying to extract the version number of the database and the name of the first table in the database. The 'concat()' function is used to concatenate the extracted data with a newline character. The double dash '--' is used to comment out the rest of the query, so that the attacker's injected code is the last thing the database executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Data Obfuscation|T1001 - Data Obfuscation]]
- [[Password Policy Discovery|T1201 - Password Policy Discovery]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

## Tags

- [[MYSQL Error Based]]
- [[MYSQL Error Based - UpdateXML function]]
- [[MYSQL Injection]]


