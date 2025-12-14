---
id: proc-inject-hackerone-asset-xss
tags:
  - xss
  - injection
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:04.016Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Asset-Identifier

## Summary

This procedure injects a malicious HTML payload into a HackerOne program's asset identifier field, exploiting lack of input sanitization to store XSS for later execution.

## Description

In the HackerOne platform, the asset identifier in the program scope is not properly escaped, allowing HTML injection. The payload `"><img src=x onerror=prompt`>` closes any open tags and injects an image with an onerror handler that executes JavaScript. This is stored and rendered in multiple views, primarily exploitable in browsers without CSP like IE. Prerequisites include authenticated access to manage program assets.

## Requirements

1. Authenticated HackerOne account with program management permissions
2. Access to the program's scope editing interface
3. Vulnerable browser (IE or CSP-disabled) for testing execution

## Defense

Defensive measures and detection strategies:

- Implement input validation and HTML escaping for asset identifiers
- Enforce Content Security Policy (CSP) to block inline scripts
- Use textContent instead of innerHTML for rendering user inputs
- Monitor for anomalous JavaScript prompts or network requests from pages

## Objectives

1. Store malicious script in the asset identifier
2. Set up for multi-context XSS execution
3. Demonstrate vulnerability without immediate detection

## Instructions

### Step 1: Access Program Scope

**Context**: Navigate to the target program's asset management to prepare injection.

Log in to HackerOne and go to the program settings > Scope > Add Asset.

### Step 2: Input Malicious Payload

**Context**: Select 'Others' category and inject the payload to bypass any basic checks.

Enter the identifier as `"><img src=x onerror=prompt`>` and save the asset.

**Expected Output**: Asset added successfully, payload stored in backend.

### Step 3: Verify Storage

**Context**: Confirm the asset is listed without rendering issues.

Refresh the scope page; the identifier should display truncated but stored.

**Expected Output**: Asset visible in list, no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection
