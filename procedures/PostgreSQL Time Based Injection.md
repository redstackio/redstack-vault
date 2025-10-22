---
id: d473422d-245f-438b-895f-7ae73da05686
name: PostgreSQL Time Based Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.835378+00:00'
updated_at: '2023-04-10T20:23:17.219851+00:00'
tags:
- '[[Identify time based]]'
- '[[PostgreSQL injection]]'
- '[[PostgreSQL Time Based]]'
---

# PostgreSQL Time Based Injection

## Summary

PostgreSQL Time Based Injection is a technique used by attackers to exploit vulnerabilities in PostgreSQL databases. This technique involves injecting malicious SQL code into an application that uses a PostgreSQL backend database. The goal of this technique is to extract sensitive information from 

## Description

# Description

PostgreSQL Time Based Injection is a technique used by attackers to exploit vulnerabilities in PostgreSQL databases. This technique involves injecting malicious SQL code into an application that uses a PostgreSQL backend database. The goal of this technique is to extract sensitive information from the database or to gain unauthorized access to the system.

To execute this technique, attackers use a specially crafted SQL injection payload that causes the database to delay its response. The attacker can then use the delay to infer information about the database, such as the number of columns in a table, or to execute arbitrary SQL commands.

Business value: By exploiting vulnerabilities in PostgreSQL databases, attackers can steal sensitive information, such as customer data or intellectual property, and disrupt business operations. This can result in financial losses, damage to reputation, and legal liability.

## Requirements

1. Access to an application that uses a PostgreSQL backend database

1. Knowledge of SQL injection techniques

## Defense

1. Use parameterized queries to prevent SQL injection attacks

1. Implement access controls to limit the amount of information that can be accessed through the database

1. Regularly monitor database activity for suspicious behavior

## Objectives

1. Extract sensitive information from a PostgreSQL database

1. Gain unauthorized access to a system

# Instructions

1. This command is used for SQL injection attacks that cause long execution times. The 'pg_sleep' function is used to delay the execution of the query by the specified number of seconds. The semicolon ';' is used to separate multiple queries, and the '||' operator is used to concatenate the results of multiple queries.

**Code**: [[select 1 from pg_sleep(5)
;(select 1 from pg_sleep]]

> The attacker can use this command to cause a denial of service attack by making the database unresponsive for an extended period of time. This command can also be used to extract sensitive information from the database by concatenating the results of multiple queries.

## Tags

- [[Identify time based]]
- [[PostgreSQL injection]]
- [[PostgreSQL Time Based]]
