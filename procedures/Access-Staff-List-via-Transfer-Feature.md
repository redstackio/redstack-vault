---
tags:
  - staff-enumeration
  - transfer-bypass
  - shopify
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:44.864Z'
sub_techniques:
  - '[[T1087.002]]'
id: 74157ff4-8723-42f5-800f-a088936aba84
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-Staff-List-via-Transfer-Feature

## Summary

This procedure accesses the staff account list through the 'Transfer store to client' feature, exploiting IDOR to view names without admin access.

## Description

The transfer dropdown loads staff data without proper checks, allowing enumeration of accounts. This extends the IDOR to personnel discovery, increasing privacy risks.

## Requirements

1. IDOR shop page accessed
2. Transfer link present
3. Limited permissions

## Defense

Defensive measures and detection strategies:

- Permission gates on UI elements
- Monitor transfer interface interactions

## Objectives

1. Enumerate staff accounts
2. Demonstrate full data leak
3. Highlight account discovery

## Instructions

### Step 1: Access Transfer Link

**Context**: Trigger staff dropdown.

On the shop detail page, click 'Transfer store to client'.

> Interface expands with options.

### Step 2: View Staff Dropdown

**Context**: Extract names.

Interact with the dropdown to list staff accounts.

> Names and details displayed despite no admin role.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques

- [[T1087.002]]

## Commands Used


## Tools Used


## Tags

- [[staff-enumeration]]
- [[transfer-bypass]]
- [[shopify]]
