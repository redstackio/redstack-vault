---
id: 70de4022-073a-4cb0-8e66-1fe66374d7ca
name: Server Side Template Injection with Groovy - Basic Injection - Multiplication
  Result
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.106784+00:00'
updated_at: '2023-04-10T20:23:47.778364+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Groovy]]'
- '[[Groovy - Basic injection]]'
- '[[Server Side Template Injection]]'
---

# Server Side Template Injection with Groovy - Basic Injection - Multiplication Result

## Summary

Server Side Template Injection is a vulnerability that allows an attacker to inject malicious code into a template engine. In this case, we are using Groovy as the template engine. Groovy is a popular scripting language that is used to create dynamic web pages. By injecting malicious code into a Gr

## Description

# Description

Server Side Template Injection is a vulnerability that allows an attacker to inject malicious code into a template engine. In this case, we are using Groovy as the template engine. Groovy is a popular scripting language that is used to create dynamic web pages. By injecting malicious code into a Groovy template, an attacker can execute arbitrary commands on the server. In this specific injection, we are multiplying two numbers together and returning the result.

This technique can be used by an attacker to gain access to sensitive data, execute malicious code, or take control of the server. From a business perspective, this can lead to data theft, financial loss, and reputational damage.

 

## Requirements

1. Access to a web application that uses Groovy as its template engine

 

## Defense

1. Ensure that all input to the application is properly sanitized to prevent injection attacks

1. Use a web application firewall to detect and block injection attacks

1. Regularly monitor logs for suspicious activity

 

## Objectives

1. Execute arbitrary commands on the server

1. Gain access to sensitive data

1. Take control of the server

 

# Instructions

1. Multiply two numbers together

 



**Code**: [[81]]



> This command takes two numerical arguments and multiplies them together to return their product.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Groovy]]
- [[Groovy - Basic injection]]
- [[Server Side Template Injection]]


