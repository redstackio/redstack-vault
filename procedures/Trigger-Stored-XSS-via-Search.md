---
id: proc-trigger-xss-search-learnboost
tags:
  - xss
  - trigger
  - stored-xss
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
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
updated_at: '2025-12-14T03:47:18.364Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS via Search

## Summary

This procedure triggers the stored XSS payload in LearnBoost by performing a search that retrieves and displays the injected ZIP code data, executing the JavaScript in the attacker's or victim's browser.

## Description

After injection, the unsanitized ZIP code is displayed in search results without proper HTML escaping. Searching for terms like 'fro' loads the school entry, rendering the payload and executing the onerror handler. This can lead to arbitrary code execution, enabling session theft or data exfiltration for any user searching the term.

## Requirements

1. Previously injected payload in the system
2. Access to the search endpoint: https://www.learnboost.com/settings/network/search
3. Web browser for verification

## Defense

Defensive measures and detection strategies:

- Escape HTML entities in all output fields, especially search results
- Implement output encoding for user-generated content
- Log and alert on JavaScript errors or unexpected script executions in search contexts

## Objectives

1. Retrieve and render the stored payload via search
2. Execute JavaScript in the browser context
3. Demonstrate impact through alert or further exploitation

## Instructions

### Step 1: Navigate to Search Endpoint

**Context**: Access the network search feature to query for the injected school.

No command required; in [[tools/Mozilla-Firefox]], visit https://www.learnboost.com/settings/network/search.

> Ensure you are logged in as a user who would perform such a search.

### Step 2: Perform Triggering Search

**Context**: Enter a search term that matches the injected school name prefix to load the vulnerable data.

Enter 'fro' in the search box and submit.

> The results will include the school entry, displaying the ZIP code and triggering the img onerror event to execute alert(document.domain).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mozilla-Firefox]]

## Tags

- xss
- trigger
