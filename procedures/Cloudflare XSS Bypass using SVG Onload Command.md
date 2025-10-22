---
id: 4c52b305-ecbf-4fca-9060-045ba0db71f6
name: Cloudflare XSS Bypass using SVG Onload Command
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.413656+00:00'
updated_at: '2023-04-10T20:21:32.929170+00:00'
tags:
- '[[Cloudflare XSS Bypass - 22nd March 2019 (by @RakeshMane10)]]'
- '[[Common WAF Bypass]]'
- '[[Cross Site Scripting]]'
---

# Cloudflare XSS Bypass using SVG Onload Command

## Summary

This technique leverages an SVG onload command to bypass Cloudflare's XSS protection. The technique was discovered on March 22nd, 2019 by @RakeshMane10. An attacker can use this technique to inject malicious code into a vulnerable website, bypassing any WAF protection in place. By using the SVG onl

## Description

# Description

This technique leverages an SVG onload command to bypass Cloudflare's XSS protection. The technique was discovered on March 22nd, 2019 by @RakeshMane10. An attacker can use this technique to inject malicious code into a vulnerable website, bypassing any WAF protection in place. By using the SVG onload command, the attacker can execute JavaScript code without triggering any alarms. This technique can be used to steal sensitive information, perform unauthorized actions, or gain access to restricted areas of the website.

From a technical perspective, the SVG onload command allows attackers to inject JavaScript code into an SVG image, which is then executed by the browser. This technique works by encoding the malicious code in base64 and including it as a parameter in the SVG image. When the image is loaded, the browser decodes the parameter and executes the code. This technique is effective because it bypasses Cloudflare's XSS protection, which is designed to detect and block malicious JavaScript code.

From a business perspective, this technique can have serious consequences. An attacker can use this technique to steal sensitive information, such as login credentials, credit card numbers, or personal data. This can result in financial loss, reputation damage, and legal liabilities for the affected organization. By using this technique, an attacker can also perform unauthorized actions on behalf of the user, such as transferring funds, changing settings, or deleting data.

## Requirements

1. Access to a vulnerable website

1. Knowledge of the SVG onload command

1. Ability to encode JavaScript code in base64

## Defense

1. Implement strict input validation and output encoding to prevent XSS attacks

1. Use a modern WAF that can detect and block advanced XSS techniques

1. Regularly update and patch web applications to prevent known vulnerabilities

## Objectives

1. Inject malicious code into a vulnerable website

1. Bypass Cloudflare's XSS protection

1. Execute JavaScript code without triggering alarms

1. Steal sensitive information

1. Perform unauthorized actions

1. Gain access to restricted areas of the website

# Instructions

1. The SVG Onload command is a type of Cross-Site Scripting (XSS) attack that injects malicious code into an SVG image. When the image is loaded, the code executes and can perform various actions, such as stealing user data or taking control of the user's session.

The 'onload' attribute in SVG specifies a script to run when the image is loaded. In this command, the script is injected with the 'svg/onload' prefix. The '&#97&#108&#101&#114&#00116&#40&#41&#x2f&#x2f' code is JavaScript that is executed when the image is loaded. This code can be replaced with any other malicious script that the attacker wishes to execute.

## Tags

- [[Cloudflare XSS Bypass - 22nd March 2019 (by @RakeshMane10)]]
- [[Common WAF Bypass]]
- [[Cross Site Scripting]]
