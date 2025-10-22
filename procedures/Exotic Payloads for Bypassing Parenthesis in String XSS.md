---
id: 199d9217-3457-4981-9dad-3fdfe1b117d7
name: Exotic Payloads for Bypassing Parenthesis in String XSS
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.539212+00:00'
updated_at: '2023-04-10T20:21:49.873832+00:00'
tags:
- '[[Bypass parenthesis for string]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Exotic Payloads for Bypassing Parenthesis in String XSS

## Summary

Exotic payloads can be used to bypass filters and execute malicious scripts in a web application. In this case, we are using exotic payloads to bypass parenthesis for string XSS attacks. This technique can be used to inject scripts into a vulnerable web page and steal sensitive information, such as

## Description

# Description

Exotic payloads can be used to bypass filters and execute malicious scripts in a web application. In this case, we are using exotic payloads to bypass parenthesis for string XSS attacks. This technique can be used to inject scripts into a vulnerable web page and steal sensitive information, such as login credentials or personal data. Technical explanation: An attacker can use exotic payloads to bypass filters that are designed to prevent XSS attacks. By using a combination of characters, such as brackets and quotes, the attacker can inject malicious scripts into the web page. Business value: By exploiting XSS vulnerabilities, attackers can gain access to sensitive data and compromise the security of a web application.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of exotic payloads and XSS attacks

## Defense

1. Implement input validation and output encoding to prevent XSS attacks

1. Regularly scan web applications for vulnerabilities and apply patches as needed

1. Train employees on how to identify and report suspicious activity on web applications

## Objectives

1. Inject malicious scripts into a vulnerable web page

1. Steal sensitive information, such as login credentials or personal data

# Instructions

1. This command executes two commands, 'alert' and 'setTimeout'.

The 'alert' command will display a message box with the text '1'.

The 'setTimeout' command will execute the 'alert(document.domain)' command after a specified amount of time has elapsed. In this case, the command will execute immediately because the time parameter is not specified.

**Code**: [[alert`1`
setTimeout`alert\u0028document.domain\u00]]

> The 'alert' command is used to display a message box with a specified message.

The 'setTimeout' command is used to execute a specified command after a specified amount of time has elapsed. The first argument is the command to execute, and the second argument is the time in milliseconds to wait before executing the command. If the time argument is not specified, the command will execute immediately.

In this case, the 'alert(document.domain)' command will display a message box with the current domain name of the webpage.

## Tags

- [[Bypass parenthesis for string]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
