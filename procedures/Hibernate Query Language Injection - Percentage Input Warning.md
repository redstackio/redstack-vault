---
id: f31a204a-7ffc-47c5-8a3e-f1237b2694e4
name: Hibernate Query Language Injection - Percentage Input Warning
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.246620+00:00'
updated_at: '2023-04-10T20:22:27.710927+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Hibernate Query Language Injection]]'
- '[[Summary]]'
---

# Hibernate Query Language Injection - Percentage Input Warning

## Summary

Hibernate is an Object-Relational Mapping (ORM) framework for Java. It allows developers to map Java classes to database tables. Hibernate Query Language (HQL) is a powerful query language that allows developers to retrieve data from the database. However, if user input is not properly sanitized, i

## Description

# Description

Hibernate is an Object-Relational Mapping (ORM) framework for Java. It allows developers to map Java classes to database tables. Hibernate Query Language (HQL) is a powerful query language that allows developers to retrieve data from the database. However, if user input is not properly sanitized, it can lead to HQL injection. This can allow an attacker to execute arbitrary HQL statements, leading to data theft or manipulation.

The Percentage Input Warning is a defense mechanism that warns users when they input the % character in a search field. This is because the % character is used in HQL to match any character or sequence of characters in a query. By warning users about the use of the % character, the organization can prevent accidental HQL injection.

 

## Requirements

1. The application must use Hibernate as its ORM framework.

1. The application must have a search function that uses HQL.

1. The application must be able to detect the % character in user input.

 

## Defense

1. Sanitize user input by removing or escaping characters that have special meaning in HQL.

1. Implement input validation to ensure that user input adheres to expected formats and values.

1. Monitor the application for suspicious HQL queries, such as those containing unusual characters or syntax.

 

## Objectives

1. To prevent accidental HQL injection by warning users about the use of the % character in search fields.

 

# Instructions

1. Please enter the required input between the percentage symbols.

 



**Code**: [[%INJECT_HERE%]]



> This field requires input that should always be between the percentage symbols. Please make sure to include the percentage symbols in your input, as they are required for this field to function properly.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[Hibernate Query Language Injection]]
- [[Summary]]


