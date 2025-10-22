---
id: 7e257717-ee01-4a1a-9c74-5d3cd36ab7a5
name: PostgreSQL Stacked Query Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.910824+00:00'
updated_at: '2023-04-10T20:23:14.029348+00:00'
tags:
- '[[PostgreSQL injection]]'
- '[[PostgreSQL Stacked Query]]'
---

# PostgreSQL Stacked Query Injection

## Summary

PostgreSQL Stacked Query Injection is a technique used by attackers to inject malicious SQL code into a PostgreSQL database through a vulnerable application. This technique allows an attacker to execute multiple SQL statements in a single request, bypassing input validation and authentication mecha

## Description

# Description

PostgreSQL Stacked Query Injection is a technique used by attackers to inject malicious SQL code into a PostgreSQL database through a vulnerable application. This technique allows an attacker to execute multiple SQL statements in a single request, bypassing input validation and authentication mechanisms. The attacker can then modify or extract sensitive data from the database, or even take control of the server hosting the database. 

From a technical perspective, PostgreSQL Stacked Query Injection is achieved by appending a semicolon (;) to the end of a legitimate SQL query and then adding a malicious SQL statement. This technique allows the attacker to execute arbitrary SQL commands, including SELECT, INSERT, UPDATE, and DELETE. 

From a business standpoint, PostgreSQL Stacked Query Injection can lead to significant financial and reputational damage. Attackers can steal sensitive customer data, such as credit card numbers and personal information, and use it for fraudulent activities. This can result in legal penalties, loss of customers, and damage to the company's reputation.

## Requirements

1. Access to a vulnerable application that uses a PostgreSQL database

1. Knowledge of SQL and the structure of the database

1. Ability to craft malicious SQL queries

## Defense

1. Sanitize user input to prevent SQL injection attacks

1. Implement proper authentication and access control mechanisms to limit the impact of successful attacks

1. Regularly update and patch the PostgreSQL database to address known vulnerabilities

## Objectives

1. Execute arbitrary SQL commands on the database server

1. Extract sensitive data from the database

1. Modify data stored in the database

# Instructions

1. To create a new table with injected data, use the following command:

**Code**: [[http://host/vuln.php?id=injection';create table No]]

> The command injects SQL code into the 'id' parameter of the URL which creates a new table called 'NotSoSecure' with a single column called 'data' that can hold up to 200 characters. The injected data is then stored in this newly created table. The semi-colon ";" is used to add another query after the injection to create the new table.

## Tags

- [[PostgreSQL injection]]
- [[PostgreSQL Stacked Query]]
