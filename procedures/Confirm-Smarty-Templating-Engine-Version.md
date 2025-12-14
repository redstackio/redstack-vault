---
id: proc-uuid-2
tags:
  - ssti
  - smarty
  - version-leak
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/smarty-version-check]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:08.601Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Confirm-Smarty-Templating-Engine-Version

## Summary

This procedure confirms the use of the Smarty templating engine by injecting a variable reference to extract its version, displayed in the rendered email template.

## Description

Following SSTI detection, this step leverages Smarty's built-in variables to leak the engine version. In the Unikrn case, injecting {$smarty.version} into profile fields results in the version being echoed in the invitation email, aiding in tailoring further exploits based on known Smarty vulnerabilities.

## Requirements

1. Confirmed SSTI from prior test
2. Profile edit access
3. Email invitation capability

## Defense

Defensive measures and detection strategies:

- Restrict access to Smarty internal variables
- Implement input validation to block variable syntax
- Log and alert on unusual template variable expansions

## Objectives

1. Identify the exact templating engine and version
2. Assess potential exploit paths based on version
3. Validate template variable resolution

## Instructions

### Step 1: Inject Version Payload

**Context**: Use Smarty's internal variable to query the version during template processing.

**Command** ([[commands/smarty-version-check]]):
```smarty
{$smarty.version}
```

> Enter this in a profile field, save, and proceed to trigger.

### Step 2: Render and Inspect

**Context**: Force template evaluation via email generation.

**Instructions**: Send an invitation email and open the received email to view the output.

> Expected output: The Smarty version (e.g., "3.1.21") appears in the email body.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/smarty-version-check]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssti]]
- [[smarty]]
- [[version-leak]]
