---
tags:
  - recon
  - headers
  - web-security
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:12.640Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c3009c26-7fb0-4e7c-8410-66cd147faf78
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Inspect-Web-Security-Headers

## Summary

This procedure involves manually inspecting HTTP response headers of a web application to detect missing security protections like CSP and X-Frame-Options, which can expose the site to clickjacking attacks.

## Description

In a typical attack scenario, an attacker targets public-facing web applications lacking frame protections. By examining headers using browser developer tools, the absence of CSP's frame-ancestors directive (e.g., 'self') or X-Frame-Options (e.g., DENY or SAMEORIGIN) is confirmed, allowing arbitrary embedding in iframes. This procedure is a prerequisite for demonstrating UI redressing and requires only browser access to the target URL.

## Requirements

1. Web browser with developer console (e.g., Chrome DevTools)
2. Public access to the target URL (e.g., https://etherscamdb.info)
3. Basic knowledge of HTTP headers

## Defense

Defensive measures and detection strategies:

- Implement CSP with frame-ancestors 'self' to restrict framing
- Set X-Frame-Options to DENY or SAMEORIGIN
- Monitor server logs for unusual iframe embedding attempts

## Objectives

1. Confirm vulnerability to clickjacking by identifying missing headers
2. Gather evidence for reporting or exploitation POC
3. Assess overall header security posture

## Instructions

### Step 1: Access Target and Open DevTools

**Context**: Navigate to the target site and prepare to inspect network traffic.

Open your browser and visit the target URL, such as https://etherscamdb.info. Right-click and select 'Inspect' or press F12 to open developer tools. Switch to the Network tab.

### Step 2: Reload and Examine Headers

**Context**: Capture and review the HTTP response headers for frame protections.

Reload the page (Ctrl+R or Cmd+R) to trigger a network request. Click on the main document request in the Network tab, then view the Response Headers section. Search for 'Content-Security-Policy' and 'X-Frame-Options'.

> Expected output: Headers list without CSP or X-Frame-Options, e.g., no line like 'Content-Security-Policy: frame-ancestors 'self';'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web-security]]
