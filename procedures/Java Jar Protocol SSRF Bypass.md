---
id: 700c5c07-42f5-41c1-8c33-b6f9d2447f9d
name: Java Jar Protocol SSRF Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.751967+00:00'
updated_at: '2023-04-10T20:23:55.812605+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypassing using jar protocol (java only)]]'
- '[[Server-Side Request Forgery]]'
commands:
- '[[Jar URLs]]'
- '[[Jar URLs]]'
- '[[Jar URLs]]'
- '[[Jar URLs]]'
---

# Java Jar Protocol SSRF Bypass

## Summary

The Java Jar Protocol SSRF Bypass technique is used to bypass filters in order to exploit server-side request forgery vulnerabilities in Java applications. This technique involves using the jar protocol to make requests to internal systems that are otherwise inaccessible. By using this method, an a

## Description

# Description

The Java Jar Protocol SSRF Bypass technique is used to bypass filters in order to exploit server-side request forgery vulnerabilities in Java applications. This technique involves using the jar protocol to make requests to internal systems that are otherwise inaccessible. By using this method, an attacker can access sensitive data or services that are not intended to be exposed to external users. This technique can be used to pivot through a network and gain access to additional systems.

To execute this technique, an attacker needs to identify a server-side request forgery vulnerability in a Java application. Once identified, the attacker can use the jar protocol to bypass any filters that are in place and make requests to internal systems. This technique can be used to access sensitive data or services, such as databases or internal APIs.

The business value of this technique is that it allows an attacker to gain access to sensitive data or services that are not intended to be exposed to external users. This can lead to data theft, data manipulation, or other malicious activities.

 

## Requirements

1. Access to a server-side request forgery vulnerability in a Java application

 

## Defense

1. Implement input validation to prevent server-side request forgery vulnerabilities

1. Restrict network access to internal systems

1. Implement access controls to limit access to sensitive data or services

 

## Objectives

1. Exploit server-side request forgery vulnerabilities in Java applications

1. Access sensitive data or services that are not intended to be exposed to external users

1. Pivot through a network and gain access to additional systems

 

# Instructions

1. The Blind SSRF command is used to test for Server Side Request Forgery vulnerabilities. It works by sending requests to a specified URL and checking the responses for any signs of SSRF. To use this command, specify the target URL in the data field.

 



**Code**: [[jar:scheme://domain/path!/ 
jar:http://127.0.0.1!/]]



> The data field should contain the target URL that you want to test for SSRF vulnerabilities. The URL should be in the format of a jar file URL that includes a scheme, domain, and path. Multiple URLs can be specified by separating them with a new line character. This command can be used in a Powershell environment.



**Command** ([[Jar URLs]]):

```bash
jar:scheme://domain/path!/
```





**Command** ([[Jar URLs]]):

```bash
jar:http://127.0.0.1!/
```





**Command** ([[Jar URLs]]):

```bash
jar:https://127.0.0.1!/
```





**Command** ([[Jar URLs]]):

```bash
jar:ftp://127.0.0.1!/
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Jar URLs]]
- [[Jar URLs]]
- [[Jar URLs]]
- [[Jar URLs]]

## Tags

- [[Bypassing filters]]
- [[Bypassing using jar protocol (java only)]]
- [[Server-Side Request Forgery]]


