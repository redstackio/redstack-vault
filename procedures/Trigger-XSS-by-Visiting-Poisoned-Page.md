---
tags:
  - xss
  - dom-xss
  - json-injection
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: e7f63761-3e31-4501-8cb9-f1ad2b44299b
created_at: '2025-12-13T09:00:34.675Z'
updated_at: '2025-12-13T09:00:34.675Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS by Visiting Poisoned Page

## Summary

This procedure triggers the DOM-based XSS by loading the poisoned page, where client-side JavaScript fetches and injects malicious JSON without proper escaping.

## Description

After cache poisoning, visiting the affected page causes JavaScript to fetch JSON from the attacker-controlled URL and insert it into the DOM, enabling HTML injection and script execution. This is a stored XSS via cache poisoning, affecting multiple users.

## Requirements

1. Web browser
2. Access to the poisoned URL
3. Cache already poisoned from prior step

## Defense

Defensive measures and detection strategies:

- Escape user-controlled data before DOM insertion
- Validate fetched resource URLs
- Monitor for unexpected script executions in browser logs

## Objectives

1. Load the poisoned content
2. Trigger JSON fetch and injection
3. Set up for payload execution

## Instructions

### Step 1: Navigate to Poisoned URL

**Context**: Open the URL in a browser to execute the vulnerable JavaScript.

> Visit https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6 in your web browser. The script will fetch the malicious JSON and inject it.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Web-Browser]]

## Tags

- xss
- dom-xss
