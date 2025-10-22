---
id: d81ce74b-cea3-4538-bd53-e55acee07a0d
name: Filter Bypass using Null Byte Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.096782+00:00'
updated_at: '2023-04-10T20:21:33.599652+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Virtualization/Sandbox Evasion|T1497 - Virtualization/Sandbox Evasion]]'
sub_techniques:
- '[[System Checks|T1497.001 - System Checks]]'
tags:
- '[[Bypass using UTF-32]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Filter Bypass using Null Byte Injection

## Summary

Null Byte Injection is a technique used to bypass web application filters that sanitize user inputs. By adding a null byte character to the end of a malicious input, it can trick the filter into allowing the input to pass through. This technique is often used in Cross-Site Scripting (XSS) attacks t

## Description

# Description

Null Byte Injection is a technique used to bypass web application filters that sanitize user inputs. By adding a null byte character to the end of a malicious input, it can trick the filter into allowing the input to pass through. This technique is often used in Cross-Site Scripting (XSS) attacks to inject malicious scripts into a website. The technical explanation behind this technique is that null bytes are used to terminate strings in certain programming languages, so when a filter encounters a null byte, it assumes that the string has ended and does not consider any characters after it. The business value of this technique is that it can allow an attacker to steal sensitive information or take control of a victim's account.

## Requirements

1. Access to a web application that uses a filter to sanitize user inputs

1. Knowledge of the filter's sanitization methods

1. Ability to inject null byte characters into user inputs

## Defense

1. Implement input validation techniques that can detect and block null byte characters

1. Use web application firewalls (WAFs) that can detect and block null byte injection attacks

1. Regularly update web application filters to ensure they are up-to-date with the latest security measures

## Objectives

1. Inject malicious scripts into a website

1. Steal sensitive information

1. Take control of a victim's account

# Instructions

1. The Null Byte Injection is a technique used to bypass security measures in applications that parse user input. In this attack, a null byte (%00) is injected into the input data, which tricks the application into interpreting the input string as two separate strings.

**Code**: [[%00%00%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%0]]

> The null byte is used as a string terminator in many programming languages. When an application encounters a null byte in user input, it stops processing the string at that point. In the case of Null Byte Injection, the attacker can use this behavior to their advantage by injecting a null byte into the input string, which can cause the application to interpret the input as two separate strings. This can allow the attacker to bypass security measures such as input validation and execute arbitrary code or access sensitive data.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Virtualization/Sandbox Evasion|T1497 - Virtualization/Sandbox Evasion]]

### Sub-Techniques

- [[System Checks|T1497.001 - System Checks]]

## Tags

- [[Bypass using UTF-32]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
