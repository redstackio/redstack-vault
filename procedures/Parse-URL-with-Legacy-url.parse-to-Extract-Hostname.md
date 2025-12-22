---
tags:
  - crlf-injection
  - legacy-parsing
  - node-js
type: procedure
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/parse-legacy-url]]'
verified: false
platforms:
  - Node.js
  - JavaScript
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.496Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 7d905c49-176e-427a-a552-734f2106b4e2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Parse-URL-with-Legacy-url.parse-to-Extract-Hostname

## Summary

This procedure exploits the CRLF injection by parsing the malicious URL with Node.js legacy url.parse(), extracting only the hostname before the newline to bypass whitelists.

## Description

The legacy parser in Node.js (lib/url.js lines 298-340) treats CRLF in the hostname as a terminator, extracting only 'test1.com' from 'http://test1.com\r\ntest2.com'. This allows attackers to pass validation while targeting unauthorized hosts, leading to exploitation of vulnerabilities like SSRF. Target environment: Node.js apps with whitelist checks on .hostname. Prerequisites: POC URL from prior step. Expected outcome: Extracted hostname passes whitelist, enabling compromise.

## Requirements

1. Node.js runtime
2. Crafted POC URL available
3. Application context using url.parse for validation

## Defense

Defensive measures and detection strategies:

- Use WHATWG-compliant URL parsing (new URL())
- Log and validate full URL strings
- Audit dependencies for legacy url module usage

## Objectives

1. Demonstrate hostname extraction flaw
2. Bypass whitelist for unauthorized access
3. Highlight risk of medium-high severity exploits

## Instructions

### Step 1: Require and Parse the URL

**Context**: Load the url module and parse to isolate the vulnerable hostname extraction.

**Command** ([[commands/parse-legacy-url]]):
```javascript
const url = require('url');
const parsed = url.parse(poc_url);
console.log(parsed.hostname);
```

> Requires the built-in url module, parses poc_url, and logs .hostname, outputting 'test1.com' due to CRLF termination. Expected output: 'test1.com', confirming bypass potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/parse-legacy-url]]

## Tools Used


## Tags

- [[crlf-injection]]
- [[legacy-parsing]]
