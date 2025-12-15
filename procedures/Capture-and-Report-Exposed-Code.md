---
id: proc-003
tags:
  - capture-evidence
  - reporting
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:24:56.708Z'
skill_level: beginner
impact_level: informational
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Capture-and-Report-Exposed-Code

## Summary

This procedure covers documenting the disclosed information from an error message and submitting a report to the vulnerability disclosure program.

## Description

Once an error exposes sensitive details like Node.js code, capturing it accurately is crucial for validation and reporting. In educational platforms like PortSwigger's academy, such findings are reported via HackerOne. The process includes screenshotting the error, analyzing the exposure (e.g., code snippets aiding vulnerability discovery), and submitting with context. Impact is limited to lab environments but illustrates real-world risks.

## Requirements

1. Screenshot tool (built-in browser or OS)
2. Access to reporting platform (HackerOne)
3. Restored network connection

## Defense

Defensive measures and detection strategies:

- Review disclosure reports promptly
- Patch error handlers in lab code
- Educate on secure error logging

## Objectives

1. Preserve evidence of the disclosure
2. Submit for review and potential remediation
3. Assess broader implications

## Instructions

### Step 1: Document the Error

**Context**: Capture the visual and textual evidence of the exposure.

Use browser screenshot (Ctrl+Shift+S in Chrome) to save the full error page, including URL, timestamp, and code visible.

> Expected output: Image file showing Node.js code in the error trace.

### Step 2: Analyze and Report

**Context**: Prepare and submit the finding.

Restore connection, log into HackerOne, create a new report with title 'Information disclosure on error message', description of steps, impact, and attach screenshot.

> Expected output: Report ID generated; triage response from team.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- capture-evidence
- reporting
