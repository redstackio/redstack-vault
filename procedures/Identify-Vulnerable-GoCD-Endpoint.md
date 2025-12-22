---
id: proc-uuid-1
tags:
  - csrf
  - recon
  - gocd
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.757Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable GoCD Endpoint

## Summary

This procedure involves analyzing the GoCD admin endpoint for CSRF protection deficiencies, confirming it allows unauthorized POST requests to modify the cruise-config.xml file.

## Description

In a GoCD environment, the endpoint /go/admin/restful/configuration/file/POST/xml lacks robust CSRF tokens, enabling attackers to forge requests from a victim's browser. This step focuses on reconnaissance to validate the vulnerability without exploitation, typically done by reviewing API docs, source code, or testing with tools like browser dev tools. Prerequisites include access to GoCD documentation or a test instance; outcomes confirm the attack vector for subsequent steps.

## Requirements

1. Access to GoCD documentation or a running instance for inspection
2. Basic knowledge of web security and HTTP requests
3. Browser developer tools or proxy like Burp Suite for request analysis

## Defense

Defensive measures and detection strategies:

- Implement strict CSRF tokens on all state-changing endpoints
- Use Content-Security-Policy (CSP) headers to restrict form submissions
- Monitor for anomalous POST requests to admin endpoints from unexpected referers

## Objectives

1. Confirm absence of CSRF protection on the config upload endpoint
2. Document the exact request format for payload crafting
3. Identify any partial mitigations like same-origin checks

## Instructions

### Step 1: Review Endpoint Documentation

**Context**: Examine official GoCD API docs or source code to understand the POST /xml endpoint's security model.

Search for endpoint details in GoCD admin guide.

> Expected: No mention of CSRF tokens; endpoint accepts XML payloads for config updates.

### Step 2: Test with Browser Tools

**Context**: Simulate a legitimate request to inspect headers and protections.

Open browser dev tools, navigate to GoCD admin, and attempt a config upload while monitoring Network tab.

> Expected: POST request lacks CSRF token in headers or body; confirm it succeeds without additional auth.

### Step 3: Validate Vulnerability

**Context**: Attempt a benign forged request from another origin to test CSRF.

Craft a simple HTML form targeting the endpoint and load it in a new tab.

> Expected: If request processes without error, vulnerability confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[gocd]]
- [[web-recon]]
