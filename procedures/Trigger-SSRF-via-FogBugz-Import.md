---
id: proc-uuid-005
name: Trigger-SSRF-via-FogBugz-Import
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.879Z'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - ssrf
  - blind-ssrf
  - gitlab
  - fogbugz
  - import
commands: []
platforms:
  - Web
  - Docker
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Trigger-SSRF-via-FogBugz-Import

## Summary

This procedure exploits the blind SSRF vulnerability by entering an internal localhost URL in GitLab's FogBugz project import interface, resulting in an unauthorized request to internal services.

## Description

The FogBugz import feature lacks URL validation, allowing inputs like 'http://localhost:12345' to trigger requests from the GitLab server to internal endpoints. This can expose sensitive data or enable further attacks. The procedure uses the GitLab UI after environment setup and listener activation.

## Requirements

1. Running GitLab instance accessible via web browser
2. Active netcat listener on port 12345 in the container
3. Basic user access to GitLab (no special privileges needed for import)

## Defense

Defensive measures and detection strategies:

- Implement URL allowlisting in import features to block internal/localhost addresses
- Log and monitor outbound requests from application servers
- Use web application firewalls (WAF) to detect SSRF patterns in inputs

## Objectives

1. Trigger an internal request via unvalidated URL input
2. Confirm SSRF success through listener connection
3. Demonstrate potential for internal network compromise

## Instructions

### Step 1: Navigate to FogBugz Import

**Context**: Access the project import section in the GitLab UI to reach the vulnerable URL field.

**Instructions**: Log in to GitLab at http://localhost (default admin/password), go to "New Project" > "Import project" > Select "FogBugz".

### Step 2: Input Malicious URL and Import

**Context**: Enter the SSRF payload in the URL field to force an internal request.

**Instructions**: In the FogBugz URL field, input `http://localhost:12345`. Click "Begin Import" or equivalent to submit.

> The application will attempt to connect to the specified URL internally. Expected outcome: No external error, but connection appears in the netcat listener.

### Step 3: Validate Exploitation

**Context**: Check the listener for confirmation of the SSRF.

**Instructions**: Switch to the netcat terminal; a new connection from the GitLab process (e.g., from PID of the import handler) should be logged.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- blind-ssrf
- gitlab
- fogbugz
- import
