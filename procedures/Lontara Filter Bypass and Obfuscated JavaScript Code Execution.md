---
id: 45c691e1-341a-4e64-a03d-59ef322af2f0
name: Lontara Filter Bypass and Obfuscated JavaScript Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.940749+00:00'
updated_at: '2023-04-10T20:21:44.618387+00:00'
tags:
- '[[Bypass using Lontara]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Lontara Filter Bypass and Obfuscated JavaScript Code Execution

## Summary

Lontara is a technique used to bypass filters and execute obfuscated JavaScript code. It involves encoding the payload in a way that the filter does not recognize it as malicious. Once the payload is delivered to the target, the obfuscated code is executed, allowing the attacker to perform various 

## Description

# Description

Lontara is a technique used to bypass filters and execute obfuscated JavaScript code. It involves encoding the payload in a way that the filter does not recognize it as malicious. Once the payload is delivered to the target, the obfuscated code is executed, allowing the attacker to perform various actions such as stealing sensitive information or performing unauthorized actions on behalf of the user. This technique is commonly used in Cross Site Scripting attacks.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the Lontara technique

1. Ability to obfuscate JavaScript code

## Defense

1. Implement input validation to prevent malicious payloads from being delivered

1. Use Content Security Policy (CSP) to restrict the sources of executable scripts

1. Regularly update and patch web application software to prevent known vulnerabilities

## Objectives

1. Execute obfuscated JavaScript code on the target system

1. Bypass filters to deliver the malicious payload

1. Steal sensitive information or perform unauthorized actions on behalf of the user

# Instructions

1. This command executes obfuscated JavaScript code. The code is stored in the 'data' field of the JSON object. To use this command, copy and paste the code into a JavaScript environment.

**Code**: [[ᨆ='',ᨊ=!ᨆ+ᨆ,ᨎ=!ᨊ+ᨆ,ᨂ=ᨆ+{},ᨇ=ᨊ[ᨆ++],ᨋ=ᨊ[ᨏ=ᨆ],ᨃ=++ᨏ+]]

> The code is written in an obfuscated manner to hide its true purpose. It first initializes several variables, including an empty string and an empty object. It then uses these variables to construct a function call, which is executed at the end of the code. The function call takes a string as an argument, which is constructed using various string concatenation operations. The resulting string is then executed as JavaScript code.

## Tags

- [[Bypass using Lontara]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
