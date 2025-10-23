---
id: c8447fdf-508a-4204-a6dc-baa93c854b26
name: HQL List Columns Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.286526+00:00'
updated_at: '2023-04-10T20:22:26.594989+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Sudo Caching|T1206 - Sudo Caching]]'
tags:
- '[[Hibernate Query Language Injection]]'
- '[[HQL List Columns]]'
---

# HQL List Columns Injection

## Summary

HQL List Columns Injection is a technique that takes advantage of a vulnerability in the Hibernate Query Language (HQL) syntax to extract information from an application's database. Attackers can use this technique to bypass authentication mechanisms, extract sensitive information, and perform othe

## Description

# Description

HQL List Columns Injection is a technique that takes advantage of a vulnerability in the Hibernate Query Language (HQL) syntax to extract information from an application's database. Attackers can use this technique to bypass authentication mechanisms, extract sensitive information, and perform other malicious actions. HQL List Columns Injection works by injecting malicious HQL code into an application's input fields, which is then executed by the application's database.

 

## Requirements

1. Access to an application with a vulnerable HQL syntax

1. Knowledge of HQL syntax and injection techniques

 

## Defense

1. Use parameterized queries to prevent injection attacks

1. Implement input validation and sanitization to prevent malicious input from being executed

1. Regularly update and patch the application to prevent known vulnerabilities from being exploited

 

## Objectives

1. Extract sensitive information from the application's database

1. Bypass authentication mechanisms

1. Perform other malicious actions

 

# Instructions

1. To find all blog posts with a specific title, replace the '%' in the 'title like' clause with your desired search term. Make sure to keep the single quotes around the search term. Also, make sure that the 'published' field is set to 'true'.

 



**Code**: [[from BlogPosts
where title like '%'
  and DOESNT_E]]



> This SQL query searches for all blog posts in the 'BlogPosts' table that have a title containing the search term specified in the 'title like' clause. The 'DOESNT_EXIST=1 and ''='%' --' part of the query is a comment and can be ignored. The 'published = true' clause ensures that only published blog posts are returned.

2. When using SQL, make sure to use existing column names in the query. Double check the spelling and syntax of the column names to avoid this error.

 



**Code**: [[org.hibernate.exception.SQLGrammarException: Colum]]



> This error occurs when a query is executed on a table in a database, but the specified column does not exist in the table. The error message will display the name of the non-existing column and may also leak the names of other columns in the table. To fix this error, check the spelling and syntax of the column name in the query and ensure that it exists in the table. It is also important to note that using '%' as a wildcard in the query may cause unexpected results, so it is best to use specific search criteria instead.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Sudo Caching|T1206 - Sudo Caching]]

## Tags

- [[Hibernate Query Language Injection]]
- [[HQL List Columns]]


