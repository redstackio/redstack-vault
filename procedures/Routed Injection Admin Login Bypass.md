---
id: c9ab2a5f-0fcc-4b16-a365-4d0eb6bf0e9a
name: Routed Injection Admin Login Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.630525+00:00'
updated_at: '2023-04-10T20:24:26.637255+00:00'
tags:
- '[[Routed injection]]'
- '[[SQL Injection]]'
---

# Routed Injection Admin Login Bypass

## Summary

Routed Injection Admin Login Bypass is a technique used to bypass authentication mechanisms in web applications that are vulnerable to SQL injection attacks. This technique involves modifying the URL of the web application in such a way that it injects SQL code into the backend database. This can a

## Description

# Description

Routed Injection Admin Login Bypass is a technique used to bypass authentication mechanisms in web applications that are vulnerable to SQL injection attacks. This technique involves modifying the URL of the web application in such a way that it injects SQL code into the backend database. This can allow an attacker to bypass authentication mechanisms and gain access to administrative features of the web application.

From a technical perspective, this technique involves identifying a vulnerable parameter in the web application and injecting SQL code into that parameter. Once the SQL code is injected, it can be used to modify the behavior of the application and bypass authentication mechanisms.

The business value of this technique is that it allows an attacker to gain access to sensitive information and administrative features of a web application, which can lead to data theft, financial loss, and reputational damage for the targeted organization.

## Requirements

1. Access to a vulnerable web application that is susceptible to SQL injection attacks

1. Knowledge of SQL injection techniques

1. Ability to modify URLs and inject SQL code

## Defense

1. Implement input validation and sanitization techniques to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Implement multi-factor authentication mechanisms to prevent unauthorized access to administrative features

## Objectives

1. Bypass authentication mechanisms in a vulnerable web application

1. Gain access to administrative features of the web application

# Instructions

1. This command allows the user to bypass the login authentication process for an admin user by injecting a SQL query into the login form. The injected query selects the username 'admin' and a pre-computed hash value for the password '1234'.

**Code**: [[admin' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb]]

> The 'admin' username and '1234' password hash are hardcoded into the SQL query. The 'AND 1=0' statement is used to make the original authentication query return no results, and the 'UNION ALL' statement is used to concatenate the injected query with the original query. This allows the injected query to execute and return the hardcoded admin credentials, which are then used to log in as an admin user.

## Tags

- [[Routed injection]]
- [[SQL Injection]]
