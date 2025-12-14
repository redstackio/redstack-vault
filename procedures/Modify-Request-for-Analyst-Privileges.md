---
id: proc-uuid-003
tags:
  - privilege-escalation
  - credential-modification
  - csrf-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:07.502Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Modify-Request-for-Analyst-Privileges

## Summary

This procedure involves altering an intercepted API request by replacing authentication cookies and CSRF token with those from a lower-privileged Analyst account, enabling unauthorized access to restricted data in LinkedIn's Voyager API.

## Description

The vulnerability stems from inadequate authorization on the endpoint, allowing requests with Analyst credentials to retrieve admin-only data. Obtain Analyst session details separately (e.g., login with Analyst account and copy from browser dev tools). This step prepares the request for escalation. Expected outcome: Modified request that evades privilege checks.

## Requirements

1. Intercepted request from previous step
2. Analyst role LinkedIn account and its Cookie/CSRF-Token values
3. Burp Suite Repeater or Intruder for editing

## Defense

Defensive measures and detection strategies:

- Implement strict authorization checks on API endpoints beyond authentication
- Validate session roles per endpoint
- Detect token mismatches or unusual header modifications via WAF

## Objectives

1. Swap credentials to simulate lower privileges
2. Preserve request integrity for valid response
3. Test for escalation success

## Instructions

### Step 1: Obtain Analyst Credentials

**Context**: Gather session data from Analyst login.

Login with Analyst account in a separate browser; inspect network tab for Cookie and CSRF-Token on any request.

> Expected output: Values like Cookie: JSESSIONID=abc123; li_at=def456 and CSRF-Token: abcdef123456.

### Step 2: Edit Intercepted Request

**Context**: Replace headers in proxy to use Analyst values.

In Burp Suite, edit the intercepted request: Replace entire Cookie header and Csrf-Token with Analyst values. Keep URL/parameters unchanged.

> Expected output: Updated request headers; no parsing errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- privilege-escalation
- credential-modification
- csrf-bypass
