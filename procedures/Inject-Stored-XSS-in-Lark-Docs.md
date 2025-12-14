---
tags:
  - xss
  - stored-xss
  - lark-docs
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/craft-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:19.925Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: bd6b1ee1-e32a-45db-9921-a1c22f287143
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-in-Lark-Docs

## Summary

This procedure exploits insufficient input sanitization in Lark Docs to inject persistent JavaScript payloads into documents, which execute in users' browsers upon viewing and can escalate when processed server-side.

## Description

Lark Docs, a collaborative document platform, fails to properly sanitize user inputs in document content, allowing attackers with edit access to insert HTML and JavaScript. The payload persists across sessions and users, leading to client-side execution. In this scenario, the injection sets up for SSRF escalation during server-side rendering in a headless browser. Prerequisites include authenticated access to create or edit documents.

## Requirements

1. Valid Lark account credentials with document edit permissions
2. Access to the Lark Docs web interface
3. Basic knowledge of JavaScript payloads for XSS

## Defense

Defensive measures and detection strategies:

- Implement strict content security policy (CSP) to block inline scripts
- Server-side sanitization using libraries like DOMPurify
- Monitor for anomalous script tags in document content

## Objectives

1. Achieve persistent code execution in document viewers
2. Set up payload for server-side exploitation
3. Demonstrate impact through alert or data exfiltration

## Instructions

### Step 1: Authenticate and Create Document

**Context**: Log in to Lark Docs and start a new document to prepare for injection.

Navigate to the Lark Docs interface and create a blank document.

### Step 2: Craft and Inject Payload

**Context**: Use a simple script tag to test XSS, escalating to SSRF-triggering code.

**Command** ([[commands/craft-xss-payload]]):
```bash
# Example payload crafting (use in browser console or editor)
echo '<script>fetch("http://internal-resource").then(r => r.text()).then(data => alert(data));</script>' > payload.html
```

> This crafts a basic fetch-based payload. Paste it into the document editor as HTML content. Save the document.

### Step 3: Verify Injection

**Context**: View the document to confirm execution.

Re-open or share the document; the script should execute, showing an alert or fetching data.

**Expected Output**: JavaScript alert or network request to the specified resource.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/craft-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
