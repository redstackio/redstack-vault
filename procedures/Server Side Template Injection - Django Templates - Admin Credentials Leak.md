---
id: 2f441894-3996-4131-8cdf-5f3d5fabcdc8
name: Server Side Template Injection - Django Templates - Admin Credentials Leak
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.542324+00:00'
updated_at: '2023-04-10T20:23:49.625071+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Credentials in Files|T1081 - Credentials in Files]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Admin username and password hash leak]]'
- '[[Django Templates]]'
- '[[Server Side Template Injection]]'
---

# Server Side Template Injection - Django Templates - Admin Credentials Leak

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject code into a web application template, which is then executed server-side. In this specific case, the vulnerability is present in Django Templates, which is a web templating system that allows developers to de

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject code into a web application template, which is then executed server-side. In this specific case, the vulnerability is present in Django Templates, which is a web templating system that allows developers to define the structure of a web page. The attacker can exploit this vulnerability to leak the admin username and password hash, which can then be cracked to obtain the plaintext password. This can lead to full compromise of the web application and sensitive data exposure. To exploit this vulnerability, the attacker needs to have access to the web application and be able to inject code into the template.

## Requirements

1. Access to the web application

1. Ability to inject code into the template

## Defense

1. Ensure that the web application is up to date and patched against known vulnerabilities

1. Implement input validation and sanitization to prevent code injection

1. Use strong and unique passwords, and consider using multi-factor authentication to protect against password cracking

## Objectives

1. Leak admin username and password hash

1. Obtain plaintext password

1. Compromise the web application

1. Exfiltrate sensitive data

# Instructions

1. This command retrieves the recent admin logins and passwords from the system logs.

The 'get_admin_log' command retrieves the recent admin logins and passwords from the system logs. The '10' argument specifies the number of log entries to retrieve. The retrieved data is in the format of 'username : password'. This command is useful for auditing purposes and to identify any potential security breaches.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Credentials in Files|T1081 - Credentials in Files]]
- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Admin username and password hash leak]]
- [[Django Templates]]
- [[Server Side Template Injection]]
