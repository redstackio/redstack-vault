---
id: proc-zaption-trigger-recent-001
tags:
  - xss
  - passive-trigger
  - listings
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
updated_at: '2025-12-14T03:15:27.013Z'
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
# Trigger XSS via Zaption Recent Tours Listing

## Summary

This procedure passively triggers the stored XSS by viewing the 'Recent Tours' section, where the malicious title is automatically listed and rendered, executing JavaScript without user input.

## Description

The recent tours listing in Zaption's gallery fetches and displays recent items without sanitization, making it a zero-interaction vector. Any user loading the page executes the payload, ideal for broad impact like defacement or data exfiltration. This exploits the stored persistence for ongoing attacks.

## Requirements

1. Injected XSS payload in a recent video/tour
2. Access to Zaption gallery recent tours page
3. Web browser

## Defense

Defensive measures and detection strategies:

- Apply output encoding to all listing components
- Regularly audit recent/popular content for injections
- Use server-side rendering with strict HTML parsers to strip scripts

## Objectives

1. Load the recent tours section
2. Render the malicious item in the listing
3. Achieve automatic JS execution on page view

## Instructions

### Step 1: Navigate to Recent Tours

**Context**: Access the gallery's recent tours view to load listings.

Go to https://www.zaption.com/gallery and scroll or click to the 'Recent Tours' section.

### Step 2: Observe Rendering

**Context**: The page loads recent items, including the injected one, triggering the payload.

As the section renders, the title HTML is inserted, executing the `<img src=x onerror=...>` on DOM insertion.

No typing or clicking needed.

> The alert should appear instantly upon loading.

### Step 3: Test Global Impact

**Context**: Verify execution in a clean session.

Open an incognito window or another account and reload the recent tours page.

**Expected Output**: Consistent JS execution across sessions.

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
- recent-tours
- auto-execution
