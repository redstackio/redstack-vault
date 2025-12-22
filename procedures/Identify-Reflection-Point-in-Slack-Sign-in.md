---
tags:
  - xss
  - recon
  - slack
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
updated_at: '2025-12-14T03:15:27.076Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 1f68cf0a-17fb-4924-8fa4-65f1d786b0c7
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify Reflection Point in Slack Sign-in

## Summary

This procedure identifies the reflection point for user-controlled input in Slack's sign-in page title, confirming lack of HTML escaping for subdomains or URL parameters like 'redir' and 'id'.

## Description

In the context of testing Slack's sign-in functionality, this step involves inspecting the HTML source of the sign-in page to locate where inputs are inserted unsanitized into the <title> tag. The vulnerability allows direct reflection, enabling XSS. Prerequisites include access to a browser and the ability to load Slack URLs. Expected outcome is confirmation of the injection point for payload crafting.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Access to Slack workspace sign-in URLs (no authentication needed)
3. Basic knowledge of HTML inspection

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all user inputs in HTML contexts
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous subdomains or parameter values in access logs

## Objectives

1. Confirm reflection of subdomain or parameters in page title
2. Verify absence of sanitization
3. Document the exact insertion point for exploitation

## Instructions

### Step 1: Load Sign-in Page and Inspect Source

**Context**: Access a sample Slack sign-in page to observe input reflection.

Open https://[example-subdomain].slack.com/workspace-signin in a browser. Right-click and select 'View Page Source' or use DevTools (F12) to inspect the <head> section. Look for the <title> tag, e.g., <title>Sign in to [subdomain]</title>.

> Expected output: Unescaped input in title, such as 'Sign in to sshunter.slack.com'.

### Step 2: Test Parameter Reflection

**Context**: Manipulate URL parameters to confirm broader reflection.

Modify the URL with parameters like ?redir=%2Fhelp%2Frequests%2F793043%3Fid%3Dtest and reload. Inspect the title again to see if 'test' or the parameter value reflects without encoding.

> Expected output: Title updates to include the parameter value, e.g., 'Sign in to /help/requests/793043?id=test'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- recon
- web-vuln
