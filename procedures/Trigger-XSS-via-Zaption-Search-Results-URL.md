---
id: proc-zaption-trigger-results-001
tags:
  - xss
  - url-trigger
  - search-results
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
updated_at: '2025-12-14T03:15:27.015Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS via Zaption Search Results URL

## Summary

This procedure uses a direct URL to the search results endpoint to render the malicious title in the results page, executing the stored XSS payload on load.

## Description

The `/gallery/search?q=` endpoint reflects stored titles in results without encoding, allowing URL-based triggering. This enables attackers to share links that execute JS on victims' browsers upon visit, bypassing search interaction. It leverages the stored nature for persistence and global reach.

## Requirements

1. Injected XSS payload in gallery title
2. Knowledge of the search endpoint URL structure
3. Web browser for URL access

## Defense

Defensive measures and detection strategies:

- Encode all outputs in search results using HTML escaping
- Rate-limit or validate search query parameters server-side
- Deploy CSP headers to block unsafe inline scripts in search pages

## Objectives

1. Access search results via direct URL
2. Render and execute the payload in results listing
3. Enable link-based exploitation

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the search query URL using the payload prefix.

Form the URL: `https://www.zaption.com/gallery/search?q=xyz123`, where `xyz123` matches the injected title.

### Step 2: Access the URL

**Context**: Load the page to trigger rendering of results.

Paste and visit the URL in a browser. The results page displays matching items, injecting the payload into the DOM.

The onerror handler executes immediately.

> Expect the alert to pop up on page load.

### Step 3: Inspect and Confirm

**Context**: Use tools to verify execution and unsanitized output.

Open dev tools, check the Network tab for the search request, and Elements tab for the raw HTML title.

**Expected Output**: JS execution confirmed via alert or console.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- search-url
- direct-trigger
