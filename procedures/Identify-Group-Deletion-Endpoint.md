---
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
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
updated_at: '2025-12-14T17:27:15.134Z'
sub_techniques: []
id: 641bd7c0-0698-40c0-9daf-1918af05b763
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Group Deletion Endpoint

## Summary

This procedure involves inspecting the target web application to identify the group deletion endpoint and its parameters, confirming the CSRF vulnerability by testing token omission.

## Description

In the context of Localize, the group deletion form submits a POST request to a specific endpoint without enforcing CSRF token validation. By examining network requests in browser tools, attackers can pinpoint the URL (e.g., http://www.localize.io/pages/create_project/9k) and parameters (deleteGroup[id] for the group ID, and CSRFToken which can be empty). This step is crucial for crafting targeted exploits, assuming the attacker has knowledge of a valid group ID from prior reconnaissance or social engineering.

## Requirements

1. Access to the Localize web application (publicly accessible)
2. Browser with developer tools (e.g., Chrome DevTools)
3. Knowledge of a target group ID (e.g., from victim's account info)

## Defense

Defensive measures and detection strategies:

- Implement strict CSRF token validation on all state-changing endpoints
- Monitor for anomalous deletion requests without tokens in server logs
- Use Content Security Policy (CSP) to restrict form submissions to same-origin

## Objectives

1. Locate the exact deletion endpoint and parameters
2. Verify lack of CSRF protection
3. Prepare data for malicious form construction

## Instructions

### Step 1: Inspect the Application

**Context**: Navigate to the group management section in Localize and attempt to delete a test group to capture the request.

Open browser developer tools (Network tab), trigger the deletion, and examine the POST request.

**Expected Output**: Request details showing endpoint http://www.localize.io/pages/create_project/9k, parameters deleteGroup[id]=<id>, and CSRFToken (if present).

### Step 2: Test Token Omission

**Context**: Replay the request with an empty CSRFToken to confirm vulnerability.

Use browser tools or a proxy to modify and resend the request, omitting or emptying the token.

**Expected Output**: Successful deletion response (e.g., 200 OK) without token, proving the flaw.

**Success Indicators**:
- Endpoint and parameters documented
- Token bypass confirmed

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-recon]]
