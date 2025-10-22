---
id: 60d53005-6bc4-4348-942a-68619c4f63b9
name: Filter Bypass with Obfuscated JavaScript Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.921723+00:00'
updated_at: '2023-04-10T20:21:32.228447+00:00'
tags:
- '[[Bypass using Cuneiform]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Filter Bypass with Obfuscated JavaScript Code Execution

## Summary

This procedure enables an attacker to bypass filters and execute obfuscated JavaScript code on a victim's browser through a Cross Site Scripting vulnerability. By using the Cuneiform encoding method, the attacker can bypass filters that are designed to detect and block malicious payloads. Once the 

## Description

# Description

This procedure enables an attacker to bypass filters and execute obfuscated JavaScript code on a victim's browser through a Cross Site Scripting vulnerability. By using the Cuneiform encoding method, the attacker can bypass filters that are designed to detect and block malicious payloads. Once the code is executed, the attacker gains access to sensitive information, such as session cookies, which can be used to impersonate the victim and perform unauthorized actions on their behalf. This procedure is commonly used in web application attacks and can lead to significant financial and reputational damage for the victim.

## Requirements

1. Access to a vulnerable web application with a Cross Site Scripting vulnerability

1. Knowledge of the Cuneiform encoding method

1. A web browser to execute the payload

## Defense

1. Implement input validation and output encoding to prevent Cross Site Scripting vulnerabilities

1. Use Content Security Policy (CSP) to limit the types of content that can be executed on a web page

1. Regularly monitor web application logs for suspicious activity

## Objectives

1. Execute obfuscated JavaScript code on a victim's browser

1. Bypass filters that are designed to detect and block malicious payloads

1. Steal sensitive information, such as session cookies

# Instructions

1. This code is an obfuscated JavaScript code that can execute arbitrary JavaScript code. To use this code, replace the empty string ('') with the code you want to execute. Then, run the code in the browser console.

**Code**: [[𒀀='',𒉺=!𒀀+𒀀,𒀃=!𒉺+𒀀,𒇺=𒀀+{},𒌐=𒉺[𒀀++],
𒀟=𒉺[𒈫=𒀀],𒀆=++𒈫]]

> The code uses a combination of Unicode characters and JavaScript built-in objects to make it difficult to read and understand. The code creates several variables and assigns them values that are used to execute the final code. The final code is constructed by concatenating these variables and using them as function calls to execute the code. This technique is used to hide the actual code being executed.

## Tags

- [[Bypass using Cuneiform]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
