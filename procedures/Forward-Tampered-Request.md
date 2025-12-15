---
id: proc-uuid-forward-request
tags:
  - request-forward
  - exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:29.043Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Forward-Tampered-Request

## Summary

This procedure releases the modified HTTP request to Zomato's server, applying the negative donation value and updating the cart total accordingly.

## Description

After tampering in the proxy, forwarding submits the altered payload, which the server processes without validation, resulting in a decreased order amount. This step confirms the exploit's success by observing the UI update. It requires the prior interception; outcomes include a validated manipulation without errors.

## Requirements

1. Tampered request ready in proxy
2. Active session with Zomato
3. Monitoring for server response

## Defense

Defensive measures and detection strategies:

- Implement request validation middleware to check for negatives
- Monitor cart total changes post-donation addition
- Use anomaly detection on order amounts

## Objectives

1. Submit the negative value to the server
2. Verify total reduction in cart
3. Proceed without triggering errors

## Instructions

### Step 1: Release from Proxy

**Context**: Send the request.

In Burp Proxy, click 'Forward' to release.

> Expected: 200 OK response; cart UI refreshes.

### Step 2: Validate Update

**Context**: Confirm impact.

Check cart total; it should decrease by ~0.99 to 1 rupee.

> Expected: Reduced total visible; no rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-forward
- exploit
