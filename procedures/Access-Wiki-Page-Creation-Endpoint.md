---
id: proc-001
tags:
  - xss
  - recon
  - web
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
updated_at: '2025-12-14T03:16:02.586Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Wiki Page Creation Endpoint

## Summary

This procedure navigates to the TopCoder wiki's page creation endpoint, which is the entry point for exploiting the reflected XSS vulnerability. It ensures the attacker has authenticated access to the interface where payloads can be injected.

## Description

The TopCoder wiki, built on Atlassian Confluence, exposes a page creation feature at https://apps.topcoder.com/wiki/pages/createpage.action. This endpoint requires authentication but does not sanitize inputs, making it vulnerable to reflected XSS. The procedure involves signing in and accessing the URL with the spaceKey parameter to load the form, setting the stage for parameter manipulation.

## Requirements

1. Valid TopCoder credentials for authentication
2. Web browser with JavaScript enabled
3. Network connectivity to https://apps.topcoder.com

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to restrict wiki editing
- Monitor access logs for unusual page creation attempts
- Enable Content Security Policy (CSP) to block inline script execution

## Objectives

1. Gain access to the vulnerable page creation interface
2. Verify authentication and endpoint availability
3. Prepare for payload injection without triggering alerts

## Instructions

### Step 1: Authenticate to TopCoder

**Context**: Sign in to ensure access to restricted wiki features.

Navigate to https://www.topcoder.com/sign-in and enter credentials.

> Upon success, the dashboard loads, confirming authenticated session.

### Step 2: Navigate to Page Creation Endpoint

**Context**: Directly access the wiki creation URL to bypass standard navigation.

Enter the following URL in the browser:

https://apps.topcoder.com/wiki/pages/createpage.action?spaceKey=tcwiki

> The page creation form appears, with fields for parent page and labels, indicating successful access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[Confluence]]
