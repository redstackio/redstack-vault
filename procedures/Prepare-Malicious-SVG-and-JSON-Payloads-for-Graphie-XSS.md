---
id: proc-prepare-graphie-payloads-001
name: Prepare-Malicious-SVG-and-JSON-Payloads-for-Graphie-XSS
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.278Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[JavaScript]]'
tags:
  - xss
  - payload-prep
  - svg
  - json
platforms:
  - Web
tools: []
commands: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Prepare-Malicious-SVG-and-JSON-Payloads-for-Graphie-XSS

## Summary

This procedure crafts malicious SVG and JSON payloads exploiting weak sanitization in Khan Academy's Graphie renderer, enabling DOM-based XSS via onload attributes and direct script insertion in labels.

## Description

In the context of Khan Academy's legacy Graphie to PNG API, the renderer inserts SVG and JSON content directly into the DOM without proper escaping. By modifying existing Graphie files to include executable JavaScript (e.g., onload events or script tags), attackers can inject code that executes when pages load affected assets from the CDN. Prerequisites include obtaining a legitimate Graphie file via inspection of Khan Academy math pages. Expected outcome: Payloads ready for upload that trigger alerts or arbitrary JS on render.

## Requirements

1. Access to a legitimate Graphie SVG and JSON (e.g., from https://cdn.kastatic.org/ka-perseus-graphie/)
2. Text editor or browser console for payload modification
3. Knowledge of target file hash for override

## Defense

Defensive measures and detection strategies:

- Implement strict SVG/JSON sanitization using libraries like DOMPurify
- Disable or deprecate legacy APIs with upload capabilities
- Monitor CDN uploads for anomalous FormData POSTs to graphie-to-png endpoints

## Objectives

1. Create injectable payloads bypassing typesetAsMath rendering
2. Ensure JS execution via DOM insertion
3. Prepare for CDN override without detection

## Instructions

### Step 1: Modify SVG Payload

**Context**: Add an onload attribute to the SVG root element to execute JS on insertion.

No command needed; edit manually:

```xml
<svg xmlns="http://www.w3.org/2000/svg" onload="alert('XSS')" width="100" height="100">
  <!-- Original SVG content -->
</svg>
```

> This inserts the alert on load; replace with actual malicious JS. Expected output: Valid SVG string with event handler.

### Step 2: Modify JSON Payload

**Context**: Alter label content to include script tags, disabling math rendering.

No command; edit JSON:

```json
{
  "labels": [{
    "text": "<script>alert('XSS')</script>",
    "typesetAsMath": false
  }],
  // Original JSON
}
```

> Sets typesetAsMath to false for direct DOM injection. Expected output: JSON object with unescaped script.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-prep]]
