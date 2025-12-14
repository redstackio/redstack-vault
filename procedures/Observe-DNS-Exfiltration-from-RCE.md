---
tags:
  - dns-exfiltration
  - rce
  - observation
type: procedure
tools:
  - '[[tools/dnsbin-zhack-ca]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:07.842Z'
sub_techniques: []
id: 59cc5757-aac7-4e01-9df0-4a5aff277dda
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe DNS Exfiltration from RCE

## Summary

This procedure monitors a controlled DNS server to detect resolution attempts from the exploited server, confirming successful RCE via the EL injection payload.

## Description

After payload delivery, the EL expression executes Java code that initiates a DNS lookup to the attacker's domain (embedded in the payload). Using a service like dnsbin.zhack.ca, the attacker observes incoming queries, verifying control without needing further interaction. This non-destructive method proves RCE while avoiding data leakage from file operations.

## Requirements

1. Controlled DNS domain configured in payload
2. Access to DNS logging service dashboard
3. Timing: Monitor immediately after payload send

## Defense

Defensive measures and detection strategies:

- Implement DNS sinkholing for known malicious domains
- Log and alert on web server-originated DNS queries to external hosts
- Use network segmentation to limit web app DNS access

## Objectives

1. Detect DNS query from target IP
2. Confirm payload execution
3. Validate RCE without additional exploits

## Instructions

### Step 1: Access DNS Logger

**Context**: Log into the DNS service (e.g., dnsbin.zhack.ca) and note your subdomain.

No command; open the web interface.

> Ensure the subdomain matches the one in remoteMalJarUrl.

### Step 2: Monitor for Queries

**Context**: Watch the logs for incoming A/AAAA records from the target's IP post-exploit.

No command; refresh the dashboard.

> Expected: Query entry with source IP of target server, timestamp aligning with curl request. If no query in 1-2 minutes, recheck payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/dnsbin-zhack-ca]]

## Tags

- dns-exfiltration
- rce
