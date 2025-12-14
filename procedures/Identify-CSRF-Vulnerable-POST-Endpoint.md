---
tags:
  - csrf
  - web
  - discovery
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - ColdFusion
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:43.110Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3b71283b-3ebc-4ca4-b0e6-d4455ddb8157
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify-CSRF-Vulnerable-POST-Endpoint

## Summary

This procedure identifies POST endpoints in web applications lacking CSRF protection, such as the MTN Group deals page at /index.cfm?GO=DEALS, enabling subsequent request forgery attacks.

## Description

In the context of the MTN Group vulnerability, this step involves analyzing the daily deals functionality to discover that the endpoint accepts POST requests with session parameters (CFID, CFTOKEN) and business parameters (category_id, cpID, location_id, m) without validating CSRF tokens. This allows attackers to forge requests on behalf of authenticated users. Prerequisites include access to the target site and a proxy tool for traffic inspection. Expected outcomes include confirmation of vulnerability, paving the way for payload injection.

## Requirements

1. Network access to the target web application (e.g., https://deals.mtn.co.za)
2. Proxy tool like Burp Suite for intercepting requests
3. Basic understanding of HTTP POST methods and session handling in ColdFusion

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST requests
- Use same-site cookies and Content-Security-Policy headers to mitigate forgery
- Monitor for anomalous request patterns from unusual referers

## Objectives

1. Discover unprotected endpoints to enable CSRF attacks
2. Validate lack of token enforcement for session parameters
3. Prepare for chaining to other vulnerabilities like XSS

## Instructions

### Step 1: Intercept Normal Traffic

**Context**: Capture legitimate POST requests to understand the endpoint and parameters.

Use Burp Suite to proxy traffic while interacting with the deals page. Look for submissions that hit /index.cfm?GO=DEALS.

**Expected Output**: Request details showing parameters without CSRF tokens.

### Step 2: Test for CSRF Protection

**Context**: Replay the request without modifications to check if tokens are required.

In Burp Repeater, send the intercepted POST without any CSRF token and observe if it processes successfully.

**Expected Output**: Endpoint responds as if legitimate, confirming vulnerability.

### Step 3: Document Parameters

**Context**: Note all accepted parameters for later exploitation.

Record CFID, CFTOKEN, category_id=9, cpID=1, location_id=0, m=1 as exploitable.

**Expected Output**: List of parameters ready for tampering.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web]]
- [[Discovery]]
