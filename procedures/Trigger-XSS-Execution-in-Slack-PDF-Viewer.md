---
tags:
  - xss
  - javascript
  - pdf-viewer
  - slack
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.348Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e396feea-0fc0-4bab-8573-c40e413a272c
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-in-Slack-PDF-Viewer

## Summary

This procedure describes how a victim viewing an uploaded malicious PDF in Slack's PDF viewer triggers the stored XSS payload, leading to JavaScript execution in the browser due to a vulnerable dependency that does not properly sanitize PDF contents.

## Description

Slack's PDF viewer (https://app.slack.com/pdf-viewer) relies on a third-party dependency vulnerable to improper encoding of special characters and scripts in PDFs. When a user clicks to preview or open the uploaded file, the viewer renders the content, executing embedded JavaScript in the context of the user's Slack session. This can result in data exposure, such as stealing authentication tokens or session cookies. The attack assumes the payload was previously uploaded; this step relies on social engineering to induce viewing. Outcomes include arbitrary code execution client-side, with potential for further exploitation like keylogging or phishing.

## Requirements

1. Access to a Slack workspace where the malicious PDF has been uploaded.
2. Victim with a Slack account who interacts with the file link.
3. Browser environment supporting JavaScript (standard for web apps).

## Defense

Defensive measures and detection strategies:

- Patch vulnerable dependencies in PDF rendering libraries promptly.
- Implement client-side sanitization or use isolated iframe rendering with strict CSP.
- Log and monitor PDF view events for unusual patterns, such as rapid views from new IPs.

## Objectives

1. Execute the stored XSS payload in the victim's browser.
2. Collect sensitive data from the Slack session.
3. Maintain stealth to avoid immediate detection.

## Instructions

### Step 1: Entice Victim to View File

**Context**: Use social engineering within Slack to encourage the target to open the PDF, such as sharing in a relevant channel with a deceptive filename like "Quarterly_Report.pdf."

Post the file link or attachment in a public channel or direct message.

### Step 2: Execute Payload on View

**Context**: When the victim clicks the preview or download link, the PDF viewer loads the file, triggering the JavaScript due to the unsanitized rendering.

The vulnerable dependency processes the PDF without escaping script tags or actions, allowing code like "eval('steal cookies')" to run.

**Expected Output**: JavaScript executes silently or with visible effects (e.g., alert); data may be exfiltrated to an attacker-controlled server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[JavaScript]]
- [[pdf-viewer]]
- [[slack]]
