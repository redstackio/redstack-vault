---
id: proc-discover-path-traversal-1245165
tags:
  - path-traversal
  - client-side
  - discovery
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1083.002]]'
updated_at: '2025-12-14T17:26:21.936Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1083.002]]'
---
# Discover Client-Side Path Traversal in Color Scheme Parameter

## Summary

This procedure identifies a client-side path traversal vulnerability in the color_scheme GET parameter of the Acronis Cloud Management Console, where JavaScript unsafely appends the parameter to CSS URLs, allowing manipulation of resource paths.

## Description

In the Acronis Cloud Management Console, the color_scheme parameter is used to load theme-specific CSS files via JavaScript that constructs URLs like /mc/theme.[color_scheme].css. Without sanitization, attackers can inject traversal sequences (e.g., '../') to escape the intended directory and point to arbitrary paths on the same domain. This sets the stage for chaining with other vulnerabilities like open redirects. The target environment is a web application, requiring browser access. Expected outcomes include confirmation of path manipulation through network requests.

## Requirements

1. Access to a browser with developer tools
2. Valid session to the Acronis Cloud Management Console (no login required for initial discovery)
3. Network connectivity to https://mc-beta-cloud.acronis.com

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all client-side path inputs in JavaScript (e.g., use basename extraction or allowlists)
- Implement Content Security Policy (CSP) to restrict CSS loading to trusted paths
- Monitor for anomalous CSS requests in server logs

## Objectives

1. Confirm lack of input sanitization in color_scheme handling
2. Demonstrate path overwrite capability
3. Identify potential chaining opportunities

## Instructions

### Step 1: Access Target with Test Parameter

**Context**: Visit the management console URL with a crafted color_scheme to trigger JavaScript CSS loading.

Use browser developer tools to inspect the page source and network tab.

Navigate to: https://mc-beta-cloud.acronis.com/mc/?color_scheme=../test

> Open the Network tab in developer tools before loading the page to capture requests.

### Step 2: Inspect JavaScript and Test Traversal

**Context**: Analyze the appended parameter in the CSS URL construction.

In the Console tab, search for 'color_scheme' in the JavaScript code. Test traversal by changing the parameter to '../../' and reload.

Observe requests like: https://mc-beta-cloud.acronis.com/test.css?v=24.0.10942

> Successful traversal shows the path escaping /mc/theme/, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1083.002]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- path-traversal
- client-side
- discovery
