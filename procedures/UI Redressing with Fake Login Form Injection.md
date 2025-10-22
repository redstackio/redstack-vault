---
id: 35d69678-213a-405d-9429-40052a532069
name: UI Redressing with Fake Login Form Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.702455+00:00'
updated_at: '2023-04-10T20:21:29.546794+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Phishing|T1566 - Phishing]]'
- '[[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]'
sub_techniques:
- '[[Spearphishing Attachment|T1566.001 - Spearphishing Attachment]]'
tags:
- '[[Cross Site Scripting]]'
- '[[Exploit code or POC]]'
- '[[UI redressing]]'
---

# UI Redressing with Fake Login Form Injection

## Summary

UI Redressing with Fake Login Form Injection is a technique used in phishing attacks to steal user credentials. The attacker injects a fake login form into a legitimate website, which is designed to look like the original login form. When the user enters their credentials, they are sent to the atta

## Description

# Description

UI Redressing with Fake Login Form Injection is a technique used in phishing attacks to steal user credentials. The attacker injects a fake login form into a legitimate website, which is designed to look like the original login form. When the user enters their credentials, they are sent to the attacker's server instead of the legitimate website. This technique is usually used in conjunction with cross-site scripting (XSS) attacks.

From a technical perspective, the attacker injects a script into a vulnerable website that loads a fake login form from the attacker's server. The script is usually injected through a vulnerable parameter in the URL or through a form field. The fake login form is designed to look like the original login form, so the user is not suspicious. When the user enters their credentials, the script sends them to the attacker's server.

The business value of this attack is that it allows an attacker to gain access to sensitive information, such as usernames and passwords. This information can be used for further attacks, such as spear-phishing or credential stuffing.

## Requirements

1. Vulnerable website with a cross-site scripting (XSS) vulnerability

## Defense

1. Implement input validation and sanitization to prevent XSS attacks

1. Use multi-factor authentication to prevent credential theft

1. Educate users on how to identify and avoid phishing attacks

## Objectives

1. Steal user credentials

1. Gain access to sensitive information

# Instructions

1. Inject the provided payload into the vulnerable input field to display a fake login form.

**Code**: [[<script>
history.replaceState(null, null, '../../.]]

> This command demonstrates the ability to exploit a Cross-Site Scripting (XSS) vulnerability in order to inject malicious code into a web page. The provided payload is designed to replace the existing content of the page with a fake login form, which can be used to steal user credentials. The attacker would typically send a link to the victim that contains the malicious payload, and if the victim clicks on the link, the payload would execute in their browser. To prevent this type of attack, web developers should ensure that user input is properly sanitized and validated before being displayed on a web page.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Phishing|T1566 - Phishing]]
- [[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]

### Sub-Techniques

- [[Spearphishing Attachment|T1566.001 - Spearphishing Attachment]]

## Tags

- [[Cross Site Scripting]]
- [[Exploit code or POC]]
- [[UI redressing]]
