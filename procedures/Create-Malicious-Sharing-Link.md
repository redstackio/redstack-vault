---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
tags:
  - xss
  - link-generation
  - adobe
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:52.996Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create Malicious Sharing Link

## Summary

This procedure finalizes the Adobe file sharing form to generate an anonymous link containing the stored XSS payload in the description, ready for distribution.

## Description

After injecting the payload, clicking 'Create Link' on https://cloud.acrobat.com/send stores the description server-side and produces a preview URL like https://files.acrobat.com/a/preview/[id]. This link, when accessed, renders the unsanitized description, executing the XSS. Requires prior steps completed. Results in a shareable URL embedding the exploit.

## Requirements

1. Form fully populated with payload
2. Valid Adobe session

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all stored fields before link generation
- Rate-limit link creations per account to prevent abuse

## Objectives

1. Persist the XSS payload via link creation
2. Obtain distributable URL for victims
3. Complete the injection phase of the attack

## Instructions

### Step 1: Review Form

**Context**: Ensure all fields are set correctly before submission.

Double-check subject, description, and anonymous option.

> Form shows preview of settings without errors.

### Step 2: Generate Link

**Context**: Submit to create the malicious resource.

Click the 'Create Link' button at the bottom of the page.

> A unique link is generated and displayed, e.g., https://files.acrobat.com/a/preview/[id], with copy option.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- link-generation
