---
id: proc-002
tags:
  - xss
  - stored-xss
  - json
  - payload
type: procedure
tools: []
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
updated_at: '2025-12-14T03:16:25.295Z'
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
# Input-Malicious-JSON-Payload

## Summary

This procedure details crafting and submitting a JSON object with an XSS payload embedded in a key name to exploit unsanitized input handling in Algolia's UI Demo feature.

## Description

The Stored XSS arises from Algolia's failure to escape JSON keys when rendering them in the UI. By using a key like '<img src=1 onerror=alert(document.domain)>', the payload is stored and later interpreted as HTML/JS. This step targets the JSON input mechanism, either direct entry or file upload, in an authenticated session. Prerequisites include access to the UI Demo interface; outcomes involve successful payload storage without immediate execution.

## Requirements

1. Access to the Generate a UI Demo interface
2. Knowledge of basic JSON syntax and XSS payloads
3. Text editor or browser dev tools for payload crafting

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled inputs, including JSON keys, using HTML entity encoding
- Validate JSON structure server-side to reject suspicious key patterns
- Log and alert on JSON uploads containing script-like content

## Objectives

1. Inject XSS payload into JSON key without rejection
2. Store the malicious content in the demo configuration
3. Enable rendering in subsequent UI interactions

## Instructions

### Step 1: Craft the Malicious JSON

**Context**: Create a JSON object where the key embeds the XSS payload.

Use a text editor to build the JSON, ensuring the key triggers HTML parsing. Example payload key: '<img src=1 onerror=alert(document.domain)>'. Full example:

```json
{
  "<img src=1 onerror=alert(document.domain)>": "hello"
}
```

> The JSON should be valid; test parsing in a JSON validator.

### Step 2: Input or Upload the JSON

**Context**: Submit the payload to the vulnerable endpoint.

In the UI Demo interface, paste the JSON into the input field or save it as a .json file and upload it via the file selector. Click submit or process.

> The interface accepts the JSON and advances to attribute selection.

### Step 3: Verify Payload Acceptance

**Context**: Confirm no sanitization blocks the input.

Check for any error messages; if none, the payload is stored.

> No alerts or rejections indicate success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[json]]
- [[payload]]
