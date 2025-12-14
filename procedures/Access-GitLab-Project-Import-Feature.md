---
tags:
  - ssrf
  - gitlab
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-import-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.616Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: fe3d322e-e7dc-4901-b006-02d10e063603
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-GitLab-Project-Import-Feature

## Summary

This procedure involves navigating to GitLab's project import interface using the 'Repo by URL' option, setting the stage for SSRF exploitation by accessing the vulnerable URL input field.

## Description

In GitLab, the project import feature allows users to clone external repositories via URL. Due to insufficient validation, this can be abused for SSRF by inputting localhost or internal URLs. The target environment is a GitLab web application, typically running on ports 80 or 443. Prerequisites include a valid user session. Expected outcomes include exposure of the import form, enabling subsequent malicious URL submission.

## Requirements

1. Valid GitLab user account with project creation permissions
2. Access to the GitLab web interface over HTTPS
3. Browser or API client for interaction

## Defense

Defensive measures and detection strategies:

- Implement strict URL whitelisting in import features to block localhost/internal IPs
- Monitor server logs for unusual internal request patterns from application processes
- Use web application firewalls (WAF) to validate input URLs

## Objectives

1. Gain access to the vulnerable import endpoint
2. Prepare for SSRF payload injection
3. Confirm feature availability without triggering alerts

## Instructions

### Step 1: Log In and Navigate to New Project

**Context**: Authenticate and reach the project creation page to access import options.

**Command** ([[commands/curl-send-import-request]]):
```bash
# Optional API login simulation; typically done via UI
curl -X POST 'https://gitlab.example.com/api/v4/session' -d 'login=username&password=pass'
```

> This authenticates the session. In UI, log in manually and click 'New Project' > 'Import project' > 'Repo by URL'.

### Step 2: Select Repo by URL Option

**Context**: Expose the URL input field for repository location.

No specific command; use UI to select the option.

> The form now accepts a URL parameter, which lacks validation for localhost addresses.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-import-request]]

## Tools Used


## Tags

- ssrf
- gitlab
