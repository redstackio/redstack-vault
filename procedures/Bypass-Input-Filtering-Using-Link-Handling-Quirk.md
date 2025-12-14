---
tags:
  - filter-bypass
  - xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
id: ed3b5199-4f40-4a2e-b325-6c4617cb74b1
created_at: '2025-12-13T23:55:06.653Z'
updated_at: '2025-12-13T23:55:06.653Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-Input-Filtering-Using-Link-Handling-Quirk

## Summary

This procedure leverages Shopify's automatic link conversion in the notes field and repeated editing to bypass basic input filtering, facilitating the injection of XSS payloads.

## Description

Shopify auto-converts URL-like inputs to <a> tags, which can be nested or modified through multiple edit-save cycles. This quirk allows evasion of simple script blocking by embedding javascript: URIs inside tags. For instance, entering repeated links builds nested structures that persist. This aids discovery and exploitation of the stored XSS, requiring iterative testing.

## Requirements

1. Edit access to customer notes
2. Patience for multiple edit iterations
3. Basic understanding of HTML tag nesting

## Defense

Defensive measures and detection strategies:

- Disable auto-linking or strip all HTML on input
- Limit edit history and validate on each save
- Use strict parsers to reject nested or malformed tags

## Objectives

1. Evade sanitization to store executable code
2. Exploit UI behaviors for payload persistence
3. Enable successful XSS injection

## Instructions

### Step 1: Trigger Auto-Linking

**Context**: Input text that Shopify interprets as a link to add <a> tags.

In the notes field, enter a URL like "http://example.com" and save.

> Shopify wraps it in <a href="http://example.com">, confirming the quirk.

### Step 2: Nest and Bypass via Repeated Edits

**Context**: Edit multiple times to build nested tags with JS.

Re-edit, append javascript:alert(1) inside the <a>, nest another <a>, and save repeatedly (2-3 times).

> Tags nest without full stripping, allowing payload survival for execution on view.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[filter-bypass]]
- [[xss]]
