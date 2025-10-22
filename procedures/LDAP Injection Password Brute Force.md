---
id: cfe703b1-90e3-434a-bbe9-6a6e11c36a31
name: LDAP Injection Password Brute Force
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.733202+00:00'
updated_at: '2023-04-10T20:36:29.407900+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Password Policy Discovery|T1201 - Password Policy Discovery]]'
tags:
- '[[LDAP Injection]]'
- '[[Scripts]]'
- '[[Special blind LDAP injection (without "*")]]'
---

# LDAP Injection Password Brute Force

## Summary

This procedure is a script that performs a password brute force attack using LDAP injection. The script tries to find the password of the admin user by injecting LDAP queries with a password that is being built character by character. The attack is performed blindly, meaning that there is no feedba

## Description

# Description

This procedure is a script that performs a password brute force attack using LDAP injection. The script tries to find the password of the admin user by injecting LDAP queries with a password that is being built character by character. The attack is performed blindly, meaning that there is no feedback from the server on whether the password is correct or not. The script tries all possible characters for each position until the password is found. This procedure can be used by an attacker to gain access to sensitive information or systems.

## Requirements

1. Access to the target system

1. Python3 or Ruby installed

## Defense

1. Implement input validation to prevent LDAP injection attacks

1. Implement account lockout policies to prevent brute force attacks

1. Implement multi-factor authentication to prevent unauthorized access

## Objectives

1. Find the password of the admin user using LDAP injection

1. Gain unauthorized access to sensitive information or systems

# Instructions

1. The script should be run with Python3. The alphabet variable contains all the possible characters that can be used in the password. The flag variable is the password that is being built character by character. The script tries all possible characters for each position until the password is found.

**Code**: [[#!/usr/bin/python3

import requests, string
alphab]]

> The script performs a password brute force attack using LDAP injection. It sends requests to the target server with an LDAP query that injects the password being built character by character. If the query returns a "TRUE CONDITION" response, it means that the password is correct and the script moves on to the next character. If the query returns a "FALSE CONDITION" response, it means that the password is incorrect and the script tries the next character.

2. The script should be run with Ruby. The alphabet variable contains all the possible characters that can be used in the password. The flag variable is the password that is being built character by character. The script tries all possible characters for each position until the password is found.

**Code**: [[#!/usr/bin/env ruby

require 'net/http'
alphabet =]]

> The script performs a password brute force attack using LDAP injection. It sends requests to the target server with an LDAP query that injects the password being built character by character. If the query returns a "TRUE CONDITION" response, it means that the password is correct and the script moves on to the next character. If the query returns a "FALSE CONDITION" response, it means that the password is incorrect and the script tries the next character.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Password Policy Discovery|T1201 - Password Policy Discovery]]

## Tags

- [[LDAP Injection]]
- [[Scripts]]
- [[Special blind LDAP injection (without "*")]]
