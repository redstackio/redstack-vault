---
id: ac-slack-teamid-bypass-001
tags:
  - auth-bypass
  - slack
  - proxy
  - web
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Obtain-Slack-Workspace-Invitation]]'
  - '[[procedures/Intercept-Slack-Signup-Request]]'
  - '[[procedures/Modify-Team-ID-Parameter]]'
  - '[[procedures/Resend-Modified-Signup-Request]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.035Z'
description: >-
  Attack chain exploiting improper authentication in Slack's signup process to
  join arbitrary workspaces by manipulating the team ID parameter using an
  intercepting proxy.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized Slack Workspace Join via Team ID Manipulation

Multi-stage attack chain demonstrating exploitation of improper authentication in Slack's signup process, allowing attackers to join unauthorized workspaces without permission by manipulating the team ID in HTTP requests.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Obtain Invitation] --> B[Intercept Request]
    B --> C[Modify Team ID]
    C --> D[Resend Request]
    D --> E[Join Workspace]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web-based Slack signup process
- Access to a valid Slack invitation email
- Intercepting proxy configured to route traffic

### Initial Access Requirements

- Valid email for receiving invitations
- Network access to Slack's API endpoints
- No prior Slack account in target workspace required

## Detailed Attack Procedures

### Step 1: Obtain Workspace Invitation
procedure: [[procedures/Obtain-Slack-Workspace-Invitation]]

**Objective**: Acquire a one-time password or invitation link from a Slack workspace to extract a team ID.

**Instructions**: Generate or receive an invitation email from any Slack workspace. Note the team ID embedded in the invitation link or one-time password details.

**Expected Output**: Invitation email with team ID (e.g., a string like 'T123456789').

**Success Indicators**:
- Invitation email received
- Team ID identified from email content

### Step 2: Intercept Signup Request
procedure: [[procedures/Intercept-Slack-Signup-Request]]

**Objective**: Capture the HTTP request to Slack's signup endpoint during the invitation flow.

**Instructions**: Configure an intercepting proxy like Burp Suite to monitor traffic. Start the Slack signup process using the invitation and intercept the POST request to `api/signup.createUser`.

**Expected Output**: Captured HTTP request showing original team ID parameter.

**Success Indicators**:
- Proxy intercepts the request successfully
- Request details visible, including team ID

### Step 3: Modify Team ID Parameter
procedure: [[procedures/Modify-Team-ID-Parameter]]

**Objective**: Replace the team ID with one from a target unauthorized workspace.

**Instructions**: In the intercepted request, locate the `team_id` parameter (e.g., in JSON payload or query string) and replace it with the arbitrary team ID from another workspace's invitation.

**Expected Output**: Modified request with new team ID.

**Success Indicators**:
- Parameter updated without syntax errors
- Request remains valid HTTP format

### Step 4: Resend Modified Signup Request
procedure: [[procedures/Resend-Modified-Signup-Request]]

**Objective**: Submit the altered request to complete unauthorized signup into the target workspace.

**Instructions**: Forward the modified request through the proxy to Slack's endpoint. This only works for workspaces without admin approval for invitations.

**Expected Output**: Successful response from Slack confirming user creation and workspace join.

**Success Indicators**:
- HTTP 200 or success status
- Access granted to the arbitrary workspace

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication checks in Slack signup
2. Joined unauthorized workspace without permission
3. Demonstrated parameter tampering vulnerability

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
