---
id: ac-nextcloud-stored-xss-oauth-261138
tags:
  - xss
  - stored-xss
  - nextcloud
  - oauth
  - javascript-injection
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-Malicious-JavaScript-into-Nextcloud-OAuth-Redirect-URI]]'
  - '[[procedures/Trigger-Stored-XSS-Execution-via-OAuth-URI-Access]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:35.554Z'
description: >-
  A stored cross-site scripting attack exploiting insufficient sanitization in
  Nextcloud's OAuth redirect URI field, allowing admins to inject and persist
  malicious JavaScript that executes when the URI is accessed or displayed.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in Nextcloud OAuth Redirect URI for Admin JavaScript Injection

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in Nextcloud's OAuth redirect URI field. An admin can inject malicious JavaScript, which is stored and executed in the context of users accessing the URI, potentially leading to session theft or data exfiltration. Reported on HackerOne (#261138) with CVSS 3.4 severity due to admin-only access requirement.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Admin Access to Nextcloud] --> B[Inject Payload]
    B --> C[Trigger URI Access]
    C --> D[XSS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome Developer Tools for payload crafting)

### Target Environment

- Nextcloud instance (Web platform, PHP-based)
- Admin privileges required
- Access to OAuth configuration settings

### Initial Access Requirements

- Valid admin credentials for Nextcloud
- Direct network access to the Nextcloud web interface
- No prior access needed beyond authentication

## Detailed Attack Procedures

### Step 1: Payload Injection
procedure: [[procedures/Inject-Malicious-JavaScript-into-Nextcloud-OAuth-Redirect-URI]]

**Objective**: Inject a malicious JavaScript payload into the OAuth redirect URI field as an admin, exploiting lack of input sanitization to store the XSS.

**Instructions**: Log in as admin, navigate to OAuth settings, and submit a payload like `javascript:alert('XSS')` or more advanced `<script>alert(document.cookie)</script>` in the redirect URI field. Use browser dev tools to encode if necessary.

**Expected Output**: Payload saved without error; field reflects the injected script when viewed.

**Success Indicators**:
- No validation error on submission
- Payload visible in stored configuration

### Step 2: Trigger Execution
procedure: [[procedures/Trigger-Stored-XSS-Execution-via-OAuth-URI-Access]]

**Objective**: Access or display the OAuth redirect URI to execute the stored JavaScript in the victim's browser context.

**Instructions**: As a user or admin, initiate an OAuth flow or directly access the URI endpoint (e.g., via browser navigation to the configured redirect path). The unsanitized URI triggers script execution.

**Expected Output**: JavaScript alert or console log fires, demonstrating code execution.

**Success Indicators**:
- Script executes (e.g., alert pops or cookie access logged)
- No server-side blocking observed

## Attack Chain Summary

### Key Achievements

1. Persistent storage of malicious JS in OAuth configuration
2. Execution of arbitrary code in user browser context upon URI access
3. Potential for session hijacking or data theft, limited by admin injection requirement

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
