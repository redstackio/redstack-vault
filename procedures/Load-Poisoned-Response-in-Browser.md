---
id: proc-smule-load-poisoned-001
name: Load-Poisoned-Response-in-Browser
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.356Z'
tactics: []
techniques: []
sub_techniques: []
tags:
  - web-cache-poisoning
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
---

# Load-Poisoned-Response-in-Browser

## Summary

This procedure simulates a victim accessing the poisoned cached page by saving and loading the HTML response in a browser, verifying that links are rewritten to the attacker-controlled host without raising suspicion.

## Description

After poisoning the cache, the response is saved as an HTML file and opened locally in a browser. The page renders normally, but embedded links (e.g., for login or actions) point to the attacker's localhost server. This step confirms the poisoning works in a browser context, setting up for victim simulation where interactions leak data.

## Requirements

1. Saved poisoned HTML response from previous step
2. Modern web browser (e.g., Firefox, Chrome)
3. Local attacker server running to handle redirects

## Defense

Defensive measures and detection strategies:

- Use Content-Security-Policy (CSP) to restrict navigations to trusted origins
- Cache responses with integrity checks or signed URLs
- Log and alert on cache hits with anomalous content

## Objectives

1. Verify poisoned page loads without errors
2. Confirm redirects occur to attacker host on interaction
3. Prepare for data disclosure simulation

## Instructions

### Step 1: Save Response

**Context**: Export the poisoned HTML from the proxy tool.

No command; right-click in Burp Suite and save response as .html.

> Expected output: Local HTML file with localhost links.

### Step 2: Open in Browser

**Context**: Load the file to simulate victim access.

No command; open file://path/to/poisoned.html in browser.

> Page should appear as normal Smule group page. Click links to verify redirects to localhost.

### Step 3: Interact to Test

**Context**: Attempt a benign action to confirm poisoning.

No command; hover or click non-sensitive links.

> Expected output: Links resolve to http://localhost/ paths.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-cache-poisoning]]
