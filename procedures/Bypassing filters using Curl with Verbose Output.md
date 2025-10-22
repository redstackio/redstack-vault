---
id: ea9d81b8-25ce-4e72-ad1f-cae24499d92e
name: Bypassing filters using Curl with Verbose Output
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.512145+00:00'
updated_at: '2023-04-10T20:24:11.239089+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
- '[[Web Service|T1102 - Web Service]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypass using bash variables]]'
- '[[Server-Side Request Forgery]]'
commands:
- '[[Assign empty string to variable]]'
- '[[Verify URL with cURL]]'
---

# Bypassing filters using Curl with Verbose Output

## Summary

Bypassing filters using Curl with Verbose Output is a technique used to bypass filters in a Server-Side Request Forgery attack. This technique involves using bash variables to manipulate the output of the Curl command, allowing an attacker to bypass filters and access resources that may not have be

## Description

# Description

Bypassing filters using Curl with Verbose Output is a technique used to bypass filters in a Server-Side Request Forgery attack. This technique involves using bash variables to manipulate the output of the Curl command, allowing an attacker to bypass filters and access resources that may not have been intended to be accessed. This technique can be used to discover information about a target system, as well as to evade detection by hiding the attack in the output of the Curl command.

Technical Explanation: An attacker can use Curl with Verbose Output to send a request to a target system and view the full response. By manipulating the output of the Curl command using bash variables, an attacker can bypass filters that may be in place to prevent access to certain resources. This technique can be used to access internal systems or sensitive data that may not be intended to be accessed by an attacker.

Business Value: By using this technique, an attacker can gain access to sensitive data or systems, which can lead to financial loss, reputational damage, and legal consequences. This technique can also be used to gather information about a target system, which can be used to launch further attacks.

## Requirements

1. Access to a system with Curl installed

1. Knowledge of bash variables and how to manipulate them

## Defense

1. Implement input validation to prevent Server-Side Request Forgery attacks

1. Monitor network traffic for suspicious activity, such as Curl commands with verbose output

1. Implement access controls to restrict access to sensitive data or systems

## Objectives

1. Bypass filters to access sensitive data or systems

1. Evade detection by hiding the attack in the output of the Curl command

1. Gather information about a target system for further attacks

# Instructions

1. To execute a curl command with verbose output, use the -v option followed by the URL. This will display additional information about the request and response, such as the headers and status codes.

**Code**: [[curl -v "http://evil$google.com"
$google = ""]]

> The -v option can be useful for debugging and troubleshooting HTTP requests. It provides more detailed information about the request and response, which can help identify issues such as incorrect headers or unexpected responses. In this example, the command is using the URL http://evil$google.com, which is not a valid URL and will likely result in an error. The variable $google is also being assigned an empty string, but it is not clear what this variable is being used for.

**Command** ([[Verify URL with cURL]]):

```bash
curl -v "http://evil$google.com"
```

**Command** ([[Assign empty string to variable]]):

```bash
$google = ""
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]
- [[Web Service|T1102 - Web Service]]

## Commands Used

- [[Assign empty string to variable]]
- [[Verify URL with cURL]]

## Tags

- [[Bypassing filters]]
- [[Bypass using bash variables]]
- [[Server-Side Request Forgery]]
