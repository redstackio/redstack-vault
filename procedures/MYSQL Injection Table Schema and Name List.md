---
id: 51b957e2-6bb2-412b-ae0b-5247609af4e6
name: MYSQL Injection Table Schema and Name List
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.945263+00:00'
updated_at: '2023-04-10T20:22:57.296345+00:00'
tags:
- '[[MYSQL Fast Exploitation]]'
- '[[MYSQL Injection]]'
---

# MYSQL Injection Table Schema and Name List

## Summary

MYSQL Injection is a type of injection attack that targets MYSQL databases. By exploiting vulnerabilities in the application or web page, an attacker can execute arbitrary SQL commands, which can lead to data theft or modification. The MYSQL Fast Exploitation procedure allows an attacker to quickly

## Description

# Description

MYSQL Injection is a type of injection attack that targets MYSQL databases. By exploiting vulnerabilities in the application or web page, an attacker can execute arbitrary SQL commands, which can lead to data theft or modification. The MYSQL Fast Exploitation procedure allows an attacker to quickly obtain the table schema and name list of a MYSQL database, which can be used to further exploit the database. This procedure can be used for both offensive and defensive purposes. 

Technical Explanation: The attacker sends a specially crafted SQL query to the application or web page, which is then executed by the MYSQL database. The query is designed to extract the table schema and name list of the database. 

Business Value: This procedure can be used by attackers to gain unauthorized access to sensitive data stored in a MYSQL database. It can also be used by security professionals to test the security of their applications and web pages, and to identify vulnerabilities before they can be exploited by attackers.

 

## Requirements

1. Access to a vulnerable application or web page

1. Knowledge of MYSQL injection techniques

 

## Defense

1. Implement input validation and parameterization to prevent MYSQL injection attacks

1. Use prepared statements and stored procedures to prevent SQL injection attacks

1. Regularly update and patch MYSQL databases to prevent known vulnerabilities

 

## Objectives

1. Obtain the table schema and name list of a MYSQL database

1. Use the obtained information to further exploit the database

 

# Instructions

1. This command retrieves a list of all table schemas and their corresponding table names from the INFORMATION_SCHEMA.TABLES system table. The result is returned as a JSON array.

 



**Code**: [[SELECT json_arrayagg(concat_ws(0x3a,table_schema,t]]



> The 'json_arrayagg' function is used to concatenate the table schema and name values into a single string separated by a colon. This string is then aggregated into a JSON array using the 'json_arrayagg' function. The resulting JSON array is returned as the output of the command.

## Tags

- [[MYSQL Fast Exploitation]]
- [[MYSQL Injection]]


