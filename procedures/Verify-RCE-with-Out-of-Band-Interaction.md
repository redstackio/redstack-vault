---
tags:
  - oob-verification
  - rce-confirmation
  - burp-collaborator
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[PowerShell]]'
updated_at: '2025-12-14T17:31:18.967Z'
sub_techniques: []
id: 9e814a62-ffd0-4828-b02e-7097c7215655
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[PowerShell]]'
---
# Verify-RCE-with-Out-of-Band-Interaction

## Summary

This procedure monitors for out-of-band interactions from the exploited server to confirm successful remote code execution of the payload command.

## Description

After triggering the deserialization, the gadget chain executes the embedded curl command, which contacts the Burp Collaborator. This OOB technique verifies RCE without relying on direct server responses, as the HTTP reply is a generic redirect.

## Requirements

1. Active Burp Collaborator instance
2. Unique subdomain generated for the payload
3. Network visibility to collaborator polls

## Defense

Defensive measures and detection strategies:

- Block outbound HTTP/DNS to unknown domains from servers
- Monitor server logs for unexpected curl or network executions
- Use EDR to detect anomalous process chains (Java -> system shell)

## Objectives

1. Detect callback from target server
2. Confirm command execution
3. Validate exploit success

## Instructions

### Step 1: Monitor Collaborator

**Context**: Poll Burp Collaborator for incoming requests triggered by the RCE.

**Command**:
No direct command; use Burp Suite interface.

> Access Burp Collaborator client and check for HTTP requests or DNS lookups to your subdomain. Expected: Incoming GET/POST from target's IP with curl-like headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[PowerShell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- oob-verification
- rce-confirmation
- burp-collaborator
