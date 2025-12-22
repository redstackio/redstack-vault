---
id: proc-trigger-xss
tags:
  - xss-trigger
  - javascript-execution
  - clickjacking
type: procedure
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
updated_at: '2025-12-14T03:16:08.179Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Uber-Mirror-Page

## Summary

This procedure triggers the stored XSS by visiting the mirrored package page on archive.uber.com and clicking the malicious link, executing the injected JavaScript in the user's browser context.

## Description

After mirroring, the Uber page renders the metadata as HTML anchors with javascript: URIs, which execute on click due to lack of sanitization. This affects all browsers and can be chained with more harmful payloads like keyloggers or credential theft. The attack is persistent as the package remains on PyPI and the mirror. No special tools are needed beyond a browser; impacts any visitor who clicks the link.

## Requirements

1. Access to the mirrored page URL
2. Standard web browser
3. Package synced on mirror

## Defense

Defensive measures and detection strategies:

- Browser-side protections like XSS auditors or safe browsing
- Server-side: Validate and rewrite all href attributes to block javascript:
- User training to avoid clicking suspicious links on package pages

## Objectives

1. Execute arbitrary JavaScript in victim browser
2. Demonstrate impact of stored XSS on public mirrors
3. Highlight risks of unsanitized metadata rendering

## Instructions

### Step 1: Access Mirrored Page

**Context**: Load the page containing the rendered metadata.

Open http://archive.uber.com/pypi/simple/ignore-me-1.0/ in a browser.

> The page displays links for home_page and download_url.

### Step 2: Click Malicious Link

**Context**: Interact with the injected URI to trigger execution.

Click the link labeled '1 home_page' or similar.

> This executes alert(0), popping an alert dialog; replace with real payload for further exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- execution
- browser
