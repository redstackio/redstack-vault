---
tags:
  - xss
  - file-upload
  - pdf
  - slack
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:06.366Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c67f1f26-dfab-45fa-8edc-f591887e6516
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-PDF-to-Slack-Workspace

## Summary

This procedure involves creating and uploading a PDF file containing an embedded JavaScript XSS payload to a Slack workspace, exploiting the lack of sanitization in file uploads to store malicious content for later execution.

## Description

In the context of Slack's stored XSS vulnerability, attackers with workspace access can upload PDFs that include unsanitized JavaScript. The payload is stored server-side and rendered client-side in the PDF viewer. This step focuses on the injection phase, requiring preparation of the malicious file using PDF manipulation techniques to embed JavaScript triggers, such as /JavaScript actions in PDF objects. Prerequisites include a valid Slack account and tools for PDF editing. Expected outcomes: The file is persisted in the workspace, ready for victim interaction, potentially leading to session hijacking or data theft.

## Requirements

1. Valid Slack workspace account with file upload permissions.
2. Malicious PDF file prepared with XSS payload (e.g., JavaScript to steal cookies).
3. Internet access to the Slack web or desktop app.

## Defense

Defensive measures and detection strategies:

- Implement content scanning for uploaded files using antivirus or custom PDF parsers to detect embedded scripts.
- Enforce upload size limits and file type validation beyond MIME checks.
- Monitor for anomalous file uploads in audit logs and alert on PDF uploads from untrusted users.

## Objectives

1. Persist malicious payload in the target environment via file upload.
2. Set up conditions for stored XSS execution upon viewing.
3. Achieve initial injection without triggering upload rejections.

## Instructions

### Step 1: Prepare Malicious PDF

**Context**: Create a PDF with an embedded JavaScript payload that will execute when opened in the vulnerable viewer. Use a tool like PDFtk or Adobe Acrobat to insert a JavaScript action, such as a document-level script that runs on open.

For example, embed a payload like: this.info.JavaScript = "app.alert('XSS');"; or more malicious code to exfiltrate data.

### Step 2: Upload to Slack

**Context**: Use Slack's native upload interface to inject the file into a channel or DM, making it available for viewing.

Navigate to a Slack channel, click the "+" icon next to the message input, select "Upload file," choose the malicious PDF, and share it with an optional enticing message like "Check this report."

**Expected Output**: Upload success message; file appears in the channel with a download/preview link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[file-upload]]
- [[pdf]]
- [[slack]]
