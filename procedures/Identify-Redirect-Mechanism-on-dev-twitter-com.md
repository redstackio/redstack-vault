---
id: proc-uuid-001
tags:
  - reconnaissance
  - redirect
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:31.764Z'
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
# Identify-Redirect-Mechanism-on-dev-twitter-com

## Summary

This procedure identifies the HTTP 302 redirect behavior on dev.twitter.com, including fallback page rendering, to uncover inconsistencies exploitable for redirects and XSS.

## Description

The site uses Request-URI to set the Location header in 302 responses. If redirection fails (e.g., invalid URL), a fallback HTML page displays a clickable link to the target. This inconsistency in URI processing across browsers enables chained attacks. Target: Public web app at dev.twitter.com. Expected outcome: Mapping of redirect logic for payload crafting.

## Requirements

1. Browser with dev tools (e.g., Firefox, Chrome)
2. Proxy tool like Burp Suite for response inspection
3. Public access to dev.twitter.com

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation in redirects
- Add Content-Security-Policy to block javascript: schemes
- Monitor for anomalous 302 responses to external domains

## Objectives

1. Confirm 302 redirect mechanism
2. Identify fallback page behavior
3. Note browser-specific rendering differences

## Instructions

### Step 1: Inspect Base Redirect

**Context**: Trigger a simple redirect to observe the mechanism.

Access `https://dev.twitter.com/somepath` in your browser and check the network tab for the 302 response.

Use curl to replicate:

```bash
curl -I 'https://dev.twitter.com/somepath'
```

> This returns a 302 with Location: https://dev.twitter.com/somepath. If invalid, fallback HTML shows <a href="target">target</a>.

### Step 2: Test Fallback Rendering

**Context**: Force fallback by using an invalid URI to see link rendering.

Navigate to a malformed path and inspect the HTML source for the displayed link.

**Expected Output**: Fallback page with unescaped URI in <a> tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[redirect]]
