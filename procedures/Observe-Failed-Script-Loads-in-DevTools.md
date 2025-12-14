---
tags:
  - reconnaissance
  - devtools
  - network-analysis
type: procedure
tools:
  - '[[tools/DevTools]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/observe-failed-script-load]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:56:19.820Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 05cb000e-1830-44be-ad1f-2c6539496796
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Observe-Failed-Script-Loads-in-DevTools

## Summary

This procedure uses browser DevTools to inspect network requests after payload injection, identifying failed script loads redirected by the <base> tag to confirm the CSP bypass setup in the GitLab XSS attack.

## Description

Post-injection, reloading the page causes GitLab's relative script URLs to resolve against the attacker domain, resulting in 404s visible in the network tab. This validates the injection without executing payloads yet and helps map required asset paths for hosting. Targets modern browsers on GitLab.com.

## Requirements

1. Injected issue page loaded
2. Browser with DevTools (Chrome/Firefox)
3. Attacker domain configured but not yet hosting files

## Defense

Defensive measures and detection strategies:

- Log and alert on cross-origin resource failures
- Sanitize to prevent <base> tag persistence
- Use SRI for critical scripts to block tampered loads

## Objectives

1. Confirm redirection of relative URLs
2. Identify specific failing asset paths
3. Validate injection success pre-exploitation

## Instructions

### Step 1: Open DevTools and Reload Page

**Context**: Inspect the page to capture network activity.

**Command** ([[commands/observe-failed-script-load]]):

Press F12 to open DevTools, go to Network tab, then reload (Ctrl+R).

> Filter for JS files. Expected: Requests like http://attacker.com/assets/webpack/hello.4948f350.chunk.js failing with 404.

### Step 2: Note Failing Paths

**Context**: Document paths for server setup.

**Command** ([[commands/observe-failed-script-load]]):

Copy URLs from failed requests.

> Examples include top_nav.c9763726.chunk.js for wikis. Expected: List of GitLab-mimicked paths.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/observe-failed-script-load]]

## Tools Used

- [[tools/DevTools]]

## Tags

- network-inspection
- validation
