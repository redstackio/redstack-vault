---
id: proc-access-filecloud-public
tags:
  - access-control-bypass
  - unauthenticated-access
  - filecloud
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.219Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-FileCloud-Public-Mode-Endpoint

## Summary

This procedure exploits improper access control in FileCloud by using a 'public' mode parameter and hash fragment to bypass authentication and access the file management UI for a shared directory.

## Description

In vulnerable FileCloud deployments, the endpoint /ui/core/index.html accepts a mode=public parameter, combined with a hash fragment targeting a shared path (e.g., #expl-tabl./SHARED/rpchllmd/CSAT), allowing unauthenticated entry into the file explorer. This grants read/write capabilities without login, enabling further actions like directory creation and file uploads. The vulnerability stems from unenforced authentication in public mode and no initial validation on shared paths.

## Requirements

1. Web browser with JavaScript enabled
2. Direct HTTP/HTTPS access to the FileCloud server (e.g., https://target.mil)
3. Knowledge of the shared directory path (e.g., /SHARED/rpchllmd/CSAT)

## Defense

Defensive measures and detection strategies:

- Enforce authentication on all endpoints, including public mode parameters
- Implement path validation to restrict access to legitimate shared folders
- Monitor for anomalous UI accesses from unauthenticated IPs using web application firewalls (WAF)
- Log and alert on directory creations or uploads in shared paths

## Objectives

1. Gain unauthenticated access to the FileCloud file management interface
2. Expose shared directories for manipulation
3. Enable subsequent persistence and execution actions

## Instructions

### Step 1: Construct and Navigate to Vulnerable URL

**Context**: Build the URL with the public mode bypass to load the UI without authentication.

No command required; use browser navigation.

Navigate to: https://████/ui/core/index.html?mode=public#expl-tabl./SHARED/rpchllmd/CSAT

> This loads the FileCloud UI directly into the shared directory view. Expected output: Interface renders with file explorer tools available, no login prompt.

### Step 2: Verify Access

**Context**: Confirm the bypass by interacting with the UI elements.

No command required.

Attempt to browse the directory contents.

> Successful access shows files/folders without errors. If redirected to login, the bypass failed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-control-bypass
- unauthenticated-access
- filecloud
