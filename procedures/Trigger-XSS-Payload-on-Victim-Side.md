---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
tags:
  - xss-trigger
  - session-hijack
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.298Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Payload-on-Victim-Side

## Summary

This procedure describes how stored XSS payloads execute when victims interact with affected MoPub pages, leading to session hijacking.

## Description

Once injected, payloads in MoPub settings render and execute JavaScript on victim browsers viewing pages like reports, settings, or user edits. This enables stealing session tokens for account takeover. The environment is web-based, with no direct attacker action needed beyond injection.

## Requirements

1. Injected payloads in shared company views
2. Victim with access to the same company account
3. Attacker server to receive exfiltrated data

## Defense

Defensive measures and detection strategies:

- Deploy browser-based XSS auditors or extensions
- Monitor outbound requests to unknown domains
- Educate users on phishing-like indicators (e.g., unexpected alerts)

## Objectives

1. Execute payload on victim navigation
2. Exfiltrate session data
3. Achieve account takeover

## Instructions

### Step 1: Direct Victim to Pages

**Context**: Ensure victim loads affected interfaces.

Socially engineer or wait for natural navigation to reports tab or settings.

**Expected Output**: Page renders with injected content.

### Step 2: Payload Execution

**Context**: Script runs automatically on render.

Observe network traffic or alerts confirming execution (e.g., request to attacker.com with cookies).

**Expected Output**: Session data sent to attacker; potential alert or redirect.

**Success Indicators**:
- Attacker receives victim cookies
- Victim session compromised

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-execution
- hijacking
