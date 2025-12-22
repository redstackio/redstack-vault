---
id: proc-uuid-1
tags:
  - reconnaissance
  - version-identification
  - jira
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-13T23:52:49.322Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Identify-Outdated-Jira-Version

## Summary

This procedure involves accessing a Jira instance to determine its version, identifying if it is outdated and potentially vulnerable to known exploits like CVE-2018-5230.

## Description

In an attack scenario targeting public-facing Jira installations, such as jira.roblox.com, the first step is to ascertain the software version. This is typically exposed in the page source, footer, or through HTTP headers. For Jira 7.6.3, this version is known to be susceptible to reflected XSS in the issue collector due to inadequate input sanitization. Prerequisites include internet access and a web browser; no special tools are needed for basic identification.

## Requirements

1. Web browser with developer tools enabled.
2. Public access to the target Jira URL (e.g., https://jira.roblox.com).
3. Basic knowledge of web inspection techniques.

## Defense

Defensive measures and detection strategies:

- Regularly update Jira to the latest version and monitor for outdated instances using vulnerability scanners.
- Implement web application firewalls (WAF) to detect version disclosure attempts.

## Objectives

1. Confirm the exact Jira version running on the target.
2. Assess vulnerability to specific CVEs like XSS issues.
3. Establish the foundation for targeted exploitation.

## Instructions

### Step 1: Access the Jira Instance

**Context**: Navigate to the target Jira site to begin inspection.

Open a web browser and visit https://jira.roblox.com. Look for login or issue tracking pages.

> Inspect the page footer or 'About' section for version details, which may display 'Jira 7.6.3'.

### Step 2: Inspect Page Source and Headers

**Context**: Use browser tools to extract hidden version information.

Right-click on the page and select 'View Page Source' or open Developer Tools (F12). Search for 'jira.version' or check HTTP response headers via Network tab.

> Expected output: Version string like '7.6.3' confirming outdated status.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[version-identification]]
