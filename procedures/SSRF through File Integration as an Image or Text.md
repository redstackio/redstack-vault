---
id: 640e44d1-3380-460b-9a01-049bd1f9d831
name: SSRF through File Integration as an Image or Text
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.131525+00:00'
updated_at: '2023-04-10T20:23:57.524023+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF from XSS]]'
- '[[Using an iframe]]'
---

# SSRF through File Integration as an Image or Text

## Summary

This procedure involves exploiting a vulnerability in a web application that allows an attacker to inject a malicious file as an image or text. The malicious file contains an iframe that points to a vulnerable endpoint on a remote server. When the user loads the page, the iframe sends a request to 

## Description

# Description

This procedure involves exploiting a vulnerability in a web application that allows an attacker to inject a malicious file as an image or text. The malicious file contains an iframe that points to a vulnerable endpoint on a remote server. When the user loads the page, the iframe sends a request to the vulnerable endpoint on the remote server, which can result in sensitive data disclosure or remote code execution.

This technique can be used by attackers to gain access to sensitive data or to execute arbitrary code on a remote server. The attacker can use this technique to bypass network security controls, such as firewalls, by using the web application as a proxy to access internal systems.

From a business perspective, this attack can result in data loss or data leakage, which can damage a company's reputation and lead to legal consequences.

 

## Requirements

1. Access to a vulnerable web application

1. Ability to inject a malicious file as an image or text

 

## Defense

1. Implement input validation and sanitization to prevent injection attacks

1. Use a Content Security Policy (CSP) to restrict the sources of content that can be loaded on a page

1. Monitor network traffic for suspicious activity, such as requests to known vulnerable endpoints

 

## Objectives

1. Gain access to sensitive data on a remote server

1. Execute arbitrary code on a remote server

1. Bypass network security controls

 

# Instructions

1. To integrate the content of a file as an image or text, use the 'img' tag in HTML and specify the source of the image as the file path. In case of text, use the 'p' tag or another appropriate tag and write the content of the file within the tag. Make sure to properly sanitize the input and validate the file path to prevent any security vulnerabilities.

 



**Code**: [[<img src="echopwn" onerror="document.write('<ifram]]



> The 'img' tag in HTML is used to display an image on a web page. In this case, we are using it to display the content of a file as an image in a PDF. The 'onerror' attribute is used to execute JavaScript code in case the image fails to load. In this example, we are using it to execute a command that displays the contents of the '/etc/passwd' file. Similarly, we can use other HTML tags to display the content of a file as text in a PDF. However, it is important to properly sanitize the input and validate the file path to prevent any security vulnerabilities.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Network Share Discovery|T1135 - Network Share Discovery]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF from XSS]]
- [[Using an iframe]]


