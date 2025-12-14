---
id: proc-ubnt-escalate-001
tags:
  - xss
  - stored
  - escalation
  - draft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.325Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Escalate-to-Stored-XSS-via-Draft

## Summary

This procedure escalates the reflected XSS to a stored variant by saving the malicious payload as a draft, allowing persistent execution for any user viewing the draft on Ubiquiti forums.

## Description

The draft saving feature fails to sanitize payloads, storing them for later rendering without escaping. This turns a one-time reflected attack into persistent XSS, executable via direct links or trusted redirects on *.ubnt.com (e.g., after login). Impact amplifies to multiple victims without repeated delivery. Requires prior payload crafting; outcomes include draft persistence and triggered execution on view.

## Requirements

1. Successful reflected XSS payload in the comment field
2. Ability to save drafts (no post required)
3. Trusted domain context for indirect delivery

## Defense

Defensive measures and detection strategies:

- Sanitize drafts at save and render time
- Restrict draft sharing or viewing to authenticated owners only
- Scan stored content for malicious patterns pre-render

## Objectives

1. Persist the payload beyond session
2. Enable broad execution via links or redirects
3. Achieve higher impact like widespread phishing

## Instructions

### Step 1: Save as Draft

**Context**: Store the unsanitized payload to convert to stored XSS.

After entering the payload, click 'Save Draft' instead of 'Post'. Confirm the draft is created.

> Draft ID or link is generated; payload remains intact in storage.

### Step 2: Trigger Stored Execution

**Context**: Deliver the draft for persistent triggering.

Share the draft URL or use a trusted redirect (e.g., post-login on *.ubnt.com) to load it. Any viewer executes the XSS.

> JS runs on draft view, confirming escalation from reflected to stored.

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
- [[stored]]
- [[escalation]]
- [[draft]]
