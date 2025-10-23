---
id: bf788195-f787-474e-88d0-50848739c777
name: CRLF Injection Phishing Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:56.041291+00:00'
updated_at: '2023-04-10T20:21:24.024267+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Phishing|T1566 - Phishing]]'
sub_techniques:
- '[[Spearphishing Attachment|T1566.001 - Spearphishing Attachment]]'
- '[[Spearphishing Link|T1566.002 - Spearphishing Link]]'
tags:
- '[[Carriage Return Line Feed]]'
- '[[CRLF - Write HTML]]'
---

# CRLF Injection Phishing Attack

## Summary

A CRLF injection attack is a type of phishing attack that involves injecting malicious code into HTTP headers. In this attack, an attacker can inject a CRLF sequence into an HTTP header, which can be used to insert additional headers or modify existing ones. This can be used to inject malicious con

## Description

# Description

A CRLF injection attack is a type of phishing attack that involves injecting malicious code into HTTP headers. In this attack, an attacker can inject a CRLF sequence into an HTTP header, which can be used to insert additional headers or modify existing ones. This can be used to inject malicious content into legitimate websites by modifying the HTTP response header. This attack can be used to steal sensitive information such as login credentials, credit card information, and other personal data. This attack can be carried out using various methods such as social engineering, email phishing, or by exploiting vulnerabilities in web applications.

 

## Requirements

1. Access to a vulnerable web application

1. Ability to inject malicious code into HTTP headers

 

## Defense

1. Implement input validation to prevent CRLF injection attacks

1. Use secure coding practices to prevent vulnerabilities in web applications

1. Train employees on how to identify and avoid phishing attacks

 

## Objectives

1. To inject malicious code into HTTP headers

1. To steal sensitive information such as login credentials and credit card information

1. To exploit vulnerabilities in web applications

 

# Instructions

1. The attacker injects a CRLF sequence into the HTTP header by adding %0D%0A to the header fields. This can be used to inject additional headers or modify existing ones.

 



**Code**: [[http://www.example.net/index.php?lang=en%0D%0ACont]]



> The attacker can use this command to inject malicious code into the HTTP headers of a vulnerable web application. The CRLF sequence is used to insert additional headers or modify existing ones. This can be used to inject malicious content into legitimate websites by modifying the HTTP response header.

2. The attacker injects malicious content into the HTTP response by modifying the HTTP response header. This can be used to steal sensitive information such as login credentials, credit card information, and other personal data.

 



**Code**: [[Set-Cookie:en
Content-Length: 0

HTTP/1.1 200 OK
C]]



> The attacker can use this command to inject malicious content into the HTTP response of a vulnerable web application. By modifying the HTTP response header, the attacker can steal sensitive information such as login credentials, credit card information, and other personal data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Phishing|T1566 - Phishing]]

### Sub-Techniques

- [[Spearphishing Attachment|T1566.001 - Spearphishing Attachment]]
- [[Spearphishing Link|T1566.002 - Spearphishing Link]]

## Tags

- [[Carriage Return Line Feed]]
- [[CRLF - Write HTML]]


