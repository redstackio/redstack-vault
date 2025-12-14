---
id: proc-verify-xframe-header
name: Verify Missing X-Frame-Options Header
tags:
  - clickjacking
  - headers
  - web
  - recon
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:05.137Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Verify Missing X-Frame-Options Header

## Summary

This procedure involves inspecting the HTTP response headers of a target website to detect the absence of the X-Frame-Options header, which is a security mechanism to prevent clickjacking by blocking iframe embedding.

## Description

In this attack scenario, an attacker visits the target website (e.g., https://kubernetes.io/) and uses browser developer tools to examine the response headers. The lack of X-Frame-Options allows the site to be framed in iframes, enabling UI redressing attacks where users can be tricked into clicking hidden elements. This is a reconnaissance step to confirm vulnerability before demonstration. Expected outcomes include header confirmation and preparation for exploitation testing. Prerequisites include a modern web browser with developer tools enabled.

## Requirements

1. Web browser with developer tools (e.g., Chrome, Firefox)
2. Internet access to the target URL
3. No special permissions or tools needed

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options header with value 'DENY' or 'SAMEORIGIN' on all responses
- Use Content-Security-Policy (CSP) frame-ancestors directive to restrict framing
- Monitor for anomalous iframe embeddings via web application firewall (WAF) logs

## Objectives

1. Confirm the site's susceptibility to iframe embedding
2. Identify potential for clickjacking attacks
3. Gather evidence for vulnerability reporting

## Instructions

### Step 1: Navigate to Target and Open Developer Tools

**Context**: Access the target website and prepare to inspect network traffic.

Open your web browser and navigate to https://kubernetes.io/. Right-click on the page and select 'Inspect' or press F12 to open developer tools. Switch to the 'Network' tab.

> This loads the site and prepares for header inspection.

### Step 2: Reload and Inspect Response Headers

**Context**: Capture and examine the HTTP response to check for the X-Frame-Options header.

Reload the page (Ctrl+R or Cmd+R) to trigger a fresh request. In the Network tab, click on the main document request (e.g., the root URL). Scroll to the 'Response Headers' section and search for 'X-Frame-Options'.

> Expected output: No X-Frame-Options entry, confirming the vulnerability. If present with 'DENY', the site is protected.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[web-recon]]
