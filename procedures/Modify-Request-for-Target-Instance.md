---
id: proc-uuid-3
name: Modify-Request-for-Target-Instance
tags:
  - request-modification
  - host-spoofing
  - endpoint-update
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Connection Proxy]]'
updated_at: '2025-12-14T17:25:13.202Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Multi-hop Proxy]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Connection Proxy]]'
---
# Modify-Request-for-Target-Instance

## Summary

This procedure adapts a captured Aura request template by changing the host, path, and target to point to the vulnerable Salesforce instance, enabling replay against the actual target.

## Description

Using Burp Repeater, update the Host header and request path to match the target's configuration (e.g., acronis.secure.force.com/acc/aura). This simulates a legitimate request from the target domain while stripping auth if needed for Guest access. The scenario targets Salesforce orgs with misconfigured object permissions; outcomes include a request ready for payload injection without triggering auth checks.

## Requirements

1. Captured template request in Burp Repeater
2. Known target domain and Aura path (e.g., /acc/aura for custom sites)
3. Burp target scope updated to avoid filtering

## Defense

Defensive measures and detection strategies:

- Validate Host headers against allowed domains in API gateways
- Log and alert on mismatched Host/path combinations
- Enforce strict referer checks for API calls

## Objectives

1. Redirect request to target Salesforce instance
2. Preserve request structure while updating routing
3. Prepare for unauthenticated submission

## Instructions

### Step 1: Update Host Header

**Context**: Change the destination domain to the target.

No command; edit in Repeater:
- In Raw or Params view, set 'Host: acronis.secure.force.com'.
- Update Burp > Target > Scope to include the domain.

> Request now targets the vulnerable instance. Expected output: Header updated, no validation errors.

### Step 2: Adjust POST Path

**Context**: Align the endpoint with target's Aura configuration.

No command; modify request line:
- Change POST /s/sfsites/aura to POST /acc/aura.

> Full URL becomes https://acronis.secure.force.com/acc/aura. Expected output: Path reflects target setup.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Connection Proxy]] Proxy

### Sub-Techniques

- [[Multi-hop Proxy]] Multi-hop Proxy

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[modification]]
- [[host-header]]
- [[path-injection]]
