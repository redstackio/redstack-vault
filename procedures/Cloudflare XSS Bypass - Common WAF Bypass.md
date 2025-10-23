---
id: 97398b5f-8254-4727-a3c8-2de7b3b45b3d
name: Cloudflare XSS Bypass - Common WAF Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.434534+00:00'
updated_at: '2023-04-10T20:21:35.313838+00:00'
tags:
- '[[Cloudflare XSS Bypass - 27th February 2018]]'
- '[[Common WAF Bypass]]'
- '[[Cross Site Scripting]]'
---

# Cloudflare XSS Bypass - Common WAF Bypass

## Summary

This procedure details a technique to bypass Cloudflare's web application firewall (WAF) using a common cross-site scripting (XSS) attack. The attack uses server-side includes injection and a specially crafted payload to bypass the WAF and execute malicious code on the target server. The business v

## Description

# Description

This procedure details a technique to bypass Cloudflare's web application firewall (WAF) using a common cross-site scripting (XSS) attack. The attack uses server-side includes injection and a specially crafted payload to bypass the WAF and execute malicious code on the target server. The business value of this procedure is to test the effectiveness of Cloudflare's WAF and identify potential vulnerabilities that could be exploited by attackers.

 

## Requirements

1. Access to a target server protected by Cloudflare

1. Knowledge of server-side includes injection and cross-site scripting attacks

 

## Defense

1. Implement strict input validation and sanitization to prevent XSS attacks

1. Regularly update and patch the WAF to protect against known vulnerabilities

1. Monitor network traffic for suspicious activity and investigate any anomalies

 

## Objectives

1. Bypass the Cloudflare WAF

1. Execute malicious code on the target server

 

# Instructions

1. The code in the 'data' field is an example of a cross-site scripting (XSS) attack. It exploits a vulnerability in a web application by injecting malicious code into a webpage. When a user clicks on the link, the code executes and can steal sensitive information, modify the webpage, or perform other malicious actions. To prevent XSS attacks, web developers should use input validation, output encoding, and other security measures.

 



**Code**: [[<a href="j&Tab;a&Tab;v&Tab;asc&NewLine;ri&Tab;pt&c]]



> The 'data' field contains HTML code that creates a link with JavaScript code embedded in it. The JavaScript code uses the 'document.domain' property to access the domain of the current webpage. By injecting this code into a vulnerable webpage, an attacker could steal cookies, login credentials, or other sensitive information from the user. Web developers should sanitize user input and encode output to prevent XSS attacks.

## Tags

- [[Cloudflare XSS Bypass - 27th February 2018]]
- [[Common WAF Bypass]]
- [[Cross Site Scripting]]


