---
id: proc-trigger-xss-safari
tags:
  - trigger
  - xss
  - safari
  - login-flow
type: procedure
tools:
  - '[[tools/Safari-Browser]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:28.872Z'
skill_level: intermediate
impact_level: low
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Safari-Login

## Summary

This procedure initiates the OIDC login flow in Safari to exploit the stored XSS, where the malicious authorization_endpoint injects HTML/JS into the meta refresh response due to unescaped concatenation in LoginController.php.

## Description

Safari's user agent triggers a workaround in the code that generates a meta refresh tag with the raw, unvalidated URL from the stored discovery document. The payload breaks out of the content attribute, injecting <svg onload=alert(document.domain)>, rendering HTML and attempting JS execution. CSP (default-src 'self') blocks inline scripts, limiting impact to visual injection or potential phishing, but confirms the vuln.

## Requirements

1. Configured malicious OIDC provider
2. Safari browser (user agent matching /Safari/ but not /Chrome/)
3. Access to Nextcloud login page

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP with no inline allowances and report-only mode for monitoring
- HTML-encode all dynamic content in responses (e.g., use OWASP ESAPI or native PHP functions)
- Log and alert on anomalous user agents or login redirects in Nextcloud access logs

## Objectives

1. Trigger the Safari-specific response path
2. Execute the injected payload in the login page
3. Observe limited XSS effects despite CSP

## Instructions

### Step 1: Open Login in Safari

**Context**: Start the authentication flow.

**Instructions**: Launch Safari, navigate to http://localhost:8081/login, and select the malicious OIDC provider to initiate login.

> Expected output: Redirect or response page with meta refresh tag.

### Step 2: Observe Injection

**Context**: Inspect the generated response for payload execution.

**Instructions**: View page source; look for injected <meta http-equiv="refresh" content="0; url='" http-equiv=><svg/onload=alert(document.domain)>?client_id=..." />. Check if alert fires or SVG renders.

> Expected output: Malformed meta tag with injected attributes; alert may pop if CSP permits, otherwise HTML injection visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Safari-Browser]]

## Tags

- [[trigger]]
- [[xss]]
- [[safari]]
- [[login-flow]]
