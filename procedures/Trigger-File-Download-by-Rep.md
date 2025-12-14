---
tags:
  - file-download
  - user-execution
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
  - '[[Malicious File]]'
updated_at: '2025-12-14T03:16:02.470Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f99d71fa-6137-442e-8c76-8739af204fac
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Malicious File]]'
---
# Trigger-File-Download-by-Rep

## Summary

This procedure relies on social engineering or workflow to prompt a support representative to download and open the uploaded malicious file, leading to execution of malware or XSS payloads.

## Description

Once uploaded, files are accessible in the support queue. Representatives typically download attachments to investigate requests. An .exe could install malware upon opening, while an office document or SVG triggers XSS in browsers or viewers, compromising the rep's session or machine.

## Requirements

1. Successful upload from prior procedure
2. Patience for processing (may take minutes to hours)
3. Optional: Follow-up request to expedite review

## Defense

Defensive measures and detection strategies:

- Train staff to scan downloads with antivirus before opening
- Use sandboxed environments for viewing attachments
- Disable auto-opening of downloads in browsers

## Objectives

1. Ensure file is downloaded by authorized personnel
2. Induce execution of the payload
3. Monitor for compromise indicators if possible

## Instructions

### Step 1: Submit Request for Processing

**Context**: Place the file in the queue for review.

After upload, the request enters the support system; no further action needed from attacker unless follow-up.

> Requests are prioritized based on description; urgent phrasing may speed up.

### Step 2: Await Download

**Context**: Depend on representative workflow to access the file.

Representatives log in to the dashboard, view the request, and download the attachment to assist.

> Download occurs in their browser or file manager.

### Step 3: Payload Activation

**Context**: Execution happens upon opening.

The rep opens the .exe (runs binary) or .svg (browser renders, fires XSS).

> Compromise: Malware installs or JS executes in rep's context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Malicious File]] User Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-download]]
- [[user-execution]]
