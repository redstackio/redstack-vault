---
id: f8e34c15-5c73-4c02-9a1b-b0db495571f1
name: Cassandra Login Bypass using Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.478835+00:00'
updated_at: '2023-04-06T03:56:32.493604+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[CMSTP|T1191 - CMSTP]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Cassandra Injection]]'
- '[[Cassandra - Login Bypass]]'
- '[[Login Bypass 0]]'
---

# Cassandra Login Bypass using Injection

## Summary

Cassandra Login Bypass using Injection is a technique used by attackers to bypass the login mechanism of a Cassandra database. This technique involves exploiting a vulnerability in the login mechanism of the Cassandra database by injecting malicious code to bypass the authentication process. This a

## Description

# Description

Cassandra Login Bypass using Injection is a technique used by attackers to bypass the login mechanism of a Cassandra database. This technique involves exploiting a vulnerability in the login mechanism of the Cassandra database by injecting malicious code to bypass the authentication process. This attack can be carried out by exploiting a software vulnerability or by exploiting a misconfigured public-facing application. By bypassing the login mechanism, attackers can gain access to sensitive information stored in the database, including admin credentials.

From a technical perspective, this attack involves injecting malicious code into the login form of the Cassandra database. The attacker can then use this code to bypass the authentication process and gain access to the database. This attack can be carried out using a variety of tools and techniques, including SQL injection and cross-site scripting (XSS) attacks.

The business value of this attack is that it allows attackers to gain access to sensitive information stored in the Cassandra database, including admin credentials. This information can then be used to carry out further attacks against the organization, such as data exfiltration, ransomware attacks, and more.

## Requirements

1. Access to the target network

1. Knowledge of the login mechanism of the target Cassandra database

1. Knowledge of SQL injection and cross-site scripting (XSS) attacks

## Defense

1. Ensure that all public-facing applications are properly configured and do not contain any vulnerabilities that can be exploited

1. Regularly scan and test all applications and systems for vulnerabilities and patch them as soon as possible

1. Implement strong authentication mechanisms, such as multi-factor authentication, to prevent unauthorized access to sensitive information

## Objectives

1. Bypass the login mechanism of a Cassandra database

1. Gain access to sensitive information stored in the database

1. Retrieve admin credentials

# Instructions

1. To retrieve the admin credentials, execute the following SQL command:

**Code**: [[username: admin' ALLOW FILTERING; %00
password: AN]]

> This command exploits a vulnerability in the authentication system by injecting a malicious query. The 'ALLOW FILTERING' keyword allows the query to bypass certain security restrictions and return all results. The injected username 'admin' combined with the wildcard character '%' and the null byte '%00' forces the query to return the password associated with the admin account. Note that this command should only be used for ethical hacking and penetration testing purposes with proper authorization and consent.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[CMSTP|T1191 - CMSTP]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[Cassandra Injection]]
- [[Cassandra - Login Bypass]]
- [[Login Bypass 0]]
