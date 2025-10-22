---
id: a1b4c9e3-ec22-44ee-a061-64bb965eda7d
name: CRLF Filter Bypass with UTF-8 Encoding
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:56.072472+00:00'
updated_at: '2023-04-10T20:21:24.372301+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Data Obfuscation|T1001 - Data Obfuscation]]'
tags:
- '[[Carriage Return Line Feed]]'
- '[[CRLF - Filter Bypass]]'
---

# CRLF Filter Bypass with UTF-8 Encoding

## Summary

This procedure utilizes CRLF injection with UTF-8 encoding to bypass filters and inject malicious code into a vulnerable system. By encoding the payload with UTF-8, it is possible to bypass filters that are not capable of detecting non-ASCII characters. This technique can be used to perform a wide 

## Description

# Description

This procedure utilizes CRLF injection with UTF-8 encoding to bypass filters and inject malicious code into a vulnerable system. By encoding the payload with UTF-8, it is possible to bypass filters that are not capable of detecting non-ASCII characters. This technique can be used to perform a wide range of attacks, including cross-site scripting (XSS) and SQL injection.

## Requirements

1. Access to a vulnerable system

1. Knowledge of CRLF injection and UTF-8 encoding

1. Tools for encoding the payload

## Defense

1. Implement input validation and sanitization to prevent CRLF injection attacks

1. Use web application firewalls (WAFs) to detect and block CRLF injection attempts

1. Implement strict content security policies (CSPs) to prevent the execution of malicious scripts

## Objectives

1. Bypass filters and inject malicious code into a vulnerable system

1. Perform cross-site scripting (XSS) and SQL injection attacks

# Instructions

1. Inject the encoded payload into a vulnerable system using CRLF injection

**Code**: [[%E5%98%8A%E5%98%8Dcontent-type:text/html%E5%98%8A%]]

> This command injects a payload that is encoded with UTF-8 and contains a script that will execute an alert window with the inner HTML of the page. The payload is injected using CRLF injection by adding the encoded payload between two CRLF sequences.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Data Obfuscation|T1001 - Data Obfuscation]]

## Tags

- [[Carriage Return Line Feed]]
- [[CRLF - Filter Bypass]]
