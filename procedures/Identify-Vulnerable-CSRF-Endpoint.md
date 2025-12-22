---
tags:
  - csrf
  - recon
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
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
updated_at: '2025-12-13T23:55:20.441Z'
sub_techniques: []
id: ee6593fb-5f8b-4f9a-bcb2-bbf89c8e38f4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-CSRF-Endpoint

## Summary

This procedure identifies POST endpoints on web applications lacking CSRF protection, such as the MTN Daily Deals /index.cfm?GO=DEALS endpoint, allowing attackers to forge requests on behalf of users.

## Description

In the context of the MTN Daily Deals site built on ColdFusion, this step involves inspecting form submissions to confirm the absence of CSRF tokens and input validation on parameters like CFID. The endpoint processes POST data without verifying the request origin, enabling cross-site forgery. Prerequisites include network access to the target HTTPS site and a tool like Burp Suite for traffic interception.

## Requirements

1. Access to the target website (https://dailydeals.mtn.co.za)
2. Proxy tool like Burp Suite to capture requests
3. Basic knowledge of HTTP POST forms and session parameters

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Enforce same-origin policy checks on POST requests
- Monitor for anomalous POST requests from external referers

## Objectives

1. Confirm vulnerable endpoint for forged requests
2. Identify unsanitized parameters like CFID
3. Establish foundation for payload injection

## Instructions

### Step 1: Intercept Legitimate Requests

**Context**: Capture normal form submissions to analyze parameters and protections.

Use [[tools/Burp-Suite-Professional]] to proxy traffic and submit a form on the deals page.

**Expected Output**: HTTP POST to /index.cfm?GO=DEALS with parameters like CFID, CFTOKEN, category_id.

### Step 2: Test for CSRF Protection

**Context**: Modify the request origin and resubmit to check enforcement.

Remove any tokens and send from a different origin; if accepted, vulnerability confirmed.

**Expected Output**: Successful response without errors, indicating no protection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[web]]
