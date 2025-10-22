---
id: c0f418a3-33dd-417a-9097-d0d8727a7266
name: Out Of Band XPATH Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.431564+00:00'
updated_at: '2023-04-10T20:24:48.337969+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Data Obfuscation|T1001 - Data Obfuscation]]'
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[Out Of Band Exploitation]]'
- '[[XPATH Injection]]'
---

# Out Of Band XPATH Injection

## Summary

Out of Band XPATH Injection is a technique used to exploit vulnerabilities in web applications that use XPATH queries to interact with XML data. This technique involves injecting malicious code into the XPATH query to extract data or perform other malicious actions. The attacker can then use an out

## Description

# Description

Out of Band XPATH Injection is a technique used to exploit vulnerabilities in web applications that use XPATH queries to interact with XML data. This technique involves injecting malicious code into the XPATH query to extract data or perform other malicious actions. The attacker can then use an out-of-band channel to exfiltrate the stolen data. This technique is particularly effective when the application filters user input, as it can bypass those filters and execute arbitrary code. 

Technical Explanation: XPATH Injection is a type of injection attack that allows an attacker to modify the intended query to extract data or perform other malicious actions. The attacker can use this technique to bypass input validation and execute arbitrary code on the server. Out-of-band data exfiltration is used to avoid detection by sending data through a separate channel that is not monitored by the target system. 

Business Value: This technique can be used to steal sensitive data such as customer information, financial data, or intellectual property. It can also be used to gain access to the target system and perform further attacks such as privilege escalation or lateral movement.

## Requirements

1. Access to the target web application

1. Knowledge of XPATH syntax and the target system's XML data structure

1. Tools such as Burp Suite or OWASP ZAP

## Defense

1. Implement input validation and sanitization to prevent XPATH Injection attacks

1. Use parameterized queries to prevent SQL Injection attacks

1. Monitor network traffic for unusual activity and out-of-band data exfiltration

## Objectives

1. Extract sensitive data from the target system

1. Gain access to the target system

1. Perform further attacks such as privilege escalation or lateral movement

# Instructions

1. This command is used to retrieve a filtered list of Foundation items from the specified URL. The filters include title, type, and rent days. The command also retrieves data from a shared folder using the doc() function.

**Code**: [[http://example.com/?title=Foundation&type=*&rent_d]]

> The 'title' filter is used to search for items with a specific title. The 'type' filter is used to search for items of a specific type, where the '*' character is used as a wildcard to match any type. The 'rent_days' filter is used to search for items that have been rented for a specific number of days. The 'doc()' function is used to retrieve data from a shared folder, where the specified path is passed as an argument to the function.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Data Obfuscation|T1001 - Data Obfuscation]]
- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Tags

- [[Out Of Band Exploitation]]
- [[XPATH Injection]]
