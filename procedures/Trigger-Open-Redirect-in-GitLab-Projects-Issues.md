---
id: proc-gitlab-issues-redirect
name: Trigger Open Redirect in GitLab Projects Issues
tags:
  - open-redirect
  - phishing
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-gitlab-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:23.470Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
# Trigger Open Redirect in GitLab Projects Issues

## Summary

This procedure exploits an open redirect vulnerability in GitLab's Projects::IssuesController by manipulating the 'host' parameter in the redirect_to call, allowing unauthenticated users to be redirected to arbitrary external sites for phishing.

## Description

The issue occurs at line 32 of Projects::IssuesController where redirect_to params.merge(...) lacks validation for the 'host' parameter. Attackers can use URLs like /projects/issues?page=99999999&host=www.evil.com to redirect visitors without needing authentication. This broadens the attack surface for phishing, as anyone can be tricked into clicking the link, leading to potential credential harvesting or drive-by downloads on the malicious site.

## Requirements

1. Access to a vulnerable GitLab instance (pre-8.11.0 versions)
2. No authentication required for the issues endpoint
3. Network connectivity to the GitLab server
4. Browser or curl for testing

## Defense

Defensive measures and detection strategies:

- Enforce host validation in redirect logic (e.g., restrict to gitlab.com domains)
- Log and alert on redirect attempts with external hosts
- Deploy rate limiting on issue/project endpoints
- Educate users on verifying URLs before clicking

## Objectives

1. Redirect unauthenticated visitors to a phishing site via GitLab's issues page
2. Exploit lack of parameter sanitization in Rails controllers
3. Enable mass phishing without session requirements

## Instructions

### Step 1: Identify Target Endpoint

**Context**: Confirm the issues controller is accessible without login.

Visit https://gitlab.example.com/projects/issues directly to ensure no auth prompt.

### Step 2: Craft Malicious URL

**Context**: Append manipulated parameters to trigger the redirect.

**Command** ([[commands/curl-test-gitlab-redirect]]):
```bash
curl -L -v "https://gitlab.example.com/projects/issues?page=99999999&host=www.evil.com"
```

> The command traces the redirect (-L) and verbose logs (-v) show the Location header to the evil site. No cookie needed due to unauthenticated access.

### Step 3: Test in Browser

**Context**: Simulate phishing by sharing the URL.

Open the URL in a browser: https://gitlab.example.com/projects/issues?page=99999999&host=www.evil.com. It should auto-redirect to the external site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[T1566.002]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-gitlab-redirect]]

## Tools Used


## Tags

- open-redirect
- phishing
- gitlab
