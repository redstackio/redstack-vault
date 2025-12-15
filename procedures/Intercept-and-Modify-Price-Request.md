---
id: intercept-modify-001
name: Intercept and Modify Price Request
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:48.037Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - idor
  - request-tampering
  - burp-suite
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
commands: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Intercept and Modify Price Request

## Summary

This procedure uses Burp Suite to capture the 'Buy Now' HTTP request during Acronis.cz checkout and modifies the price parameter, exploiting IDOR to set an arbitrary low value (e.g., 1 unit) that the server accepts without validation.

## Description

The Acronis.cz checkout endpoint suffers from IDOR, allowing unauthenticated manipulation of the price parameter in client-side requests. By proxying traffic through Burp Suite, attackers intercept the POST request, alter the price from its original value to a minimal positive amount, and forward it. The server lacks integrity checks or encryption, accepting changes >0, which propagates to payment gateways. This targets web-based e-commerce environments and requires intermediate proxy tool knowledge.

## Requirements

1. Burp Suite installed and running
2. Browser proxy set to Burp (e.g., 127.0.0.1:8080)
3. Completed checkout form from prior steps

## Defense

Defensive measures and detection strategies:

- Server-side validation of price against session/cart state
- Encrypt or sign request parameters
- Log and alert on price changes > threshold (e.g., 50% reduction)

## Objectives

1. Capture and tamper with the vulnerable price parameter
2. Bypass lack of request validation to enforce low price
3. Advance to payment with manipulated data

## Instructions

### Step 1: Enable Intercept Mode

**Context**: Configure Burp Suite to pause and inspect outgoing requests from the browser.

In Burp Suite Proxy > Options, ensure intercept is on. Set browser proxy accordingly.

> No command; GUI action. Expected output: 'Intercept is on' status.

### Step 2: Trigger and Capture Request

**Context**: Initiate the request to capture it for modification.

Click 'Buy Now' in browser; request pauses in Burp Intercept tab.

> Expected output: Raw HTTP request visible, including price parameter.

### Step 3: Modify and Forward

**Context**: Alter the price to exploit IDOR.

Edit the price field (e.g., change 'price=1000' to 'price=1'), then click 'Forward'.

> Server response: 200 OK or redirect if accepted; rejection only for <=0.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[request-tampering]]
- [[tools/Burp-Suite]]
