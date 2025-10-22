---
id: 52b7736f-3754-4a90-9c9d-65de2d451982
name: PHP Object Injection for Arbitrary Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.361022+00:00'
updated_at: '2023-04-06T03:55:59.375764+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[LSASS Driver|T1177 - LSASS Driver]]'
tags:
- '[[Object Injection]]'
- '[[PHP Deserialization]]'
commands:
- '[[ObjectExample]]'
---

# PHP Object Injection for Arbitrary Code Execution

## Summary

PHP Object Injection is a vulnerability that allows an attacker to inject custom objects into an application's code, which can then be executed by the application. This vulnerability can be exploited by sending a specially crafted serialized object to the application. When the application deseriali

## Description

# Description

PHP Object Injection is a vulnerability that allows an attacker to inject custom objects into an application's code, which can then be executed by the application. This vulnerability can be exploited by sending a specially crafted serialized object to the application. When the application deserializes the object, the attacker's code is executed. This can lead to arbitrary code execution, allowing the attacker to take control of the application and potentially the underlying system. In this specific example, the vulnerable code allows an attacker to guess a secret code by manipulating the serialized object.

## Requirements

1. Access to the vulnerable application.

1. Knowledge of the PHP Object Injection vulnerability.

1. Ability to craft a serialized object.

## Defense

1. Validate and sanitize all user input, especially when deserializing objects.

1. Use a whitelist approach when deserializing objects, only allowing known safe classes and rejecting all others.

1. Monitor applications for any attempts to exploit the PHP Object Injection vulnerability.

## Objectives

1. Exploit the PHP Object Injection vulnerability to execute arbitrary code.

1. Guess the secret code by manipulating the serialized object.

# Instructions

1. 

**Code**: [[<?php
class ObjectExample
{
  var $guess;
  var $s]]

> This code deserializes an object from user input and sets a random secret code. If the user's guess matches the secret code, the application prints 'Win'.

2. 

**Code**: [[O:13:"ObjectExample":2:{s:10:"secretCode";N;s:5:"g]]

> This payload is a serialized object that sets the secret code to null and the guess to 2. When the application deserializes this object, it will set the secret code to null and compare the guess to the secret code, which will always be false, preventing the 'Win' message from being printed.

**Command** ([[ObjectExample]]):

```bash
O:13:\"ObjectExample\":2:{s:10:\"secretCode\";N;s:5:\"guess\";R:2;}
```

3. 

**Code**: [[a:2:{s:10:"admin_hash";N;s:4:"hmac";R:2;}]]

> This payload is an array that sets the 'admin_hash' key to null and the 'hmac' key to 2. When the application deserializes this array, it will set the 'admin_hash' key to null and return the value of the 'hmac' key, which is 2. This can be used to manipulate the application's logic and potentially gain unauthorized access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[LSASS Driver|T1177 - LSASS Driver]]

## Commands Used

- [[ObjectExample]]

## Tags

- [[Object Injection]]
- [[PHP Deserialization]]
