---
id: d71dc723-5859-4f93-b19e-f9b823d914ce
name: XSS Payload Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.802924+00:00'
updated_at: '2023-04-10T20:21:51.955719+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Common Payloads]]'
- '[[Cross Site Scripting]]'
- '[[XSS in HTML/Applications]]'
---

# XSS Payload Injection

## Summary

Cross-Site Scripting (XSS) is a web application vulnerability that allows an attacker to inject malicious code into a web page viewed by other users. This can result in the attacker stealing sensitive information, such as login credentials, or executing arbitrary code on the victim's machine. Commo

## Description

# Description

Cross-Site Scripting (XSS) is a web application vulnerability that allows an attacker to inject malicious code into a web page viewed by other users. This can result in the attacker stealing sensitive information, such as login credentials, or executing arbitrary code on the victim's machine. Common payloads for XSS attacks include <script>alert('XSS')</script> and <img src='javascript:alert('XSS')'>. This technique is commonly used in initial access and execution phases of an attack. From a technical perspective, XSS occurs when an application takes user supplied data and sends it to a web browser without proper validation or escaping. From a business perspective, XSS attacks can result in loss of customer trust, data breaches, and financial loss.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of XSS payloads

## Defense

1. Sanitize user input on the server side to prevent XSS attacks

1. Use Content Security Policy (CSP) to restrict the sources of content that can be loaded on a web page

1. Educate users on how to identify and avoid malicious web pages

## Objectives

1. Injecting malicious code into a web page viewed by other users

1. Stealing sensitive information, such as login credentials

1. Executing arbitrary code on the victim's machine

# Instructions

1. Fill in the details for multiple commands, instruction fields, and explain the arguments of the command in detail.

**Code**: [[// Basic payload
<script>alert('XSS')</script>
<sc]]

> This JSON object contains a list of Cross-Site Scripting (XSS) payloads that can be used to test web applications. The payloads are categorized into basic, image, SVG, and div payloads. Each payload is designed to exploit a vulnerability in the web application by injecting malicious code into the page. The payloads include various forms of alert messages that can be customized to suit the attacker's needs. The payloads can be used to test the security of a web application and to identify vulnerabilities that could be exploited by an attacker.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Common Payloads]]
- [[Cross Site Scripting]]
- [[XSS in HTML/Applications]]
