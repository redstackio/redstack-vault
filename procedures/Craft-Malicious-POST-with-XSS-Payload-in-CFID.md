---
tags:
  - xss
  - csrf
  - injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - ColdFusion
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:43.108Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: aa403a01-4431-4c97-95e5-e289d04674ce
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-POST-with-XSS-Payload-in-CFID

## Summary

This procedure crafts a POST request injecting an XSS payload into the CFID session parameter on the MTN deals endpoint, exploiting reflection without sanitization to execute JavaScript.

## Description

The CFID parameter, used for session management in ColdFusion, is reflected back in the HTML response without escaping, allowing closure of tags and script injection. The payload appends to a valid UUID, e.g., 'fbe8c86c-c0b2-4421-8ca2-dcfc14763d6e"><img src=x onerror=alert(document.domain)>'. When sent via CSRF, this executes in the victim's authenticated context, stealing cookies or local storage. Requires prior endpoint identification and Burp Suite for crafting.

## Requirements

1. Identified vulnerable endpoint from previous procedure
2. Burp Suite for request modification and encoding
3. Knowledge of URL encoding for payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all reflected inputs, especially session IDs
- Implement output encoding for HTML contexts in ColdFusion
- Use Web Application Firewall (WAF) rules to block script injections in parameters

## Objectives

1. Inject and reflect XSS payload via tampered CFID
2. Verify JavaScript execution in response
3. Enable session theft or page manipulation

## Instructions

### Step 1: Prepare Payload

**Context**: Construct the XSS payload and URL-encode it for safe transmission.

Create payload: fbe8c86c-c0b2-4421-8ca2-dcfc14763d6e"><img src=x onerror=alert(document.domain)>. Encode to %27fbe8c86c-c0b2-4421-8ca2-dcfc14763d6e%22%3E%3Cimg%20src%3Dx%20onerror%3Dalert%28document.domain%29%3E.

**Expected Output**: Encoded string ready for insertion.

### Step 2: Modify Request in Burp

**Context**: Insert payload into CFID and set other parameters.

In Burp Repeater, update POST body: CFID=<encoded_payload>, CFTOKEN=0, category_id=9, cpID=1, location_id=0, m=1. Target /index.cfm?GO=DEALS.

**Expected Output**: Send request and see alert pop-up in browser.

### Step 3: Validate Reflection

**Context**: Inspect response for unsanitized output.

Check HTML response for the injected <img> tag executing onerror.

**Expected Output**: Script runs, alerting domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[csrf]]
- [[injection]]
