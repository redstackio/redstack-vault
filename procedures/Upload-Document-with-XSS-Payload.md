---
id: proc-uuid-0003
tags:
  - xss-injection
  - upload
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:03.549Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Document-with-XSS-Payload

## Summary

This procedure involves uploading a document to the Localize project while injecting a stored XSS payload into the title field, exploiting insufficient input sanitization to store malicious JavaScript.

## Description

The document title field lacks proper escaping, allowing HTML and JavaScript injection. The payload `>"><img src=x onerror=alert(document.domain)>` closes open tags, injects an image with an onerror handler, and executes on render. This stored variant persists for any viewer, enabling broad impact like session hijacking. Prerequisites include an active project; outcomes confirm storage via successful save without errors.

## Requirements

1. Configured translation project.
2. Sample document file (e.g., .txt or .doc).
3. Knowledge of XSS payloads.

## Defense

Defensive measures and detection strategies:

- Sanitize and escape user inputs in titles using libraries like DOMPurify.
- Implement Content Security Policy (CSP) to block inline scripts.
- Scan uploads for malicious patterns with antivirus or WAF rules.

## Objectives

1. Store unsanitized payload in the database.
2. Prepare for execution on document view.
3. Demonstrate vulnerability without immediate detection.

## Instructions

### Step 1: Prepare Upload

**Context**: Select and configure the document for upload.

Click 'Upload Document' and choose a file.

> File selector opens. Expected output: Preview of upload form including title field.

### Step 2: Inject Payload in Title

**Context**: Target the vulnerable title input to embed the XSS script.

In the 'Document Title' field, enter: `>"><img src=x onerror=alert(document.domain)>`

> This payload breaks out of context and sets up execution. Expected output: Title accepted without validation errors.

### Step 3: Save Document

**Context**: Persist the injection by completing the upload.

Click 'Save' or 'Upload' to store the document.

> Processes and lists the document. Expected output: Success message with tainted title visible in list.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
