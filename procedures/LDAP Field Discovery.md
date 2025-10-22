---
id: ae86accf-e897-4873-bcca-35c40051213f
name: LDAP Field Discovery
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.712607+00:00'
updated_at: '2023-04-10T20:36:28.016198+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Discover valid LDAP fields]]'
- '[[LDAP Injection]]'
- '[[Scripts]]'
---

# LDAP Field Discovery

## Summary

LDAP injection is an attack technique used to exploit web applications that construct LDAP statements from user-supplied input. The attacker injects malicious LDAP statements into an application, which then passes the statements to the LDAP server. By leveraging LDAP injection, an attacker can gain

## Description

# Description

LDAP injection is an attack technique used to exploit web applications that construct LDAP statements from user-supplied input. The attacker injects malicious LDAP statements into an application, which then passes the statements to the LDAP server. By leveraging LDAP injection, an attacker can gain unauthorized access to sensitive data or execute unauthorized operations on the LDAP server. This script discovers valid LDAP fields by iterating through a wordlist of common attributes and sending requests to the target URL. If a true condition is found in the response, the attribute is added to the list of valid fields.

## Requirements

1. Access to the target URL.

## Defense

1. Input validation and sanitization can help prevent LDAP injection attacks.

1. Implementing access controls and limiting the privileges of LDAP service accounts can help mitigate the impact of an LDAP injection attack.

1. Monitoring LDAP logs for suspicious activity can help detect and respond to LDAP injection attacks.

## Objectives

1. Discover valid LDAP fields for use in subsequent injection attacks.

# Instructions

1. To use this script, save it to a local file and modify the URL and wordlist variables as needed. Then, run the script from the command line.

**Code**: [[#!/usr/bin/python3

import requests
import string
]]

> The script uses the requests library to send HTTP POST requests to the target URL. The payload for each request includes a crafted LDAP statement that includes the current attribute value from the wordlist. If a true condition is found in the response, the attribute is considered valid and added to the list of valid fields. The list of valid fields is then printed to the console.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[Discover valid LDAP fields]]
- [[LDAP Injection]]
- [[Scripts]]
