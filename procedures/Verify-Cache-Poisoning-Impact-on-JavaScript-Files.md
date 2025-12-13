---
tags:
  - dos
  - cache-verification
  - paypal
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: bcaef55d-b3a0-4e50-adae-c33de26b357b
created_at: '2025-12-13T09:01:16.919Z'
updated_at: '2025-12-13T09:01:16.919Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Verify Cache Poisoning Impact on JavaScript Files

## Summary

This procedure verifies the success of web cache poisoning by checking if cached JavaScript files have been replaced with error messages, confirming the denial of service impact on PayPal functionality.

## Description

After poisoning the cache, this step involves accessing the affected resources to ensure the '501 Not Implemented' error is served instead of legitimate content. This disrupts user access to essential JavaScript, preventing core website features from loading properly.

## Requirements

1. Web browser or HTTP client
2. Access to paypal.com
3. Knowledge of poisoned resource paths

## Defense

Defensive measures and detection strategies:

- Regularly flush or monitor cache contents for anomalies
- Use cache keys that include header validation

## Objectives

1. Confirm poisoned responses are served
2. Validate DoS on core functionality
3. Document impact for reporting

## Instructions

### Step 1: Access Poisoned Resource

**Context**: Request the JavaScript file to check the cached response.

```bash
curl https://www.paypalobjects.com/path/to/js/file.js
```

> Expect the output to be '501 Not Implemented' instead of JavaScript code.

### Step 2: Test Website Functionality

**Context**: Load the PayPal website in a browser to observe if JavaScript failures cause DoS.

> Navigate to paypal.com and check for broken features due to missing scripts.

> Explanation: The poisoned cache will serve errors, leading to functionality breakdowns.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[dos]]
- [[cache-verification]]
