---
tags:
  - open-redirect
  - sso
  - saml
  - phishing
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-open-redirect]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Insert-Crafted-Open-Redirect-URL]]'
  - '[[procedures/Trigger-Redirection-via-Link-Click]]'
  - '[[procedures/Observe-Bypassed-Redirection]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of a limited open redirection vulnerability in HackerOne's
  SSO-SAML sign-in endpoint by using a double slash to bypass previous patches,
  enabling direct redirection to external sites without warnings.
skill_level: beginner
impact_level: low
id: 2727a6d8-b31e-4f54-911e-00934e0eb967
created_at: '2025-12-13T09:01:26.460Z'
updated_at: '2025-12-13T09:01:26.460Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Open Redirection Patch in SSO-SAML Endpoint Using Double Slash

Multi-stage attack chain demonstrating the exploitation of a limited open redirection vulnerability in HackerOne's SSO-SAML sign-in endpoint. The attack bypasses a previous patch by inserting a double slash in the URL path, allowing redirection to an external SSO URL without triggering the external link warning page. This enables potential phishing by directly redirecting users to malicious sites, though classified as low severity.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Insert Crafted Link] --> B[Click Link to Trigger] --> C[Observe Redirection]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None

### Target Environment

- Web platform
- SSO-SAML service
- Network access to HackerOne endpoint

### Initial Access Requirements

- Ability to insert links in comments or reports on HackerOne
- No credentials required beyond access to the platform

## Detailed Attack Procedures

### Step 1: Insert Crafted Open Redirect URL
procedure: [[procedures/Insert-Crafted-Open-Redirect-URL]]

**Objective**: Add a specially crafted URL with double slash to a comment or report to set up the redirection.

**Instructions**: Insert the URL 'https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true' into a comment or report on HackerOne. This URL exploits the insufficient validation by using a double slash in the path.

To test the URL crafting, you can use [[commands/curl-test-open-redirect]]:

```bash
curl -I 'https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true'
```

**Expected Output**: The URL is successfully inserted without immediate errors.

**Success Indicators**:
- Link appears in the comment or report
- No validation errors from the platform

### Step 2: Trigger Redirection via Link Click
procedure: [[procedures/Trigger-Redirection-via-Link-Click]]

**Objective**: Simulate user interaction by clicking the inserted link to initiate the redirection.

**Instructions**: Click on the inserted link in the comment or report. This action triggers the open redirection due to the bypassed patch.

You can simulate the request using [[commands/curl-test-open-redirect]] to follow redirects:

```bash
curl -L 'https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true'
```

**Expected Output**: The browser or tool follows the link and redirects.

**Success Indicators**:
- Redirection occurs without interruption
- No warning page is displayed

### Step 3: Observe Bypassed Redirection
procedure: [[procedures/Observe-Bypassed-Redirection]]

**Objective**: Verify that the redirection bypasses the external link warning and lands on the target SSO URL.

**Instructions**: After clicking, observe the final URL in the browser or tool output. The user is redirected directly to the SSO URL 'saml/sign_in?email=teste@snapchat.com&remember_me=true' without the protective warning page, due to the double slash bypassing the regex validation.

Use [[commands/curl-test-open-redirect]] to confirm the final location:

```bash
curl -I -L 'https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true'
```

**Expected Output**: Final redirection to the external SSO URL.

**Success Indicators**:
- Direct redirection to external site
- Absence of external link warning page

## Attack Chain Summary

### Key Achievements

1. Successful bypass of open redirection patch using double slash
2. Direct redirection to external SSO URL
3. Potential for phishing without user warnings

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

*Last updated: 2023-10-01*
