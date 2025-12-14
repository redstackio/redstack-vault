---
tags:
  - browser-access
  - xss-trigger
type: procedure
tools:
  - '[[tools/Firefox-ESR]]'
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
updated_at: '2025-12-14T03:46:31.281Z'
sub_techniques: []
id: 22649236-c911-4960-bc17-d4a9c2eb65bb
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Directory-Listing

## Summary

This procedure accesses the served directory listing in a browser, loading the HTML that renders the unsanitized malicious filename and sets up the XSS payload for execution.

## Description

The server's response includes <a> tags with filenames directly interpolated into href and text, without HTML entities. Viewing http://localhost:8080/ in a browser like Firefox ESR parses this as executable HTML, injecting the onmouseover handler.

## Requirements

1. Server running on localhost:8080
2. Web browser installed (e.g., Firefox ESR 52.7.3)
3. Local network access

## Defense

Defensive measures and detection strategies:

- Encode filenames with htmlentities() or equivalent before output
- Disable directory listings or use secure alternatives like Apache with mod_autoindex
- Browser extensions for XSS detection

## Objectives

1. Load the vulnerable page in client context
2. Render the injected payload in DOM
3. Prepare for user interaction to trigger execution

## Instructions

### Step 1: Navigate to the Server URL

**Context**: Open the browser and enter the localhost URL to fetch and display the directory listing.

No command; manually type http://localhost:8080/ in the address bar of [[tools/Firefox-ESR]].

> Expected output: A web page listing files, with the malicious filename visible. Inspect source to confirm no escaping (e.g., quotes not &quot;).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-ESR]]

## Tags

- browser-access
- xss-trigger
