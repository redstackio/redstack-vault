---
id: proc-mapbox-xss-identify
tags:
  - xss
  - reflected-xss
  - template-injection
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:25.085Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Reflected-XSS-in-Access-Token-Parameter

## Summary

This procedure involves inspecting the Mapbox API endpoint to detect a reflected XSS vulnerability in the access_token query parameter, where Underscore.js templates interpolate the value without HTML escaping, allowing potential JavaScript injection.

## Description

In the Mapbox map embed page at api.tiles.mapbox.com/v4/{mapid}/page.html, the access_token is inserted using Underscore's '<%=' syntax, which does not escape HTML. This enables attackers to inject payloads that break out of HTML contexts, particularly in Firefox due to its address bar encoding behavior. The procedure targets public-facing web APIs and requires no authentication, leading to client-side execution risks like session hijacking.

## Requirements

1. Access to a web browser like Firefox for inspection
2. Public URL to Mapbox API endpoint (e.g., api.tiles.mapbox.com)
3. Basic knowledge of HTML templates and XSS vectors

## Defense

Defensive measures and detection strategies:

- Switch to HTML-escaped templates ('<%-') in Underscore.js
- Implement content security policy (CSP) to block inline scripts
- Monitor for anomalous query parameters in API logs

## Objectives

1. Confirm reflection of access_token without escaping
2. Identify browser-specific exploitation opportunities
3. Assess potential for JavaScript injection

## Instructions

### Step 1: Access the Endpoint

**Context**: Load the vulnerable page to examine the source code and identify template usage.

Navigate to: https://api.tiles.mapbox.com/v4/ctswebrequest.m4ga59jd/page.html?access_token=pk.eyJ1IjoiY3Rzd2VicmVxdWVzdCIsImEiOiJTb19VUHM0In0.muGg6tMDG4NOGrV4qQQ8yw

> View page source to locate the '<%=' interpolation for access_token in meta tags or HTML attributes.

### Step 2: Analyze Template

**Context**: Inspect the Underscore.js template rendering to confirm lack of escaping.

Examine the JavaScript source for template definitions using Underscore's _.template function.

> Look for unescaped outputs that reflect query parameters directly into HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[reflected-xss]]
