---
id: bf9115af-5635-4c82-8bcc-1e66a7739115
name: Server Side Template Injection with Pebble - Basic Injection using Convert String
  to Uppercase
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.121600+00:00'
updated_at: '2023-04-10T20:23:45.937235+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Pebble]]'
- '[[Pebble - Basic injection]]'
- '[[Server Side Template Injection]]'
---

# Server Side Template Injection with Pebble - Basic Injection using Convert String to Uppercase

## Summary

Server Side Template Injection (SSTI) is a type of injection attack that allows an attacker to inject malicious input into a template engine, which can lead to arbitrary code execution on the server. Pebble is a popular Java-based template engine that supports SSTI. This procedure demonstrates a ba

## Description

# Description

Server Side Template Injection (SSTI) is a type of injection attack that allows an attacker to inject malicious input into a template engine, which can lead to arbitrary code execution on the server. Pebble is a popular Java-based template engine that supports SSTI. This procedure demonstrates a basic SSTI attack using Pebble, where the attacker uses the 'Convert String to Uppercase' command to execute arbitrary code on the server. 

The technical explanation of this procedure involves the attacker exploiting a vulnerability in the Pebble template engine by injecting a payload that executes arbitrary code. The attacker can then use the 'Convert String to Uppercase' command to execute the payload and gain control of the server. The business value of this procedure is that it demonstrates the importance of securing web applications that use template engines, as SSTI attacks can lead to data theft, server compromise, and reputational damage.

## Requirements

1. Access to a vulnerable web application that uses the Pebble template engine

## Defense

1. Implement input validation and sanitization to prevent SSTI attacks

1. Use a web application firewall (WAF) to detect and block SSTI attacks

1. Regularly update the template engine and associated libraries to patch known vulnerabilities

## Objectives

1. Execute arbitrary code on the server

1. Gain control of the server

# Instructions

1. To convert a string to uppercase in Java, you can use the `toUpperCase()` method of the `String` class. This method returns a new string with all the characters in uppercase.

**Code**: [[{{ SOMESTRING.TOUPPERCASE() }}]]

> The `toUpperCase()` method takes no arguments and returns a new string with all the characters in uppercase. For example, if `someString` is a string variable, you can convert it to uppercase using the following code:

```
String upperCaseString = someString.toUpperCase();
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Pebble]]
- [[Pebble - Basic injection]]
- [[Server Side Template Injection]]
