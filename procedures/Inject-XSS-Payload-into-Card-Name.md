---
id: proc-uuid-2
tags:
  - xss
  - payload-injection
  - javascript
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
updated_at: '2025-12-14T03:15:53.093Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Card-Name

## Summary

This procedure details injecting a malicious JavaScript payload into the card[name] parameter during Twitter Ads card creation to exploit a persistent XSS vulnerability.

## Description

The attack targets insufficient sanitization in the card[name] field, allowing HTML tag breakage and script insertion. In the web environment of ads.twitter.com, an authenticated user crafts a payload that closes an existing <title> tag, injects <script>alert(document.cookie)</script>, and reopens <title> to maintain page integrity. This sets up persistence upon submission. Prerequisites: Access to the creation form from the prior procedure.

## Requirements

1. Loaded card creation form
2. Understanding of HTML context (e.g., title tag breakout)
3. Browser with JS console for testing

## Defense

Defensive measures and detection strategies:

- Enforce strict input sanitization using libraries like DOMPurify
- Validate and escape user inputs server-side before storage

## Objectives

1. Bypass client-side validation to insert raw HTML/JS
2. Ensure payload survives form submission
3. Prepare for persistence and execution

## Instructions

### Step 1: Identify Vulnerable Field

**Context**: Locate the card[name] input in the form.

Inspect the form using browser dev tools to confirm the field accepts arbitrary text.

> Field identified as editable text input without visible restrictions.

### Step 2: Craft and Insert Payload

**Context**: Enter the breakout payload to inject JS.

Type or paste: `</title><script>alert(document.cookie)</script><title>` into card[name].

> Payload entered; form may render partially broken, but submission proceeds.

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
- [[payload-injection]]
