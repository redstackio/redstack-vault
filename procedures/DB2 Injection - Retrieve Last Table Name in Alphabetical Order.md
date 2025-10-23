---
id: 08eb8a31-3319-46d5-af40-30af8811dd1a
name: DB2 Injection - Retrieve Last Table Name in Alphabetical Order
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.865841+00:00'
updated_at: '2023-04-10T20:22:00.819180+00:00'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[Select Nth Row]]'
---

# DB2 Injection - Retrieve Last Table Name in Alphabetical Order

## Summary

DB2 Injection is a type of SQL injection attack that targets IBM's DB2 database management system. In this specific procedure, the objective is to retrieve the last table name in alphabetical order. This can be useful for an attacker to gain knowledge of the database schema, which can aid in furthe

## Description

# Description

DB2 Injection is a type of SQL injection attack that targets IBM's DB2 database management system. In this specific procedure, the objective is to retrieve the last table name in alphabetical order. This can be useful for an attacker to gain knowledge of the database schema, which can aid in further attacks.

Technically, the attacker injects malicious SQL code into a vulnerable application that interacts with the DB2 database. The injected code is then executed on the database, allowing the attacker to retrieve the desired information. This procedure specifically uses the 'SELECT' statement to retrieve the last table name in alphabetical order.

The business value of this attack is that it can lead to unauthorized access to sensitive data stored in the DB2 database, such as customer information or intellectual property.

 

## Requirements

1. Access to a vulnerable application that interacts with a DB2 database

1. Knowledge of SQL injection techniques

 

## Defense

1. Input validation and sanitization should be implemented to prevent SQL injection attacks

1. Database administrators should regularly review and monitor database logs for suspicious activity

 

## Objectives

1. Retrieve the last table name in alphabetical order

1. Gain knowledge of the database schema

 

# Instructions

1. This command retrieves the name of the last table in alphabetical order from the sysibm.systables table. Replace 'N' with the number of rows you want to retrieve. If you want to retrieve the last table name only, set 'N' to 1.

 



**Code**: [[select name from (select * from sysibm.systables o]]



> SYSTABLES is a system catalog table that contains information about tables in the database. This command selects the name column from a subquery that retrieves the first 'N' rows from the SYSTABLES table in ascending order of name, and then orders those rows in descending order of name and retrieves the first row. This effectively retrieves the last table name in alphabetical order.

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[Select Nth Row]]


