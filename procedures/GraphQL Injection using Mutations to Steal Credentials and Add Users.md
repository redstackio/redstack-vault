---
id: 8463518b-7952-405a-a302-5872b72a83b2
name: GraphQL Injection using Mutations to Steal Credentials and Add Users
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.902054+00:00'
updated_at: '2023-04-10T20:22:22.881716+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Exploit]]'
- '[[GraphQL Injection]]'
- '[[Use mutations]]'
commands:
- '[[Add user with id 1]]'
- '[[Sign in as Admin]]'
---

# GraphQL Injection using Mutations to Steal Credentials and Add Users

## Summary

GraphQL Injection is a technique used to exploit vulnerabilities in GraphQL APIs. In this procedure, we will use mutations to steal user credentials and add new users to the system. By injecting malicious code into the GraphQL query, we can bypass security measures and gain unauthorized access to s

## Description

# Description

GraphQL Injection is a technique used to exploit vulnerabilities in GraphQL APIs. In this procedure, we will use mutations to steal user credentials and add new users to the system. By injecting malicious code into the GraphQL query, we can bypass security measures and gain unauthorized access to sensitive data. This attack can have severe consequences, including data theft, identity theft, and financial loss. 

Technical Explanation: GraphQL is a query language used to interact with APIs. Mutations are a type of query that allows users to modify data on the server. In this procedure, we will use mutations to execute malicious code and steal user credentials. We will also add new users to the system, giving us unauthorized access to sensitive data. 

Business Value: This procedure demonstrates the importance of securing GraphQL APIs. By implementing security measures such as input validation and query whitelisting, organizations can protect themselves from GraphQL Injection attacks.

## Requirements

1. Access to a vulnerable GraphQL API

## Defense

1. Implement input validation to prevent SQL injection attacks.

1. Implement query whitelisting to restrict access to sensitive data.

1. Regularly update and patch the GraphQL API to protect against known vulnerabilities.

## Objectives

1. To steal user credentials

1. To add new users to the system

# Instructions

1. To execute this attack, we will use two mutations. The first mutation will sign in as the admin user and return a token. The second mutation will add a new user to the system. We will inject malicious code into the mutations to steal user credentials and gain unauthorized access to sensitive data.

**Code**: [[# mutation{signIn(login:"Admin", password:"secretp]]

> The signIn mutation is used to sign in as the admin user and return a token. We will use this token to authenticate ourselves for the second mutation. The addUser mutation is used to add a new user to the system. We will inject malicious code into the name and email fields to steal user credentials. For example, we can use the following code to steal user credentials: 

id: "1", name: "Dan Abramov", email: "dan@dan.com" UNION SELECT id, password, email FROM users --"

This code will inject a SQL injection attack into the GraphQL query, allowing us to steal user credentials. We can also use similar code to add a new user to the system and gain unauthorized access to sensitive data.

**Command** ([[Sign in as Admin]]):

```bash
# mutation{signIn(login:"Admin", password:"secretp@ssw0rd"){token}}
```

**Command** ([[Add user with id 1]]):

```bash
# mutation{addUser(id:"1", name:"Dan Abramov", email:"dan@dan.com") {id name email}}
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Add user with id 1]]
- [[Sign in as Admin]]

## Tags

- [[Exploit]]
- [[GraphQL Injection]]
- [[Use mutations]]
