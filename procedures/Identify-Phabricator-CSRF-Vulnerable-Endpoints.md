---
tags:
  - csrf
  - recon
  - phabricator
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:23.247Z'
sub_techniques: []
id: ae1104d6-49b8-4605-aad4-8396d9c6ef50
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Phabricator-CSRF-Vulnerable-Endpoints

## Summary

This procedure involves reconnaissance to identify CSRF-vulnerable endpoints in Phabricator's dashboard panel rendering, specifically those lacking anti-CSRF tokens for state-changing requests.

## Description

Phabricator's dashboard panels use endpoints like /dashboard/panel/render/[ID]/ to render and modify content. Without CSRF tokens, these can be exploited to force authenticated users to perform actions such as reconfiguring panels, potentially leading to data exposure or account manipulation. This procedure focuses on manual inspection to pinpoint unprotected paths, assuming access to a Phabricator instance for testing.

## Requirements

1. Access to a Phabricator instance (tester or target environment)
2. Browser with developer tools (e.g., Chrome DevTools) for network monitoring
3. Basic knowledge of HTTP requests and Phabricator's dashboard functionality

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Monitor for anomalous POST requests to dashboard endpoints from unexpected referers
- Enable logging of user actions on panels to detect unauthorized changes

## Objectives

1. Locate endpoints that modify application state without token validation
2. Document vulnerable paths for targeted exploitation
3. Assess potential impact on authenticated users

## Instructions

### Step 1: Inspect Dashboard Interactions

**Context**: Load the Phabricator dashboard and interact with panels to capture requests.

Open browser developer tools (Network tab) and navigate to the dashboard. Modify a panel (e.g., add or edit) and observe the POST requests.

**Expected Output**: Requests to /dashboard/panel/render/[ID]/ without CSRF token parameters.

### Step 2: Validate Lack of Protection

**Context**: Test if requests can be replayed without authentication tokens.

Copy a captured request and attempt to send it via a tool like curl or Postman from a different origin. Check if it succeeds without a CSRF token.

For example, using a simple curl test (adapt to actual payload):

```bash
curl -X POST https://target-phabricator.com/dashboard/panel/render/12/ \
  -d "action=reconfigure" \
  -d "new_setting=test" \
  -H "Cookie: session=valid_session_cookie"
```

> This command simulates the request; success indicates no CSRF protection.

**Expected Output**: Server accepts the request and applies the change.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Reconnaissance]]
- [[web]]
