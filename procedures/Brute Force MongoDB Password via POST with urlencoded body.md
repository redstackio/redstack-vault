---
id: 4c54344f-b966-4c34-b318-9adbf99343e4
name: Brute Force MongoDB Password via POST with urlencoded body
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.538401+00:00'
updated_at: '2023-04-10T20:23:00.393196+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Blind NoSQL]]'
- '[[NoSQL Injection]]'
- '[[POST with urlencoded body]]'
---

# Brute Force MongoDB Password via POST with urlencoded body

## Summary

Brute forcing MongoDB password via POST with urlencoded body is a technique used to gain access to a MongoDB instance by guessing the password. This technique involves sending multiple requests with different passwords until the correct password is found. This technique is effective against weak pa

## Description

# Description

Brute forcing MongoDB password via POST with urlencoded body is a technique used to gain access to a MongoDB instance by guessing the password. This technique involves sending multiple requests with different passwords until the correct password is found. This technique is effective against weak passwords, and can be automated to speed up the process. 

This technique involves sending POST requests to the MongoDB instance with a urlencoded body containing the username and password. The response from the server can be used to determine if the password is correct or not.

The business value of this technique is that it can be used to gain unauthorized access to sensitive data stored in a MongoDB instance, which can lead to data theft, loss of reputation, and financial losses.

## Requirements

1. Access to the MongoDB instance

1. A tool to automate the brute force process

## Defense

1. Use strong and complex passwords to prevent brute force attacks

1. Implement rate limiting on login attempts to prevent brute force attacks

1. Monitor the MongoDB instance for suspicious activity and unauthorized access

## Objectives

1. Gain unauthorized access to a MongoDB instance

1. Steal sensitive data stored in a MongoDB instance

# Instructions

1. This script is used to brute force the password of a MongoDB database. It takes advantage of the $regex operator of MongoDB to try different combinations of passwords until the correct one is found.

**Code**: [[import requests
import urllib3
import string
impor]]

> The script first imports necessary libraries and disables warnings. It then sets the username as 'admin' and initializes an empty password. The URL of the login page is set to 'http://example.org/login' and the content type of the headers is set to 'application/x-www-form-urlencoded'.

The while loop runs indefinitely until the correct password is found. The for loop iterates through all printable characters except for some special characters. It then generates a payload with the current username and password plus the current character. This payload is sent as a POST request to the login page with the headers and other parameters set. If the status code of the response is 302 and the location header is '/dashboard', it means that the correct password has been found and the loop exits. Otherwise, the loop continues and tries the next character. Once the correct password is found, it is printed to the console.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Tags

- [[Blind NoSQL]]
- [[NoSQL Injection]]
- [[POST with urlencoded body]]
