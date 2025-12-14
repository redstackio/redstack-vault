---
id: proc-gitlab-inject-xss-custom-tracker
tags:
  - xss
  - javascript-uri
  - payload-injection
  - gitlab
type: procedure
tools: []
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
updated_at: '2025-12-14T03:16:31.010Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Custom-Issue-Tracker

## Summary

This procedure exploits the lack of URL scheme validation in GitLab's custom issue tracker to inject a persistent javascript: URI payload into the Project URL field, which executes on the Issues page.

## Description

GitLab's integration model fails to enforce HTTPS/HTTP schemes (regex /\Ahttps?:\///i), allowing javascript: URIs to be stored unsanitized. The payload, e.g., targeting window.gon.api_token, persists and renders as a link, enabling JS execution for token theft and account takeover.

## Requirements

1. Access to Custom Issue Tracker configuration form.
2. Knowledge of GitLab's client-side variables like window.gon.api_token.
3. Web browser developer tools for testing payloads.

## Defense

Defensive measures and detection strategies:

- Implement strict URL validators enforcing only http/https schemes.
- Sanitize all rendered links in issue tracker displays.
- Monitor for javascript: schemes in stored configurations.

## Objectives

1. Store malicious URI without triggering validation.
2. Target sensitive data like API tokens.
3. Ensure persistence for victim triggering.

## Instructions

### Step 1: Prepare Payload

**Context**: Craft a javascript: URI to execute on load or click.

Use a payload like `javascript:alert('Current user API token: ' + window.gon.api_token)` to test; for production, replace alert with exfiltration to an attacker server.

### Step 2: Fill Vulnerable Fields

**Context**: Input the payload into unvalidated URL fields.

In the form, set Project URL to the javascript: payload. Optionally, test Issues URL and New Issue URL with similar inputs.

**Expected Output**: Fields accept the input without errors.

### Step 3: Save Configuration

**Context**: Persist the payload in the backend.

Click "Save changes" to store the integration settings.

**Expected Output**: Success message; no validation rejection.

**Success Indicators**:
- Payload saved.
- No scheme enforcement errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
