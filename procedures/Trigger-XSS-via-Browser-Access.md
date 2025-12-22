---
id: proc-trigger-xss-browser
tags:
  - xss-trigger
  - browser-execution
type: procedure
tools:
  - '[[tools/browser]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Browser
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.492Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Browser-Access

## Summary

This procedure accesses the vulnerable /scrap endpoint in a browser, causing metascraper to extract and render the injected script, executing the XSS payload.

## Description

Visiting http://127.0.0.1:8888/scrap triggers the scrape, inserts the unsanitized <script> from metadata.publisher, loads malware.js, and runs the alert. Demonstrates impact in a victim browser context. Prerequisites: Servers running on 8080 and 8888.

## Requirements

1. Running static server (port 8080)
2. Running Express app (port 8888)
3. Modern web browser

## Defense

Defensive measures and detection strategies:

- Enable XSS protection headers (X-XSS-Protection, CSP)
- Sanitize all dynamic HTML insertions
- Detect and block cross-origin script loads

## Objectives

1. Execute the injected JavaScript
2. Validate payload delivery via alert
3. Confirm arbitrary code execution

## Instructions

### Step 1: Access the Endpoint in Browser

**Context**: Load the URL to trigger scraping and rendering.

No command; open in browser:

Visit: http://127.0.0.1:8888/scrap

> The page renders with the script tag, loading http://127.0.0.1:8080/malware.js and executing the alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/browser]]

## Tags

- [[xss-trigger]]
- [[browser-execution]]
