---
id: f3f46d0f-7f5b-450c-8e19-957a97d31e62
name: Blind NoSQL Injection via Brute Force
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.559677+00:00'
updated_at: '2023-04-10T20:23:02.733998+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
sub_techniques:
- '[[Password Guessing|T1110.001 - Password Guessing]]'
tags:
- '[[Blind NoSQL]]'
- '[[GET]]'
- '[[NoSQL Injection]]'
---

# Blind NoSQL Injection via Brute Force

## Summary

Blind NoSQL injection is a type of injection attack that targets NoSQL databases. Unlike traditional SQL injection attacks, blind NoSQL injection attacks do not rely on error messages to extract information from the database. Instead, attackers use brute force techniques to guess the correct input 

## Description

# Description

Blind NoSQL injection is a type of injection attack that targets NoSQL databases. Unlike traditional SQL injection attacks, blind NoSQL injection attacks do not rely on error messages to extract information from the database. Instead, attackers use brute force techniques to guess the correct input values that allow them to extract data from the database. In this specific case, the attacker is using brute force techniques to guess login credentials and gain access to the database. This attack can be highly effective against weak passwords and poorly secured systems.

From a technical perspective, NoSQL injection attacks occur when an attacker is able to inject malicious code into a NoSQL query. This code can then be executed by the database, allowing the attacker to extract sensitive information from the database. In this specific case, the attacker is attempting to guess login credentials by repeatedly submitting login requests with different username/password combinations.

From a business perspective, blind NoSQL injection attacks can be highly damaging to organizations. If successful, attackers can gain access to sensitive data such as customer information, financial records, and intellectual property. This can result in reputational damage, financial losses, and legal liabilities.

## Requirements

1. Access to the target network

1. Knowledge of the target's NoSQL database system

1. Brute force tool capable of guessing login credentials

## Defense

1. Implement strong password policies, including the use of complex passwords and multi-factor authentication

1. Monitor network traffic for suspicious login attempts and implement rate limiting to prevent brute force attacks

1. Regularly update and patch NoSQL database systems to address known vulnerabilities

## Objectives

1. Gain unauthorized access to a NoSQL database

1. Extract sensitive information from the database

# Instructions

1. This script is used to brute force MongoDB password. It uses string.printable to generate all possible characters and sends requests to the MongoDB login page with a payload containing the username and password[$regex] parameter. The password[$regex] parameter is used to match the password against a regular expression. If the response contains the word 'Yeah', it means that the password is correct and the script prints the password.

**Code**: [[import requests
import urllib3
import string
impor]]

> The script requires the user to modify the 'username' and 'u' variables with their own values. The 'username' variable should contain the username for the MongoDB server and the 'u' variable should contain the URL of the MongoDB login page. The script will use string.printable to generate all possible characters for the password and send requests to the login page with a payload containing the username and password[$regex] parameter. The password[$regex] parameter is used to match the password against a regular expression. If the response contains the word 'Yeah', it means that the password is correct and the script prints the password. The script can be modified to use a different character set for the password or to use a different payload for the requests.

2. This script uses a brute force method to login to a website by guessing the password using regex.

**Code**: [[require 'httpx'

username = 'admin'
password = ''
]]

> The script takes the username and an empty password as input. It then uses a list of characters and symbols to generate all possible combinations of passwords. It sends a GET request to the website with each combination and the username. The password is sent using a regex pattern. If the response body contains the word 'Yeah', it means that the password is correct and the script moves on to the next character. The script continues this process until it finds the correct password.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

### Sub-Techniques

- [[Password Guessing|T1110.001 - Password Guessing]]

## Tags

- [[Blind NoSQL]]
- [[GET]]
- [[NoSQL Injection]]
