---
id: 3d2c5178-b84f-47c6-8418-948e5a6aa807
name: Brute Force Login with MongoDB Query Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.517650+00:00'
updated_at: '2023-04-10T20:23:01.631145+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[DCShadow|T1207 - DCShadow]]'
tags:
- '[[Blind NoSQL]]'
- '[[NoSQL Injection]]'
- '[[POST with JSON body]]'
---

# Brute Force Login with MongoDB Query Injection

## Summary

Brute force login with MongoDB query injection is a technique used by attackers to gain unauthorized access to a system by exploiting vulnerabilities in the login process. This attack involves sending specially crafted MongoDB queries in the JSON body of a POST request to the server. The queries ar

## Description

# Description

Brute force login with MongoDB query injection is a technique used by attackers to gain unauthorized access to a system by exploiting vulnerabilities in the login process. This attack involves sending specially crafted MongoDB queries in the JSON body of a POST request to the server. The queries are designed to bypass authentication and grant access to the attacker. This attack is particularly effective against systems that use MongoDB as their database backend.

From a technical perspective, this attack works by injecting malicious code into the MongoDB queries used by the login process. The attacker sends a series of queries that attempt to guess the correct username and password combination. If successful, the attacker gains access to the system and can perform unauthorized actions. This attack can be difficult to detect, as it does not generate any errors or warnings in the server logs.

From a business perspective, this attack can result in the theft of sensitive data, financial loss, and damage to the reputation of the affected organization.

 

## Requirements

1. Access to a vulnerable system

1. Knowledge of the login process and MongoDB query syntax

1. Tools for crafting and sending POST requests with JSON bodies

 

## Defense

1. Use parameterized queries to prevent injection attacks

1. Implement rate limiting to prevent brute force attacks

1. Monitor server logs for suspicious activity

 

## Objectives

1. Gain unauthorized access to a system

1. Bypass authentication

1. Perform unauthorized actions

 

# Instructions

1. This script performs a brute force login attack using MongoDB query injection. It uses a loop to iterate through the printable ASCII characters except for '*', '+', '.', '?', and '|'. It then constructs a payload that queries the MongoDB database for a matching username and password. The password is constructed one character at a time and tested against the server until a successful login is found.

 



**Code**: [[import requests
import urllib3
import string
impor]]



> The script requires the requests, urllib3, string, and urllib modules. The username and initial password are set in the script. The script sends a POST request to the login page with a payload that queries the MongoDB database for a matching username and password. The password is constructed one character at a time and tested against the server until a successful login is found. The script prints each character as it is found and adds it to the password variable until the full password is discovered.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[DCShadow|T1207 - DCShadow]]

## Tags

- [[Blind NoSQL]]
- [[NoSQL Injection]]
- [[POST with JSON body]]


