---
id: d24ad39f-ec51-46a8-b9e3-67ee3eb5b0de
name: Netdoc SSRF via URL Scheme
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.999934+00:00'
updated_at: '2023-04-10T20:23:56.219526+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Data from Information Repositories|T1213 - Data from Information Repositories]]'
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[Netdoc]]'
- '[[Server-Side Request Forgery]]'
- '[[SSRF exploitation via URL Scheme]]'
---

# Netdoc SSRF via URL Scheme

## Summary

Netdoc is a web application that allows users to store and share documents. It is vulnerable to Server-Side Request Forgery (SSRF) attacks via URL Scheme. An attacker can exploit this vulnerability by sending a specially crafted request to the server, which will then make a request to a third-party

## Description

# Description

Netdoc is a web application that allows users to store and share documents. It is vulnerable to Server-Side Request Forgery (SSRF) attacks via URL Scheme. An attacker can exploit this vulnerability by sending a specially crafted request to the server, which will then make a request to a third-party server on behalf of the attacker. This can be used to access sensitive information or to perform actions on the third-party server that the attacker is not authorized to do.

To exploit this vulnerability, the attacker needs to craft a request that includes a URL Scheme that points to the third-party server. This can be done by using the SSRF Wrapper command.

Business Value: An attacker could use this vulnerability to steal sensitive information or perform unauthorized actions on a third-party server, potentially causing reputational damage and financial loss.

## Requirements

1. Access to the vulnerable Netdoc web application

1. Ability to craft a specially crafted request with a URL Scheme

## Defense

1. Implement input validation and sanitization to prevent SSRF attacks

1. Use a whitelist of allowed URL Schemes to limit the potential attack surface

1. Monitor network traffic for unusual activity and investigate any suspicious requests

## Objectives

1. Access sensitive information on a third-party server

1. Perform unauthorized actions on a third-party server

# Instructions

1. This command is used to wrap Java payloads when they are struggling with "\n" and "\r" characters. It is specifically designed for Server-Side Request Forgery (SSRF) attacks. The command takes in a URL as an argument and returns the contents of the specified URL.

**Code**: [[ssrf.php?url=netdoc:///etc/passwd]]

> The command works by wrapping the Java payload in a way that it can bypass filters that block certain characters such as "\n" and "\r". This allows the payload to be executed successfully and retrieve the contents of the specified URL. The "ssrf.php" file is used as a proxy to bypass any filters that may be in place. It is important to note that this command should only be used for ethical hacking and penetration testing purposes with proper authorization and consent.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Data from Information Repositories|T1213 - Data from Information Repositories]]
- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Tags

- [[Netdoc]]
- [[Server-Side Request Forgery]]
- [[SSRF exploitation via URL Scheme]]
