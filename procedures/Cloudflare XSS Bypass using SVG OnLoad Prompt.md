---
id: bce9e371-94b7-406b-97c6-3c5eb94ec9db
name: Cloudflare XSS Bypass using SVG OnLoad Prompt
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.327823+00:00'
updated_at: '2023-04-10T20:21:37.076324+00:00'
tags:
- '[[21st April 2020]]'
- '[[Cloudflare XSS Bypasses by [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)]]'
- '[[Common WAF Bypass]]'
- '[[Cross Site Scripting]]'
---

# Cloudflare XSS Bypass using SVG OnLoad Prompt

## Summary

Cloudflare is a popular web application firewall (WAF) used to protect websites from various attacks including cross-site scripting (XSS). However, sometimes attackers can bypass the WAF using different techniques. One such technique is using the SVG OnLoad Prompt. This technique involves injecting

## Description

# Description

Cloudflare is a popular web application firewall (WAF) used to protect websites from various attacks including cross-site scripting (XSS). However, sometimes attackers can bypass the WAF using different techniques. One such technique is using the SVG OnLoad Prompt. This technique involves injecting malicious code into an SVG image that triggers a prompt when the image is loaded. The prompt can then be used to execute arbitrary code on the victim's browser, bypassing the Cloudflare WAF.

From an offensive perspective, this technique can be used to bypass Cloudflare's protection and execute malicious code on the victim's browser. This can lead to various attacks such as stealing sensitive information, installing malware, or taking control of the victim's device.

To prevent this attack, it is important to keep your web application firewall up to date and configure it properly. Additionally, input validation and output encoding can be used to prevent XSS attacks.

 

## Requirements

1. Access to a vulnerable website protected by Cloudflare

1. Knowledge of the SVG OnLoad Prompt technique

 

## Defense

1. Regularly update and configure your web application firewall

1. Implement input validation and output encoding to prevent XSS attacks

1. Educate users on how to identify and avoid phishing attacks

 

## Objectives

1. Bypass Cloudflare's web application firewall

1. Execute arbitrary code on the victim's browser

 

# Instructions

1. Add a prompt to an SVG element's OnLoad event

 



**Code**: [[<svg/OnLoad="`${prompt()}`">]]



> This command adds a prompt to an SVG element's OnLoad event. When the SVG is loaded, the prompt will appear and the user can enter a value. This value can then be used in other parts of the SVG or in the surrounding HTML code.

## Tags

- [[21st April 2020]]
- [[Cloudflare XSS Bypasses by [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)]]
- [[Common WAF Bypass]]
- [[Cross Site Scripting]]


