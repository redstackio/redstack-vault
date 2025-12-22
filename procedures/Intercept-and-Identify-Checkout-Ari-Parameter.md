---
id: proc-uuid-3
tags:
  - intercept
  - parameter-identification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:47.479Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Identify-Checkout-Ari-Parameter

## Summary

This procedure uses Burp Suite to intercept the Affirm API POST request and locate the 'checkout_ari' parameter for subsequent modification.

## Description

After selecting Affirm, the API request is captured in transit. Forwarding to Repeater allows inspection of the parameter, which is specific to the transaction and lacks access controls, enabling IDOR.

## Requirements

1. Burp Suite running as proxy
2. Browser traffic routed through proxy
3. Familiarity with HTTP request structure

## Defense

Defensive measures and detection strategies:

- Encrypt API communications
- Detect proxy interception via timing anomalies

## Objectives

1. Capture the request
2. Identify vulnerable parameter
3. Expected outcome: 'checkout_ari' value extracted

## Instructions

### Step 1: Set Up Interception

**Context**: Configure Burp to intercept checkout traffic.

Enable interception in Burp Proxy and load the Affirm page.

> Request halts at proxy for review.

### Step 2: Forward to Repeater

**Context**: Prepare for modification.

Right-click the intercepted request and forward to Repeater; inspect body for 'checkout_ari': 'XXXXXXXXXXXXXXXX'.

> Expected output: Parameter visible in Repeater interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[parameter-identification]]
