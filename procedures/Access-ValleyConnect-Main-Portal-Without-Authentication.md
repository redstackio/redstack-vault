---
id: proc-tva-main-portal-bypass
name: Access-ValleyConnect-Main-Portal-Without-Authentication
type: procedure
verified: false
submitted: true
created_at: '2023-10-17T00:00:00Z'
updated_at: '2025-12-14T17:31:52.486Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - auth-bypass
  - web
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Access-ValleyConnect-Main-Portal-Without-Authentication

## Summary

This procedure exploits improper authentication in the TVA ValleyConnect portal by simply visiting the main URL, resulting in a default logged-in state that grants access to internal navigation without credentials.

## Description

The ValleyConnect portal at https://valleyconnect.tva.gov/ fails to enforce authentication checks on the entry point, displaying a session as 'Hello, null' for unauthenticated visitors. This allows immediate navigation to restricted areas like profile and password reset, exposing application internals. The target environment is a public-facing web application using HTTP/2, and no prior access or tools beyond a browser are needed. Expected outcomes include visibility into user-facing features without login.

## Requirements

1. Internet access to https://valleyconnect.tva.gov/
2. Web browser (e.g., Chrome or Firefox)
3. No credentials or special permissions

## Defense

Defensive measures and detection strategies:

- Implement proper session validation on all entry points to redirect unauthenticated users to login.
- Monitor access logs for requests to internal paths from unauthenticated sessions, alerting on 'null' user indicators.

## Objectives

1. Establish unauthorized entry to the portal.
2. Observe default session behavior.
3. Enable navigation to further restricted features.

## Instructions

### Step 1: Navigate to Main Portal

**Context**: Directly access the portal URL to trigger the authentication bypass.

No command required; use a web browser to visit https://valleyconnect.tva.gov/.

> The page loads in under 5 seconds, showing 'Hello, null' and internal menus. If it prompts for login, the bypass may have been patched.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- auth-bypass
- web
