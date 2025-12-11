---
tags:
  - request-interception
  - proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 023abcb7-f821-4049-b643-f8c1f0ad795f
created_at: '2025-12-11T06:10:15.789Z'
updated_at: '2025-12-11T06:10:15.789Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Intercept Smart2Pay POST Request

## Summary

This procedure uses a proxy tool to capture the HTTP POST request to the Smart2Pay API during Steam payment processing.

## Description

Configure a tool like Burp Suite to intercept traffic to https://globalapi.smart2pay.com/. The request contains form-urlencoded data including MerchantID, Amount, CustomerEmail, and Hash. This allows analysis and modification in the next steps.

## Requirements

1. Proxy tool like Burp Suite set up
2. Browser configured to route through the proxy
3. Active payment initiation from Steam

## Defense

Defensive measures and detection strategies:

- Enforce client-side integrity checks
- Detect proxy usage via anomalies in request headers

## Objectives

1. Capture the vulnerable request
2. Expose parameters for tampering
3. Enable hash analysis

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception for the target domain.

Launch Burp Suite and configure the browser to use it as a proxy.

### Step 2: Capture Request

**Context**: Intercept during payment.

Proceed with the payment and pause the POST request in Burp's Proxy tab.

> Examine fields like Amount and CustomerEmail.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-interception
- proxy
