---
tags:
  - xss
  - web
  - confluence
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
updated_at: '2025-12-14T03:16:02.546Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 4159f5cc-ca39-4afc-a416-f3ff9b53d745
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-TopCoder-Bookmark-Creation-Endpoint

## Summary

This procedure outlines navigating to the vulnerable bookmark creation endpoint in the TopCoder wiki, setting the stage for injecting a malicious payload in a stored XSS attack.

## Description

The TopCoder wiki, built on Atlassian Confluence, exposes a social bookmarking plugin at /plugins/socialbookmarking/updatebookmark.action. This endpoint accepts user input for bookmarks without proper validation, allowing storage of malicious javascript: URIs. Attackers with wiki access can reach this form to begin exploitation, targeting authenticated or public wiki pages where victims may view the content.

## Requirements

1. Valid TopCoder wiki account for authentication
2. Web browser with internet access
3. Knowledge of the target wiki URL: https://apps.topcoder.com/wiki/

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit bookmark creation to trusted users
- Monitor wiki edit logs for suspicious URL patterns like javascript:
- Use Content Security Policy (CSP) to block inline JavaScript execution

## Objectives

1. Gain access to the bookmark creation form
2. Prepare for payload injection without triggering client-side validation
3. Ensure the endpoint is reachable and functional

## Instructions

### Step 1: Authenticate to Wiki

**Context**: Log in to ensure access to creation features.

Navigate to https://apps.topcoder.com/wiki/ and sign in with valid credentials.

> Successful login redirects to the dashboard, confirming access.

### Step 2: Navigate to Endpoint

**Context**: Directly access the bookmark creation page to load the form.

Enter the URL https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action in the browser address bar.

> The form loads with fields for title, URL, and description.

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
