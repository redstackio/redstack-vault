---
id: 41ef1c08-80b9-4bde-bc1d-15914626a775
name: ASCII Conversion XSS Filter Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.422890+00:00'
updated_at: '2023-04-10T20:21:48.860205+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Create Account|T1136 - Create Account]]'
- '[[Drive-by Compromise|T1189 - Drive-by Compromise]]'
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
tags:
- '[[Bypass quotes for string]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# ASCII Conversion XSS Filter Bypass

## Summary

The ASCII Conversion XSS Filter Bypass technique is a way to bypass filters that prevent the use of certain characters or strings in user input. This technique involves converting special characters to their ASCII equivalent, allowing them to slip past filters and execute malicious code. This techn

## Description

# Description

The ASCII Conversion XSS Filter Bypass technique is a way to bypass filters that prevent the use of certain characters or strings in user input. This technique involves converting special characters to their ASCII equivalent, allowing them to slip past filters and execute malicious code. This technique can be used to steal sensitive user data, such as login credentials, or to perform actions on behalf of the user, such as making unauthorized purchases or posting malicious content. Technicaly, the attacker converts the payload to ASCII values and then uses JavaScript to convert the ASCII values back to their original form. This technique can be used in various contexts, including web applications, email clients, and instant messaging platforms.

 

## Requirements

1. Access to a vulnerable web application or other platform with input filters that can be bypassed

1. Knowledge of ASCII conversion and JavaScript

 

## Defense

1. Implement input validation to prevent the use of special characters and strings

1. Use a web application firewall to block known XSS attacks

1. Regularly update and patch software to prevent vulnerabilities

 

## Objectives

1. Bypass input filters to execute malicious code

1. Steal sensitive user information

1. Perform unauthorized actions on behalf of the user

 

# Instructions

1. String.fromCharCode()

 



**Code**: [[String.fromCharCode(88,83,83)]]



> The String.fromCharCode() method converts Unicode values into characters. It takes one or more comma-separated integers as arguments and returns a string that corresponds to the character sequence represented by the Unicode values of those integers. In this case, the method is used to convert the ASCII values 88, 83, and 83 (which represent the characters X, S, and S) into the string 'XSS'.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Create Account|T1136 - Create Account]]
- [[Drive-by Compromise|T1189 - Drive-by Compromise]]
- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]

## Tags

- [[Bypass quotes for string]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


