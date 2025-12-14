---
id: proc-8x8-endpoint-identify-001
tags:
  - api-recon
  - endpoint-discovery
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:30:47.047Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify Invite Endpoint in 8x8 Connect

## Summary

This procedure involves examining the 8x8 Connect platform's API to identify the POST /api/v1/users/<User ID>/invites endpoint, which is used for sending user invites and forms the basis for access control exploitation.

## Description

In the 8x8 Connect web platform, admins manage users via API endpoints. By inspecting network traffic or API docs during normal invite operations, attackers discover the vulnerable endpoint that accepts a User ID in the path. This allows testing for improper authorization. The procedure assumes authenticated admin access and focuses on reconnaissance to confirm endpoint functionality before exploitation. Expected outcomes include understanding the endpoint's parameters like email and role in the request body.

## Requirements

1. Authenticated admin session in 8x8 Connect
2. Access to browser developer tools or an HTTP client like curl
3. Knowledge of the target platform's base URL (connect.8x8.com)

## Defense

Defensive measures and detection strategies:

- Implement API rate limiting on user management endpoints
- Log all API calls with User ID parameters for anomaly detection
- Enforce strict authorization checks at the application level

## Objectives

1. Locate the invite-sending API endpoint
2. Document its path and payload structure
3. Prepare for authorization testing

## Instructions

### Step 1: Inspect Platform API

**Context**: Use browser tools to capture API calls during a legitimate invite action.

Navigate to the user management section in 8x8 Connect, attempt to send an invite as the current admin, and monitor the network tab for the POST request to /api/v1/users/<User ID>/invites.

**Expected Output**: Request details showing path with User ID and JSON body with invite data.

### Step 2: Verify Endpoint Accessibility

**Context**: Confirm the endpoint responds to authenticated requests.

Send a GET or OPTIONS request to the base path if available, or prepare a sample POST to test.

**Expected Output**: 200 OK or endpoint schema confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[api-recon]]
- [[endpoint-discovery]]
