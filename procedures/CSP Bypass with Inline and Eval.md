---
id: 5d78d277-bf40-4e1e-81a4-4fe2590c8be7
name: CSP Bypass with Inline and Eval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.240987+00:00'
updated_at: '2023-04-10T20:21:38.838951+00:00'
tags:
- '[[Bypass CSP by [Rhynorater](https://gist.github.com/Rhynorater/311cf3981fda8303d65c27316e69209f)]]'
- '[[Cross Site Scripting]]'
- '[[CSP Bypass]]'
---

# CSP Bypass with Inline and Eval

## Summary

CSP (Content Security Policy) is a security feature that prevents the execution of inline scripts and the use of eval functions in web applications. However, attackers can bypass CSP protections by using inline scripts and eval functions. This technique allows attackers to execute their own malicio

## Description

# Description

CSP (Content Security Policy) is a security feature that prevents the execution of inline scripts and the use of eval functions in web applications. However, attackers can bypass CSP protections by using inline scripts and eval functions. This technique allows attackers to execute their own malicious code on the victim's browser, leading to various attacks such as stealing sensitive information, session hijacking, and more. This procedure provides steps to bypass CSP using inline scripts and eval functions.

Technical Explanation: CSP is a security feature that is implemented on web applications to prevent the execution of malicious scripts. CSP enforces the use of only trusted sources for scripts, such as external files or scripts that are embedded within HTML tags. However, attackers can bypass CSP by using inline scripts and eval functions. Inline scripts are scripts that are embedded within HTML tags, while eval functions allow the execution of arbitrary code. By using these techniques, attackers can execute their own malicious code on the victim's browser, leading to various attacks.

Business Value: By bypassing CSP, attackers can execute their own malicious code on the victim's browser, leading to various attacks such as stealing sensitive information, session hijacking, and more. This can result in financial loss, loss of reputation, and legal actions against the affected organization.

## Requirements

1. Access to a vulnerable web application with CSP protections enabled

1. Knowledge of inline scripts and eval functions

## Defense

1. Implement strict CSP policies that do not allow the use of inline scripts or eval functions

1. Regularly update and patch web applications to prevent vulnerabilities

1. Implement web application firewalls (WAFs) that can detect and block malicious requests

## Objectives

1. Bypass CSP protections using inline scripts and eval functions

1. Execute malicious code on the victim's browser

# Instructions

1. This command is used to bypass CSP (Content Security Policy) using inline and eval. The command creates an iframe element and sets its source to the first CSS file it finds on the page. It then appends the iframe to the document body. Next, it creates a script element and sets its source to a malicious script hosted on xss.ht. Finally, it waits for one second and appends the script to the iframe's head element. This allows the malicious script to bypass CSP and execute.

**Code**: [[// CSP Bypass with Inline and Eval
d=document;f=d.]]

> The command takes advantage of the fact that if an inline script is executed within an iframe, it is subject to the iframe's CSP instead of the parent document's CSP. By creating an iframe and appending it to the document body, the command can execute inline scripts within the iframe that would otherwise be blocked by the parent document's CSP. The command also uses eval to execute the malicious script within the iframe, which is allowed by the iframe's CSP.

## Tags

- [[Bypass CSP by [Rhynorater](https://gist.github.com/Rhynorater/311cf3981fda8303d65c27316e69209f)]]
- [[Cross Site Scripting]]
- [[CSP Bypass]]
