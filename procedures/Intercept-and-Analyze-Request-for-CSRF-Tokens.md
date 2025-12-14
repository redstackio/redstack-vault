---
tags:
  - csrf
  - analysis
  - interception
type: procedure
tools:
  - '[[tools/Tamper-Data]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:22.849Z'
sub_techniques: []
id: 71207d1b-4a37-4822-a52b-5a388720e104
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Analyze-Request-for-CSRF-Tokens

## Summary

This procedure examines the captured HTTP POST request from the Slack form to detect missing anti-CSRF tokens, confirming the vulnerability.

## Description

By inspecting the request headers, body, and parameters in Tamper Data, testers can verify the absence of CSRF protections. In Slack's case, no tokens were found, allowing potential forgery from malicious sites, leading to unauthorized support requests and possible information disclosure or actions by the support team.

## Requirements

1. Intercepted POST request from form submission
2. Tamper Data dialog open with request details
3. Understanding of HTTP structures and CSRF mechanics

## Defense

Defensive measures and detection strategies:

- Always include and validate CSRF tokens server-side
- Audit request logs for anomalous submissions

## Objectives

1. Identify missing security tokens
2. Document request structure for reporting
3. Assess exploitability for unauthorized actions

## Instructions

### Step 1: Review Request Details

**Context**: Examine the full request payload.

In Tamper Data, view the Headers tab for custom tokens (e.g., X-CSRF-Token) and the POST Data tab for form parameters.

> Look for fields like csrf_token, _token, or authenticity_token; absence indicates vulnerability.

**Expected Output**: No token fields present in headers or body.

### Step 2: Tamper and Proceed

**Context**: Test by allowing the request to continue unmodified.

Click "Send" or "Tamper" without changes to complete submission, then re-inspect if needed.

> Confirms the server accepts requests without token validation.

**Expected Output**: Request succeeds, form submission completes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Tamper-Data]]

## Tags

- [[csrf]]
- [[analysis]]
