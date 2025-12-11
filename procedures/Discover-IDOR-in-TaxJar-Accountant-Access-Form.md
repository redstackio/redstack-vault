---
tags:
  - idor
  - web-vuln
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: dbb05b71-b480-4223-8720-e71b91b479e4
created_at: '2025-12-11T03:47:49.163Z'
updated_at: '2025-12-11T03:47:49.163Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Discover IDOR in TaxJar Accountant Access Form

## Summary

This procedure involves identifying an Insecure Direct Object Reference (IDOR) vulnerability in the Accountant Access form of TaxJar by examining the form and testing the POST endpoint for manipulable parameters.

## Description

The attack targets the /accounts/<ACCOUNT_NUMBER> endpoint, which handles email changes. By altering the account number, attackers can target any user without authorization checks, leading to potential account takeovers. This is discovered through manual inspection of requests in a web proxy or browser tools.

## Requirements

1. Access to TaxJar's Accountant Access form
2. Web proxy tool like Burp Suite for request interception (optional)
3. Basic knowledge of HTTP requests and parameters

## Defense

Defensive measures and detection strategies:

- Implement proper authorization checks on object references
- Monitor for anomalous request patterns to the endpoint

## Objectives

1. Identify vulnerable endpoint for email changes
2. Confirm manipulability of account number parameter
3. Document lack of authorization validation

## Instructions

### Step 1: Examine the Accountant Access Form

**Context**: Navigate to the form and inspect the network requests to find the POST endpoint.

Use browser developer tools to capture the request to /accounts/<ACCOUNT_NUMBER>.

> Expected: Identification of the endpoint and parameters like account number and email.

### Step 2: Test Parameter Manipulation

**Context**: Attempt to change the account number in the request and observe if it affects other accounts.

Replay the request with a different account number and monitor the response.

> Expected: Response indicates successful processing without authorization errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #idor
- #web-vuln
