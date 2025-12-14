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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:03.821Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 4f95c47f-b018-4141-a8dc-ca6ae31f8741
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-CSRF-Vulnerable-Invitation-Endpoint

## Summary

This procedure involves reconnaissance to identify the endpoint handling private project invitation acceptances in Localize and confirm the absence of server-side CSRF token validation, enabling subsequent forgery.

## Description

In the context of web applications like Localize, invitation processes often use POST requests to endpoints such as /invitations/{id}. By inspecting network traffic during a legitimate acceptance, attackers can observe form parameters including CSRFToken, userID, accept, and role. The key vulnerability is that the server processes requests without validating the CSRFToken, allowing cross-origin forgery. This step requires access to a test invitation or observation of the application's behavior.

## Requirements

1. Access to a Localize account to generate or observe an invitation
2. Web browser with developer tools (e.g., Chrome DevTools)
3. Knowledge of the target domain (www.localize.io)

## Defense

Defensive measures and detection strategies:

- Implement and enforce server-side CSRF token validation for all state-changing endpoints
- Use SameSite cookies to mitigate cross-site requests
- Monitor for anomalous invitation acceptances from unexpected sources

## Objectives

1. Locate the exact POST endpoint for invitation acceptance
2. Document required form parameters
3. Verify lack of CSRF protection

## Instructions

### Step 1: Generate or Access an Invitation

**Context**: Create a test invitation in Localize to observe the acceptance flow.

Log into Localize, create a private project, and generate an invitation link. Note the invitation ID from the URL (e.g., /invitations/9l).

### Step 2: Inspect Legitimate Request

**Context**: Use browser tools to capture the POST request during acceptance.

Navigate to the invitation acceptance page, open DevTools (F12), go to the Network tab, and submit the acceptance form. Filter for POST requests to /invitations/{id} and examine the request payload.

**Expected Output**: Payload shows fields like CSRFToken (a value), invitations[userID]: 'value', invitations[accept]: 'true', invitations[role]: 'member'.

### Step 3: Test CSRF Validation

**Context**: Attempt a forged request without a valid token to confirm vulnerability.

Use a tool like curl or Postman to send a POST to the endpoint with empty CSRFToken. If accepted, vulnerability confirmed.

**Expected Output**: Server processes the request despite invalid/empty token.

**Success Indicators**:
- Endpoint and parameters identified
- Forged request succeeds without token

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-recon]]
