---
tags:
  - admin-access
  - preview-trigger
  - revive-adserver
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:41.646Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e7f071c8-9544-4d7a-ace5-36ab0abb54a5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Login-as-Admin-and-Generate-Affiliate-Preview

## Summary

This procedure involves logging in as an administrator to Revive Adserver and generating an affiliate preview that renders the previously stored malicious URL, setting the stage for XSS execution.

## Description

Administrators have privileges to preview affiliate content, which pulls and renders stored website URLs without proper output encoding. This procedure assumes the payload is already injected and focuses on triggering the vulnerable rendering path via affiliate-preview.php, exploiting the open redirect and stored XSS.

## Requirements

1. Valid administrator credentials
2. Previously injected payload in the system
3. Direct URL access to admin interfaces

## Defense

Defensive measures and detection strategies:

- Enforce role-based access controls to limit preview access
- Sanitize outputs in preview generation scripts
- Log all admin preview actions for anomaly detection
- Implement URL validation to block JavaScript attributes

## Objectives

1. Elevate to admin context for privileged actions
2. Render stored payload in vulnerable context
3. Prepare for interaction-based trigger

## Instructions

### Step 1: Authenticate as Admin

**Context**: Switch to elevated privileges.

Log out of any existing session and log in with admin credentials.

> Admin dashboard appears with full access.

### Step 2: Navigate to Affiliate Preview

**Context**: Load the preview endpoint.

Directly access: `http://localhost/hackerone/www/admin/affiliate-preview.php?codetype=invocationTags%3AoxInvocationTags%3Aspc&block=0&blockcampaign=0&target=&source=&withtext=0&charset=&noscript=1&ssl=0&comments=0&affiliateid=1&submitbutton=Generate`.

> The page generates content including the injected banner.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[admin-access]]
- [[preview-trigger]]
- [[revive-adserver]]
