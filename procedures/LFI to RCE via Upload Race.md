---
id: b7bbe4f4-0d1b-48e2-8adc-48b1d712a563
name: LFI to RCE via Upload Race
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.508591+00:00'
updated_at: '2023-04-10T20:22:16.292488+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[File Inclusion]]'
- '[[LFI to RCE via upload (race)]]'
---

# LFI to RCE via Upload Race

## Summary

The LFI to RCE via Upload Race technique is used to exploit a race condition vulnerability in the file upload functionality of a web application. This technique can be used to upload a PHP shell and execute arbitrary code on the server. The attack involves uploading a PHP shell in a loop and simult

## Description

# Description

The LFI to RCE via Upload Race technique is used to exploit a race condition vulnerability in the file upload functionality of a web application. This technique can be used to upload a PHP shell and execute arbitrary code on the server. The attack involves uploading a PHP shell in a loop and simultaneously requesting the inclusion of the uploaded file using Local File Inclusion (LFI) vulnerabilities. Once the file is included, the attacker can execute arbitrary commands on the server.

## Requirements

1. Access to a web application with a file upload functionality

1. Knowledge of LFI vulnerabilities

## Defense

1. Implement proper input validation and sanitization for file uploads

1. Use a Content Security Policy (CSP) to restrict the sources of executable scripts

1. Implement proper access controls to prevent unauthorized access to sensitive files and directories

1. Monitor the server for unusual activity and investigate any suspicious requests or behavior

1. Use a Web Application Firewall (WAF) to detect and block attacks

## Objectives

1. Upload a PHP shell to the server

1. Execute arbitrary commands on the server

# Instructions

1. Save the script as a .py file and run it using Python 3.

**Code**: [[import itertools
import requests
import sys

print]]

> The script first uploads a PHP shell in a loop using the requests.post() method. The loop runs 4096 * 4096 times, trying to win the race condition. Once the PHP shell is uploaded, the script starts bruteforcing the inclusion of the uploaded file using LFI vulnerabilities. The itertools.combinations() method is used to generate all possible combinations of six characters from the set of ASCII letters and digits. The script then sends GET requests to the target server with the URL of the included file. If the response contains the string 'load average', the script assumes that the PHP shell has been successfully included and executed on the server. The script then prints the URL of the included file and exits. If the loop completes without finding a valid inclusion, the script prints an error message and exits.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Tags

- [[File Inclusion]]
- [[LFI to RCE via upload (race)]]
