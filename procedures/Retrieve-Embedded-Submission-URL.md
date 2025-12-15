---
id: proc-003
tags:
  - reconnaissance
  - embedded-form
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:48.537Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve-Embedded-Submission-URL

## Summary

This procedure extracts the URL for HackerOne's embedded submission form from a program's policy page, enabling access to the vulnerable endpoint.

## Description

Embedded forms are intended for integration but use a non-standard authorization method (interact_without_authorization), skipping key checks. By inspecting the policy page, attackers obtain the UUID-based URL (e.g., /0a1e1f11-257e-4b46-b949-c7151212ffbb/embedded_submissions/new). This step is reconnaissance-focused, preparing for the bypass. Expected outcome: Usable URL for subsequent exploitation.

## Requirements

1. Access to target program policy page (e.g., https://hackerone.com/parrot_sec/policy)
2. Web browser with developer tools for URL extraction if not visible
3. No authentication required for policy viewing

## Defense

Defensive measures and detection strategies:

- Restrict embedded form URLs to authorized integrators only
- Monitor access to policy pages for unusual patterns
- Obfuscate or protect UUIDs in public pages

## Objectives

1. Locate the embedded form endpoint
2. Gather UUID for targeted requests
3. Set up for authorization bypass testing

## Instructions

### Step 1: Visit Policy Page

**Context**: Access the program's policy documentation.

Navigate to https://hackerone.com/parrot_sec/policy.

> Policy content loads, often including embedded form instructions.

### Step 2: Inspect for Embedded URL

**Context**: Search for the form URL in page content or source.

Look for links or text mentioning 'embedded submissions'; copy the URL like https://hackerone.com/0a1e1f11-257e-4b46-b949-c7151212ffbb/embedded_submissions/new.

> URL found in HTML or visible embed code.

### Step 3: Verify URL Accessibility

**Context**: Test if the URL loads.

Paste the URL into a new tab; it should show the form.

> Form interface appears without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- reconnaissance
- embedded-form
