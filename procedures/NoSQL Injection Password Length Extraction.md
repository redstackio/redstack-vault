---
id: 1e536e9e-1c61-4852-a2b6-cf168e68bd37
name: NoSQL Injection Password Length Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.448796+00:00'
updated_at: '2023-04-10T20:23:02.029025+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Bash History|T1139 - Bash History]]'
tags:
- '[[Exploit]]'
- '[[Extract length information]]'
- '[[NoSQL Injection]]'
---

# NoSQL Injection Password Length Extraction

## Summary

NoSQL Injection is a type of injection attack that targets NoSQL databases. In this specific procedure, the attacker is attempting to extract password length information from the database using a NoSQL Injection exploit. By sending specially crafted queries to the database, the attacker can extract

## Description

# Description

NoSQL Injection is a type of injection attack that targets NoSQL databases. In this specific procedure, the attacker is attempting to extract password length information from the database using a NoSQL Injection exploit. By sending specially crafted queries to the database, the attacker can extract length information about the password field. This information can be used to optimize a password brute force attack. From a technical perspective, the attacker is manipulating the query syntax to bypass input validation and inject malicious code into the database. The business value of this procedure is that it allows an attacker to gain unauthorized access to sensitive information, such as user credentials, which can lead to data theft and other malicious activities.

## Requirements

1. Access to the target NoSQL database.

1. Knowledge of the database structure and query syntax.

1. Tools for crafting and executing NoSQL Injection queries.

## Defense

1. Implement input validation and sanitization to prevent NoSQL Injection attacks.

1. Use parameterized queries or prepared statements to avoid injection vulnerabilities.

1. Monitor database activity for suspicious queries and access attempts.

## Objectives

1. Extract password length information from the NoSQL database.

1. Optimize password brute force attacks using the extracted information.

# Instructions

1. This command is used to perform a password bruteforce attack. It takes two arguments, username and password. The username argument is used to specify the target account for the attack. The password argument is a regex pattern that is used to generate a list of possible passwords for the attack. The regex pattern should be in the format of '.{n}', where n is the length of the password to be generated.

**Code**: [[username[$ne]=toto&password[$regex]=.{1}
username[]]

> The command generates a list of passwords based on the regex pattern provided and attempts to login to the target account using each password in the list. The command will stop once a valid password is found or the list of passwords is exhausted. This command should only be used for legal and authorized security testing purposes.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Bash History|T1139 - Bash History]]

## Tags

- [[Exploit]]
- [[Extract length information]]
- [[NoSQL Injection]]
