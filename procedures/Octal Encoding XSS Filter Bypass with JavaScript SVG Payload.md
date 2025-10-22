---
id: 1a7f8950-c0a3-4d69-b586-c5b34b3d052b
name: Octal Encoding XSS Filter Bypass with JavaScript SVG Payload
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.983252+00:00'
updated_at: '2023-04-10T20:21:33.276870+00:00'
tags:
- '[[Bypass using Octal encoding]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Octal Encoding XSS Filter Bypass with JavaScript SVG Payload

## Summary

This procedure is a technique for bypassing Cross Site Scripting (XSS) filters using octal encoding and a JavaScript SVG payload. The attack involves encoding the malicious script in octal format to bypass input validation filters. The payload is then delivered using an SVG image, which can be embe

## Description

# Description

This procedure is a technique for bypassing Cross Site Scripting (XSS) filters using octal encoding and a JavaScript SVG payload. The attack involves encoding the malicious script in octal format to bypass input validation filters. The payload is then delivered using an SVG image, which can be embedded in a webpage. When the user visits the webpage, the script is executed, allowing the attacker to steal sensitive information such as cookies, passwords, and session tokens. This technique is particularly effective against filters that only check for ASCII characters and do not properly handle Unicode or other character encodings.

Technical: The attacker crafts a malicious payload using JavaScript code that is then encoded in octal format. This encoding converts the script into a series of numbers that can be interpreted by the browser as JavaScript code. The payload is then delivered using an SVG image, which is embedded in a webpage. When the user visits the webpage, the SVG image is loaded and the JavaScript code is executed, allowing the attacker to steal sensitive information.

Business Value: This technique can be used by attackers to steal sensitive information such as cookies, passwords, and session tokens. This information can then be used to gain unauthorized access to a victim's accounts and steal sensitive data. This can have serious consequences for individuals and organizations, including financial loss, reputational damage, and legal liability.

## Requirements

1. Access to a vulnerable webpage with an XSS filter that only checks for ASCII characters

1. Ability to craft a malicious JavaScript payload and encode it in octal format

1. Ability to deliver the payload using an SVG image

## Defense

1. Implement input validation filters that properly handle Unicode and other character encodings

1. Use Content Security Policy (CSP) to restrict the types of content that can be loaded on a webpage

1. Educate users about the risks of clicking on unknown links or visiting untrusted websites

## Objectives

1. Bypass XSS filters and execute malicious JavaScript code on a victim's browser

1. Steal sensitive information such as cookies, passwords, and session tokens

# Instructions

1. The JavaScript SVG command is used to execute a JavaScript payload in an SVG object. The payload can be any valid JavaScript code that is executed when the SVG object is loaded.

**Code**: [[javascript:'<svg onload=alert(1)>']]

> The 'data' field should contain the JavaScript payload that is to be executed when the SVG object is loaded. This can be used to perform various types of attacks, including XSS and CSRF attacks.

## Tags

- [[Bypass using Octal encoding]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
