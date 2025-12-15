---
id: proc-vimeo-inject-payload-3
tags:
  - xss
  - injection
  - stored-xss
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
updated_at: '2025-12-14T17:28:20.661Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Malformed XSS Payload into Input Fields

## Summary

This procedure injects a validated bypass payload into web application input fields, achieving storage in the database for later exploitation as stored XSS.

## Description

In Vimeo's case, the payload `<%0crameset%20src=''>` (or enhanced with JS) is submitted to fields like profile updates, bypassing the regex and evading output encoding in certain contexts. This stores malicious HTML/JS, impacting viewers. Requires tested payloads; outcomes include confirmed storage via response inspection.

## Requirements

1. Validated bypass payload from testing
2. Access to vulnerable input forms (e.g., profile, comments)
3. Ability to submit and retrieve content

## Defense

Defensive measures and detection strategies:

- Canonicalize inputs before filtering to handle encodings
- Escape outputs contextually (JS, HTML, JSON separately)
- Rate-limit submissions and scan for XSS patterns

## Objectives

1. Store payload without detection
2. Target multiple fields for broader impact
3. Confirm persistence in database

## Instructions

### Step 1: Select and Prepare Input

**Context**: Choose a storage-prone field.

Go to profile update form. Enter `<%0crameset%20src='' onerror='alert(1)'>` and submit.

> Form accepts without error; check network tab for stored payload in response.

### Step 2: Verify Immediate Storage

**Context**: Ensure payload is not altered post-submission.

Reload the profile page and inspect the HTML/JSON source for the intact payload in unencoded sections.

> Payload visible in raw form, indicating successful injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
