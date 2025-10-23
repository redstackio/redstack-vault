---
id: 9ae3e079-dd5c-42d2-bb46-a66cff9aeb13
name: HQL Injection via Unsupported Comment Error
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.267178+00:00'
updated_at: '2023-04-10T20:22:25.759702+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Password Policy Discovery|T1201 - Password Policy Discovery]]'
tags:
- '[[Hibernate Query Language Injection]]'
- '[[HQL Comments]]'
---

# HQL Injection via Unsupported Comment Error

## Summary

HQL injection is an attack technique that exploits input validation vulnerabilities in an application that uses Hibernate Query Language (HQL). This technique involves injecting malicious code into an HQL statement via unsupported comments to manipulate the query's logic and extract sensitive infor

## Description

# Description

HQL injection is an attack technique that exploits input validation vulnerabilities in an application that uses Hibernate Query Language (HQL). This technique involves injecting malicious code into an HQL statement via unsupported comments to manipulate the query's logic and extract sensitive information. Attackers can use this technique to bypass authentication mechanisms, extract sensitive data, and execute arbitrary code. HQL injection is a serious threat to applications that use Hibernate, and developers should take steps to prevent it.

 

## Requirements

1. Access to the application's input validation mechanism

1. Knowledge of the application's HQL syntax

1. Ability to inject unsupported comments into the HQL statement

 

## Defense

1. Validate and sanitize user input to prevent injection attacks

1. Use parameterized queries instead of string concatenation to build HQL statements

1. Implement strict input validation and output encoding to prevent attacks

 

## Objectives

1. Extract sensitive data from the application's database

1. Bypass authentication mechanisms

1. Execute arbitrary code on the target system

 

# Instructions

1. To avoid this error, please remove any comments from your HQL code.

 



**Code**: [[HQL does not support comments]]



> HQL is a SQL-like language used in Hive. While SQL supports comments, HQL does not. Therefore, any comments within your HQL code will result in an error. To avoid this error, please remove any comments from your HQL code before running it in Hive.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Password Policy Discovery|T1201 - Password Policy Discovery]]

## Tags

- [[Hibernate Query Language Injection]]
- [[HQL Comments]]


