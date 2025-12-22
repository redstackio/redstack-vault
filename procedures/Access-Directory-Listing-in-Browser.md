---
id: proc-uuid-003
name: Access-Directory-Listing-in-Browser
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.537Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - browser-access
  - directory-listing
  - xss-exposure
commands: []
platforms:
  - Web
  - Browser
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Access-Directory-Listing-in-Browser

## Summary

This procedure involves navigating to the vulnerable server's directory listing in a web browser to view the unsanitized HTML output containing the stored XSS payload.

## Description

Once the simplehttpserver is running, accessing http://127.0.0.1:8000 generates an HTML page with <ul> elements listing files, where the malicious name is inserted via ulist.push('<a href="'+item+'">'+item+'</a>') without escaping. This step simulates a victim or tester accessing the endpoint. Prerequisites: Running server from prior step. Expected outcome: Visible listing with clickable malicious link.

## Requirements

1. Server running on localhost:8000
2. Modern web browser (Chrome, Firefox, etc.)
3. Local network access (localhost)

## Defense

Defensive measures and detection strategies:

- Disable directory listings in production servers
- Implement authentication for admin interfaces
- Browser extensions or policies to block javascript: links
- Network monitoring for local server access patterns

## Objectives

1. Render the vulnerable HTML in a client context
2. Expose the payload for interaction
3. Validate the stored XSS persistence

## Instructions

### Step 1: Navigate to Server URL

**Context**: Open the browser to the local endpoint to load the directory listing.

**Command** (Browser action):
No command; manual navigation.

> Enter http://127.0.0.1:8000 in the browser address bar and press Enter. Expected output: An HTML page displaying the directory contents, including the malicious file as a link with href starting with 'javascript:'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[browser-access]]
- [[directory-listing]]
- [[xss-exposure]]
