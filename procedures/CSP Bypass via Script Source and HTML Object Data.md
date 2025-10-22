---
id: 89a7bd0f-a0c0-4a6a-815a-8b27ede40ef3
name: CSP Bypass via Script Source and HTML Object Data
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.259877+00:00'
updated_at: '2023-04-10T20:21:45.347353+00:00'
tags:
- '[[Bypass CSP by [@akita_zen](https://twitter.com/akita_zen)]]'
- '[[Cross Site Scripting]]'
- '[[CSP Bypass]]'
---

# CSP Bypass via Script Source and HTML Object Data

## Summary

This procedure bypasses Content Security Policy (CSP) by utilizing the CSP Script Source command and HTML Object Data. CSP is a security feature that is implemented in modern browsers to mitigate cross-site scripting (XSS) attacks. It works by allowing website owners to specify which sources of con

## Description

# Description

This procedure bypasses Content Security Policy (CSP) by utilizing the CSP Script Source command and HTML Object Data. CSP is a security feature that is implemented in modern browsers to mitigate cross-site scripting (XSS) attacks. It works by allowing website owners to specify which sources of content are allowed to be loaded on their website. This procedure exploits a misconfiguration in the CSP policy to allow for the execution of malicious scripts.

## Requirements

1. Access to a target website with a misconfigured CSP policy

1. Ability to inject malicious code into the website

## Defense

1. Ensure that the CSP policy is properly configured to only allow trusted sources of content

1. Implement strict input validation and output encoding to prevent injection attacks

1. Regularly review and audit the CSP policy to ensure that it is up-to-date and effective

## Objectives

1. Bypass CSP protection to execute malicious scripts on a target website

1. Gain access to sensitive information on the target website

1. Perform actions on behalf of the victim user

# Instructions

1. Use this command to specify the source of scripts that are allowed to execute on your web page.

**Code**: [[script-src self]]

> The 'script-src' command is a part of Content Security Policy (CSP) that allows you to specify the sources from which the browser can load JavaScript, such as 'self', 'unsafe-inline', 'unsafe-eval', 'https://example.com', etc. In this case, the 'self' keyword indicates that scripts can only be loaded from the same origin as the page itself. This helps to prevent cross-site scripting (XSS) attacks by disallowing the execution of scripts from untrusted sources.

2. The HTML Object Data command is used to embed HTML code into a web page. The 'data' attribute specifies the URL of the data to be displayed. In this case, the data is encoded in base64 format and is displayed as an HTML page.

**Code**: [[<object data="data:text/html;base64,PHNjcmlwdD5hbG]]

> The 'data' attribute can also be used to display other types of data, such as images, videos, or audio files. The 'type' attribute can be used to specify the MIME type of the data. The 'width' and 'height' attributes can be used to specify the dimensions of the object display area.

## Tags

- [[Bypass CSP by [@akita_zen](https://twitter.com/akita_zen)]]
- [[Cross Site Scripting]]
- [[CSP Bypass]]
