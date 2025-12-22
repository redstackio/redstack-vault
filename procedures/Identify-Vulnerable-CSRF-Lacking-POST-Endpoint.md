---
id: proc-uuid-1
tags:
  - csrf
  - web
  - recon
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:21.025Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify-Vulnerable-CSRF-Lacking-POST-Endpoint

## Summary

This procedure identifies POST endpoints in web applications that lack CSRF protection, enabling attackers to forge requests from external sites on behalf of authenticated users. It is primarily used in web penetration testing to uncover cross-origin request vulnerabilities.

## Description

In the context of a U.S. Department of Defense web application, this step targets endpoints like /submit-form that accept form data without CSRF tokens. By proxying legitimate traffic and testing for token absence, attackers confirm the ability to craft cross-site requests. Prerequisites include network access to the target and an authenticated session. Expected outcomes are the pinpointing of exploitable endpoints leading to unauthorized actions such as data submission.

## Requirements

1. Proxy tool like Burp Suite for traffic interception
2. Authenticated access to the target web application
3. Basic knowledge of HTTP requests and CSRF mechanics

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST endpoints
- Use SameSite cookies and Content-Security-Policy headers to mitigate cross-site requests
- Monitor for anomalous cross-origin POSTs in server logs

## Objectives

1. Locate unprotected POST endpoints
2. Verify cross-origin submission feasibility
3. Prepare for payload injection in subsequent steps

## Instructions

### Step 1: Proxy and Inspect Legitimate Requests

**Context**: Capture normal form submissions to analyze for CSRF protections.

Use [[tools/Burp-Suite]] to intercept traffic: Configure your browser to proxy through Burp, submit the target form (e.g., for building and classroom selection), and examine the POST request in the Proxy history.

**Expected Output**: Request details showing parameters like building, classroom, course without _csrf or similar tokens.

### Step 2: Test for CSRF Absence

**Context**: Confirm vulnerability by simulating a cross-origin request.

In Burp Repeater, copy the legitimate POST request to /submit-form. Modify the Origin header to an external domain (e.g., evil.com) and resubmit. If accepted without error, CSRF protection is lacking.

**Expected Output**: Successful 200 OK response with form processed.

### Step 3: Document Endpoint Details

**Context**: Record findings for chaining with XSS payloads.

Note the full URL (e.g., https://target-site.com/submit-form), required parameters, and any authentication headers needed.

**Expected Output**: Endpoint profile ready for exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web]]
- [[recon]]
