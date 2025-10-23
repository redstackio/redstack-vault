---
id: 62649cd0-3168-4da7-bf0f-c325cce76306
name: SSRF via URL Scheme File Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.784725+00:00'
updated_at: '2023-04-10T20:24:04.614191+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Protocol Tunneling|T1572 - Protocol Tunneling]]'
tags:
- '[[File]]'
- '[[Server-Side Request Forgery]]'
- '[[SSRF exploitation via URL Scheme]]'
---

# SSRF via URL Scheme File Retrieval

## Summary

This procedure involves exploiting a Server-Side Request Forgery (SSRF) vulnerability via a URL Scheme to retrieve file content. An attacker can manipulate the URL Scheme to point to a file on the targeted server and retrieve its content. This technique is commonly used in exfiltration attacks wher

## Description

# Description

This procedure involves exploiting a Server-Side Request Forgery (SSRF) vulnerability via a URL Scheme to retrieve file content. An attacker can manipulate the URL Scheme to point to a file on the targeted server and retrieve its content. This technique is commonly used in exfiltration attacks where the attacker wants to retrieve sensitive data from the targeted server. Technical details involve crafting a specially crafted URL Scheme and sending it to the server in order to retrieve the desired file content. Business value of this attack lies in the ability to retrieve sensitive data from the targeted server, which can be used for financial gain or competitive advantage.

 

## Requirements

1. Access to a vulnerable server with an SSRF vulnerability

1. Knowledge of URL Scheme manipulation

1. Access to a tool for crafting custom URL Schemes

 

## Defense

1. Implement input validation and sanitization to prevent SSRF vulnerabilities

1. Limit network access from servers to prevent exfiltration of sensitive data

1. Implement network segmentation to limit lateral movement in case of a successful attack

 

## Objectives

1. Retrieve sensitive data from the targeted server

1. Exfiltrate data from the targeted server

 

# Instructions

1. To use this command, the attacker must have access to the server and know the path of the file they want to retrieve. The command can be executed using PowerShell.

 



**Code**: [[file://path/to/file
file:///etc/passwd
file://\/\/]]



> The 'file://' prefix is used to specify that the following string is a file path. The path can be absolute or relative. The 'ssrf.php' script is used to fetch files from the server using Server Side Request Forgery (SSRF). This technique allows an attacker to manipulate the URL of a request sent by the server and trick it into fetching a file from the server's file system. The 'url=file:///etc/passwd' parameter in the URL specifies the file path to be fetched.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Protocol Tunneling|T1572 - Protocol Tunneling]]

## Tags

- [[File]]
- [[Server-Side Request Forgery]]
- [[SSRF exploitation via URL Scheme]]


