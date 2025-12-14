---
tags:
  - open-redirect
  - gitlab
  - phishing
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-and-Test-GitLab-Repository-Import]]'
  - '[[procedures/Observe-continue-to-Parameter-Exposure]]'
  - '[[procedures/Exploit-Open-Redirect-with-Double-Slash-Bypass]]'
step_count: 3
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.213Z'
description: >-
  Multi-stage attack chain exploiting an open redirect vulnerability in GitLab's
  Repository Import feature using the continue[to] parameter to redirect users
  to external phishing sites.
id: 469e7623-8551-432f-a008-04789d1b5ac1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# GitLab-Open-Redirect-via-Repository-Import-continue-to-Parameter

Multi-stage attack chain demonstrating exploitation of an open redirect in GitLab 9.0 CE's Repository Import functionality, allowing redirection of users with view permissions to external sites for phishing.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup and Test Import] --> B[Observe Parameter Exposure]
    B --> C[Exploit Redirect]
    C --> D[Phishing Redirect]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual testing via browser or curl)

### Target Environment

- GitLab 9.0 CE installation
- Web platform with Repository Import service enabled
- Access to a repository with view permissions

### Initial Access Requirements

- Valid user account with view access to a GitLab project/repository
- No edit permissions required for observation
- Network access to the GitLab instance

## Detailed Attack Procedures

### Step 1: Setup and Test Repository Import
procedure: [[procedures/Setup-and-Test-GitLab-Repository-Import]]

**Objective**: Establish a test environment and explore the Repository Import feature to identify potential entry points.

**Instructions**: Install a fresh GitLab 9.0 CE instance and navigate to the import functionality for a target repository. Attempt to initiate an import process without edit permissions to trigger error states.

**Expected Output**: Access to the import interface and initial error messages upon permission denial.

**Success Indicators**:
- GitLab instance running successfully
- Repository Import page accessible

### Step 2: Observe Parameter Exposure
procedure: [[procedures/Observe-continue-to-Parameter-Exposure]]

**Objective**: Identify the vulnerable continue[to] parameter through error message leakage, confirming exposure without elevated privileges.

**Instructions**: Trigger an import attempt on a repository where the user lacks edit permissions. Inspect the error response for reflected parameters.

**Expected Output**: Error message displaying 'You're not allowed to make changes to this project directly' with the continue[to] parameter visible.

**Success Indicators**:
- Parameter revealed in error output
- Confirmation of view-only access sufficiency

### Step 3: Exploit Open Redirect
procedure: [[procedures/Exploit-Open-Redirect-with-Double-Slash-Bypass]]

**Objective**: Construct and test a malicious URL to bypass validation and redirect to an external site, enabling phishing.

**Instructions**: Modify the continue[to] parameter in the import URL using a double-slash prefix (e.g., //evil.com) to force an external redirect. Share the URL with a victim possessing view permissions.

**Expected Output**: Automatic browser redirect to the external domain upon accessing the crafted URL.

**Success Indicators**:
- Successful redirect to external site
- No validation blocking the double-slash bypass

## Attack Chain Summary

### Key Achievements

1. Identified open redirect in GitLab Repository Import without requiring edit access
2. Bypassed internal validation using double-slash prefix
3. Enabled phishing attacks on users with view permissions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
