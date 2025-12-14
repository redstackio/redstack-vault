---
id: ac-gitlab-open-redirect-phishing
name: GitLab Open Redirect in Dashboard and Issues Controllers for Phishing
tags:
  - open-redirect
  - phishing
  - gitlab
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-Open-Redirect-in-GitLab-Dashboard-Todos]]'
  - '[[procedures/Trigger-Open-Redirect-in-GitLab-Projects-Issues]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:23.474Z'
description: >-
  An attack chain exploiting open redirect vulnerabilities in GitLab's
  Dashboard::TodosController and Projects::IssuesController to redirect
  authenticated and unauthenticated users to arbitrary external sites, enabling
  phishing attacks.
skill_level: low
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
# GitLab Open Redirect in Dashboard and Issues Controllers for Phishing

Multi-stage attack chain demonstrating exploitation of open redirect vulnerabilities in GitLab to facilitate phishing by redirecting users to malicious external sites.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Vulnerable Endpoint] --> B[Trigger Redirect to Malicious Site]
    B --> C[Phishing Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[commands/curl-test-gitlab-redirect]]

### Target Environment

- GitLab instance (Ruby on Rails web application)
- Access to dashboard/todos endpoint (requires authentication)
- Access to projects/issues endpoint (no authentication required)

### Initial Access Requirements

- Valid GitLab URL (e.g., https://gitlab.example.com)
- For dashboard: Authenticated session
- Network access to the GitLab instance

## Detailed Attack Procedures

### Step 1: Exploit Dashboard Todos Redirect
procedure: [[procedures/Trigger-Open-Redirect-in-GitLab-Dashboard-Todos]]

**Objective**: Redirect an authenticated user from the GitLab dashboard todos page to an external malicious site for phishing.

**Instructions**: Authenticate to the GitLab instance, then construct and visit a manipulated URL with the 'host' parameter set to a malicious domain. Use [[commands/curl-test-gitlab-redirect]] to test the redirect behavior:

```bash
curl -L -v "https://gitlab.example.com/dashboard/todos?page=99999999&host=www.evil.com" --cookie "session=your_session_cookie"
```

**Expected Output**: HTTP 302 redirect to https://www.evil.com, confirming the open redirect.

**Success Indicators**:
- Redirect occurs to the specified external host
- No validation error on the 'host' parameter

### Step 2: Exploit Projects Issues Redirect
procedure: [[procedures/Trigger-Open-Redirect-in-GitLab-Projects-Issues]]

**Objective**: Redirect an unauthenticated user from the GitLab projects issues page to an external malicious site, enabling broad phishing without login.

**Instructions**: Construct and visit a manipulated URL targeting the issues controller with the 'host' parameter. Use [[commands/curl-test-gitlab-redirect]] to verify:

```bash
curl -L -v "https://gitlab.example.com/projects/issues?page=99999999&host=www.evil.com"
```

**Expected Output**: HTTP 302 redirect to https://www.evil.com without requiring authentication.

**Success Indicators**:
- Successful redirect to external host
- Endpoint accessible without login

## Attack Chain Summary

### Key Achievements

1. Bypassed redirect validation in GitLab controllers using untrusted 'host' parameter
2. Enabled phishing by tricking users into visiting arbitrary external sites
3. Demonstrated impact on both authenticated (dashboard) and unauthenticated (issues) users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[T1566.002]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
