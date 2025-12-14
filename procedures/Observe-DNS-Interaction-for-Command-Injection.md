---
tags:
  - command-injection-detection
  - dns-oob
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T04:08:55.191Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b8377581-486a-4a2e-bafb-ca58c2091841
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Observe-DNS-Interaction-for-Command-Injection

## Summary

This procedure validates blind command injection by monitoring DNS lookups triggered by the injected ping command, providing confirmation of server-side execution.

## Description

The ping command causes the server to resolve the attacker's domain, creating an observable DNS query. This OOB technique confirms the vulnerability without relying on direct output, highlighting risks for more destructive commands.

## Requirements

1. Command payload injected
2. Burp Collaborator monitoring active
3. DNS polling enabled

## Defense

Defensive measures and detection strategies:

- Block or log DNS queries to suspicious domains from web servers
- Use endpoint detection to flag command execution in web contexts
- Apply least-privilege principles to application processes

## Objectives

1. Detect DNS resolution from target
2. Confirm command injection
3. Assess potential for advanced attacks

## Instructions

### Step 1: Monitor DNS Polling

**Context**: Check Collaborator for DNS interactions after injection.

Poll the Collaborator client for new DNS queries.

> Query from target's IP to the subdomain indicates success.

### Step 2: Verify Execution Details

**Context**: Analyze the DNS record for timing and source validation.

Review query type (A/AAAA) and any additional data.

> Correlates with injection timestamp, proving causation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[command-injection-detection]]
- [[dns-oob]]
