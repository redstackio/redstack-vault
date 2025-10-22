---
id: bc98bb38-9232-450a-ae57-6b47fa871ca6
name: Filter Bypass using SVG onload alert command
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.805108+00:00'
updated_at: '2023-04-10T20:21:44.266736+00:00'
tags:
- '[[Bypass ">" using nothing]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Filter Bypass using SVG onload alert command

## Summary

This procedure is designed to bypass input filters that are looking for the ">" character. By using an SVG onload alert command, an attacker can execute a cross-site scripting (XSS) attack. This technique can be used to steal sensitive information such as cookies, login credentials, or other person

## Description

# Description

This procedure is designed to bypass input filters that are looking for the ">" character. By using an SVG onload alert command, an attacker can execute a cross-site scripting (XSS) attack. This technique can be used to steal sensitive information such as cookies, login credentials, or other personal data. The business value of this technique is that it allows an attacker to gain unauthorized access to sensitive information, which can lead to financial loss, reputational damage, and legal repercussions.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the input filter being used

1. Ability to inject an SVG onload alert command

## Defense

1. Implement input filters that are capable of detecting and blocking SVG onload alert commands

1. Regularly scan web applications for vulnerabilities and patch them as soon as possible

1. Educate users on the dangers of XSS attacks and how to avoid them

## Objectives

1. To execute a successful XSS attack

1. To bypass input filters that are looking for the ">" character

1. To steal sensitive information such as cookies, login credentials, or other personal data

# Instructions

1. This command is used to execute a JavaScript alert command when an SVG image loads. The command takes advantage of a vulnerability in certain browsers that allow for code injection through the onload attribute of an SVG tag. By injecting JavaScript code into the SVG tag, an attacker can execute arbitrary code on the victim's browser.

**Code**: [[<svg onload=alert(1)//]]

> The 'onload' attribute is used to execute a JavaScript function when an SVG image has finished loading. In this case, the function being executed is an alert command that displays a pop-up message with the text '1'. The double forward slashes ('//') at the end of the command are used to comment out any remaining code and prevent errors. This command should not be used for any legitimate purpose and is only intended for malicious attacks.

## Tags

- [[Bypass ">" using nothing]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
