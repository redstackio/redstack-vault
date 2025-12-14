---
tags:
  - xss
  - bypass
  - obfuscation
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:08:55.617Z'
skill_level: advanced
impact_level: high
sub_techniques: []
id: f8749037-cb95-4cc3-a0e4-86c94ca4c0cd
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-URL-Validation-with-Whitespace

## Summary

This procedure obfuscates the javascript: protocol in the Mastodon API response using leading whitespace or control characters to evade URL validation fixes in IRCCloud.

## Description

After initial patches block direct 'javascript:', attackers prepend spaces or ASCII controls (e.g., ' javascript:') in the JSON 'url' field. This targets updated IRCCloud clients; requires API control. Outcome: Embed loads and executes despite fixes, maintaining XSS viability.

## Requirements

1. Patched IRCCloud version with protocol checks
2. Modified Mastodon API response
3. Prior attack setup

## Defense

Defensive measures and detection strategies:

- Trim whitespace and normalize URLs before validation in embed logic
- Reject any URL starting with non-standard protocols after sanitization

## Objectives

1. Obfuscate malicious URL to bypass checks
2. Restore JS execution capability
3. Demonstrate fix inadequacy

## Instructions

### Step 1: Modify API Response

**Context**: Add obfuscation to the JSON payload.

Update Mastodon API to return: 'url': ' javascript:top.document.body.innerHTML = "hi your cookie is " + document.cookie;//' (note leading space).

> Test endpoint to ensure JSON parses correctly.

### Step 2: Send Obfuscated Link and Test

**Context**: Repeat delivery on patched target.

Send https://sm4.ca/@a/000000000000000002; wait for embed and confirm execution.

> Verify JS runs without protocol block.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[bypass]]
