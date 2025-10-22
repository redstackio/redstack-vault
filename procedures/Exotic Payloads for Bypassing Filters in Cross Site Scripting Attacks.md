---
id: 307965b1-0091-4162-8eca-8a4e84d46d97
name: Exotic Payloads for Bypassing Filters in Cross Site Scripting Attacks
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.557840+00:00'
updated_at: '2023-04-10T20:21:31.881649+00:00'
tags:
- '[[Bypass parenthesis and semi colon]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Exotic Payloads for Bypassing Filters in Cross Site Scripting Attacks

## Summary

Cross Site Scripting (XSS) attacks involve injecting malicious code into a web page viewed by other users. Filter bypass and exotic payloads are techniques used to evade detection and bypass security measures put in place to prevent XSS attacks. In this specific procedure, we will explore how to by

## Description

# Description

Cross Site Scripting (XSS) attacks involve injecting malicious code into a web page viewed by other users. Filter bypass and exotic payloads are techniques used to evade detection and bypass security measures put in place to prevent XSS attacks. In this specific procedure, we will explore how to bypass filters using exotic payloads, specifically targeting the use of parenthesis and semi-colons. By using these payloads, attackers can evade detection and successfully execute their malicious code, potentially leading to the theft of sensitive data or the takeover of a user's session. The business value of this procedure is to raise awareness of the potential for XSS attacks and the importance of implementing proper security measures to prevent them.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the specific filters in place

1. Ability to craft exotic payloads

## Defense

1. Implement proper input validation and sanitization techniques to prevent XSS attacks

1. Use Content Security Policy (CSP) to restrict the types of content that can be loaded by a web page

1. Regularly update and patch web applications to prevent known vulnerabilities

## Objectives

1. To bypass filters in XSS attacks using exotic payloads

1. To evade detection and successfully execute malicious code

1. To gain access to sensitive data or take over a user's session

# Instructions

1. This command executes malicious code in a web page through script injection.

**Code**: [[// From @garethheyes
<script>onerror=alert;throw 1]]

> The script injection technique allows attackers to inject malicious code into a web page, which can then be executed in the context of the victim's browser. This can be used to steal sensitive information, such as login credentials, or to perform other malicious actions, such as redirecting the victim to a phishing page. The injected code can be triggered by various events, such as loading the page or clicking a button. The code can be obfuscated to evade detection by security tools.

## Tags

- [[Bypass parenthesis and semi colon]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
