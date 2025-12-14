---
id: uuid-test-escalations
tags:
  - ssrf
  - escalation
  - limitations
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.739Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Further-Escalations-and-Limitations

## Summary

This procedure probes for additional SSRF escalations, such as other protocols or deeper metadata, while confirming limitations to scope the attack's impact.

## Description

Attempts to redirect to gopher://, file://, or JSON metadata endpoints reveal failures due to protocol blocks, curly braces, or response issues. No IAM role prevents RCE, limiting to basic discovery.

## Requirements

1. Successful SSRF setup from prior steps
2. Test URLs for various protocols
3. AWS metadata knowledge

## Defense

Defensive measures and detection strategies:

- Enforce protocol whitelisting (HTTPS only, no redirects to others)
- Parse and filter responses for sensitive patterns (e.g., JSON with braces)
- Attach minimal IAM roles or none to backend instances

## Objectives

1. Test non-HTTP protocols for broader SSRF
2. Attempt JSON metadata access
3. Confirm no escalation path

## Instructions

### Step 1: Test Other Protocols

**Context**: Check gopher, ftp, etc.

Modify PHP to redirect to gopher://... and trigger command.

> Expected: [Bad Server Response / Too slow].

### Step 2: Test JSON Endpoint

**Context**: Target dynamic metadata.

Redirect to http://169.254.169.254/latest/dynamic/instance-identity/document.

> Expected: Failure due to curly braces in JSON.

### Step 3: Verify IAM Limits

**Context**: Check for role-based escalation.

Attempt IAM role endpoints if present.

> Expected: No role, so limited to basic metadata.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[escalation]]
- [[limitations]]
