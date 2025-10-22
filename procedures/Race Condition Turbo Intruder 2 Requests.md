---
id: 31ac787b-e78f-44d6-8cd1-dd23be0b6526
name: Race Condition Turbo Intruder 2 Requests
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.922683+00:00'
updated_at: '2023-04-06T03:56:31.938611+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
tags:
- '[[Race Condition]]'
- '[[Turbo Intruder 2 Requests Examples]]'
---

# Race Condition Turbo Intruder 2 Requests

## Summary

This procedure involves utilizing Turbo Intruder 2 to exploit a time-of-check time-of-use (TOCTOU) race condition vulnerability. This type of vulnerability occurs when a resource is checked for a certain condition, but the condition changes before the resource is used. In this case, Turbo Intruder 

## Description

# Description

This procedure involves utilizing Turbo Intruder 2 to exploit a time-of-check time-of-use (TOCTOU) race condition vulnerability. This type of vulnerability occurs when a resource is checked for a certain condition, but the condition changes before the resource is used. In this case, Turbo Intruder 2 is used to send multiple requests in quick succession, causing a race condition where the server may respond with unexpected results.

This technique can be used by attackers to escalate privileges or gain unauthorized access to sensitive information. From a technical perspective, Turbo Intruder 2 is a powerful tool that allows for the automation of sending multiple HTTP requests and analyzing the responses. From a business standpoint, this procedure can help identify and remediate vulnerabilities before they can be exploited by attackers.

## Requirements

1. Access to Turbo Intruder 2

1. Knowledge of HTTP requests and responses

1. Access to target system

## Defense

1. Implement proper input validation and error handling to prevent race conditions

1. Implement proper access controls to limit unauthorized access

1. Regularly monitor and analyze system logs for suspicious activity

## Objectives

1. Identify and exploit time-of-check time-of-use race condition vulnerabilities

1. Gain unauthorized access to sensitive information

1. Escalate privileges

# Instructions

1. To use this template, replace the <REDACTED> placeholders with the appropriate values for your target. Additionally, modify the 'parameterName' and 'parameterValue' fields as needed to match the parameters you wish to send. Finally, modify the 'target-URI-1' and 'target-URI-2' fields to match the endpoints you wish to target with the requests.

**Code**: [[def queueRequests(target, wordlists): 
    engine ]]

> This template is useful for testing the response of a web application when multiple requests are sent simultaneously. The 'request1' variable sends a POST request to the target endpoint with the specified parameters. The 'request2' variable sends a GET request to a different endpoint on the same target. These requests are then queued up in the 'engine' object, with the 'race1' gate being used to ensure they are sent simultaneously. The 'handleResponse' function can be used to handle any responses received from the target. The 'table.add' function can be used to add any interesting responses to a table for further analysis.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

## Tags

- [[Race Condition]]
- [[Turbo Intruder 2 Requests Examples]]
