---
id: proc-khan-identify-flash-endpoint
tags:
  - recon
  - flash
  - swf
  - endpoint-discovery
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
updated_at: '2025-12-14T03:16:25.445Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable Flash SWF Endpoint

## Summary

This procedure involves manually inspecting a web application's assets to locate Flash SWF files and identify parameters vulnerable to injection, such as the 'iceID' in cozimo.swf on smarthistory.khanacademy.org.

## Description

In legacy web applications using Adobe Flash, SWF files often process URL parameters without proper sanitization, leading to XSS opportunities. This step targets the discovery of such endpoints by examining publicly accessible Flash resources. The target environment is a web platform with Flash integration, and success enables payload crafting for client-side execution. Prerequisites include basic web browsing and knowledge of Flash parameter handling.

## Requirements

1. Access to a web browser for manual inspection
2. Knowledge of the target subdomain (e.g., smarthistory.khanacademy.org)
3. No special credentials; public access suffices

## Defense

Defensive measures and detection strategies:

- Disable Adobe Flash globally via browser settings or extensions
- Implement Content Security Policy (CSP) to block inline JavaScript execution
- Monitor for anomalous Flash file requests in web server logs

## Objectives

1. Locate the specific SWF file URL
2. Confirm parameter processability
3. Prepare for injection testing

## Instructions

### Step 1: Examine Target Site Assets

**Context**: Browse the target site to identify Flash-based resources, focusing on asset directories.

Inspect the URL http://smarthistory.khanacademy.org/assets/flash/cozimo.swf directly in a browser.

> Loading the SWF should display the Flash content; note any query parameters like 'iceID' in related links or source inspection.

### Step 2: Test Parameter Injection

**Context**: Append a simple test value to the 'iceID' parameter to observe if it's processed by the Flash application.

Access http://smarthistory.khanacademy.org/assets/flash/cozimo.swf?iceID=test in the browser.

> Expected output: The Flash application loads and may display or use the 'test' value, indicating lack of sanitization and potential for string context breakout.

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
- [[flash]]
- [[swf]]
