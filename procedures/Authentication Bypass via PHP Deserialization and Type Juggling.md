---
id: fb2ee009-be50-4f3c-aeb2-0c38f88583e3
name: Authentication Bypass via PHP Deserialization and Type Juggling
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.337243+00:00'
updated_at: '2023-04-06T03:55:59.351356+00:00'
tags:
- '[[Authentication bypass]]'
- '[[PHP Deserialization]]'
- '[[Type juggling]]'
commands:
- '[[Comparison of boolean and string]]'
---

# Authentication Bypass via PHP Deserialization and Type Juggling

## Summary

This attack leverages a vulnerability in the PHP application code that allows an attacker to bypass authentication. The vulnerability is caused by the insecure deserialization of user input, which can be manipulated to create a specially crafted object that can be used to bypass the authentication 

## Description

# Description

This attack leverages a vulnerability in the PHP application code that allows an attacker to bypass authentication. The vulnerability is caused by the insecure deserialization of user input, which can be manipulated to create a specially crafted object that can be used to bypass the authentication check. In particular, the attacker can use a technique called 'type juggling' to manipulate the values of the serialized object so that they match the expected values of the application. By doing so, the attacker can trick the application into thinking that the authentication check has succeeded, and gain access to sensitive resources or functionality.

From a technical perspective, the attack works by sending a specially crafted serialized object as a cookie to the PHP application. The object contains two fields, 'username' and 'password', both set to the boolean value 'true'. However, because of the way PHP handles type conversions, the 'true' value can be interpreted as a string, and compared to the expected string values of the username and password fields. By carefully crafting the serialized object, the attacker can make the comparison succeed, and bypass the authentication check.

The business value of this attack is that it allows an attacker to gain unauthorized access to sensitive resources or functionality in the application, such as customer data, financial information, or administrative privileges. This can result in financial loss, reputational damage, or legal liability for the affected organization.

## Requirements

1. Access to the vulnerable PHP application

1. Ability to send a specially crafted serialized object as a cookie

## Defense

1. Always validate and sanitize user input, especially when it is used in sensitive operations such as authentication

1. Use a secure serialization format, such as JSON or XML, that does not allow arbitrary code execution or object creation

1. Implement strong authentication controls, such as multi-factor authentication, to reduce the impact of authentication bypass attacks

## Objectives

1. Bypass authentication controls in the PHP application

1. Gain unauthorized access to sensitive resources or functionality

# Instructions

1. This PHP code is vulnerable to authentication bypass via PHP deserialization and type juggling. Specifically, the code deserializes user input from a cookie named 'auth', and checks whether the 'username' and 'password' fields of the resulting object match the expected values. However, because of the way PHP handles type conversions, the 'true' value can be interpreted as a string, and compared to the expected string values of the username and password fields. By carefully crafting the serialized object, an attacker can make the comparison succeed, and bypass the authentication check.

**Code**: [[<?php
$data = unserialize($_COOKIE['auth']);

if (]]

> 

2. This is an example of a serialized object that can be used to bypass authentication in the vulnerable PHP code. The object contains two fields, 'username' and 'password', both set to the boolean value 'true'. However, because of the way PHP handles type conversions, the 'true' value can be interpreted as a string, and compared to the expected string values of the username and password fields. By carefully crafting the serialized object, an attacker can make the comparison succeed, and bypass the authentication check.

**Code**: [[a:2:{s:8:"username";b:1;s:8:"password";b:1;}]]

> 

3. This is an example of a type juggling attack that can be used to bypass authentication in the vulnerable PHP code. The attack works by comparing the boolean value 'true' to a string value, using the '==' operator. Because of the way PHP handles type conversions, the 'true' value can be interpreted as a string, and compared to the expected string values of the username and password fields. By carefully crafting the serialized object, an attacker can make the comparison succeed, and bypass the authentication check.

**Code**: [[true == &quot;str&quot;]]

> 

**Command** ([[Comparison of boolean and string]]):

```bash
true == &quot;str&quot;
```

## Commands Used

- [[Comparison of boolean and string]]

## Tags

- [[Authentication bypass]]
- [[PHP Deserialization]]
- [[Type juggling]]
