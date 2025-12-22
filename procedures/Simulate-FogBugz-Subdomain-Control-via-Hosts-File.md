---
id: proc-simulate-subdomain-control
tags:
  - ssrf
  - subdomain
  - hosts-file
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/add-hosts-entry-for-subdomain-redirect]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.239Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Simulate FogBugz Subdomain Control via Hosts File

## Summary

This procedure simulates control over a fogbugz.com subdomain by modifying the target's /etc/hosts file, redirecting traffic to an attacker-controlled VPS for PoC purposes in SSRF exploitation.

## Description

In a real attack, control would come from vulnerabilities like SQLi or subdomain takeover on fogbugz.com. For reproduction, edit /etc/hosts on the GitLab server to point poc.fogbugz.com to a VPS IP (e.g., 198.211.125.160). This allows hosting malicious responses that GitLab will fetch during import, bypassing domain checks since Kernel.open resolves locally.

## Requirements

1. Root or sudo access to the GitLab server (Linux)
2. VPS with public IP for hosting
3. Network access to edit /etc/hosts

## Defense

Defensive measures and detection strategies:

- Monitor /etc/hosts modifications via file integrity tools like Auditd
- Implement strict DNS resolution without local overrides in import services
- Use network segmentation to prevent localhost access from external fetches

## Objectives

1. Redirect fogbugz.com subdomain to controlled server
2. Enable injection of malicious URLs in API responses
3. Set up for SSRF trigger during GitLab import

## Instructions

### Step 1: Add Hosts Entry

**Context**: Append the redirect entry to /etc/hosts to simulate subdomain control.

**Command** ([[commands/add-hosts-entry-for-subdomain-redirect]]):
```bash
echo "198.211.125.160 poc.fogbugz.com" | sudo tee -a /etc/hosts
```

> This command adds the line '198.211.125.160 poc.fogbugz.com' to /etc/hosts. Expected output: No errors, and 'cat /etc/hosts' shows the new entry. Verify with 'ping poc.fogbugz.com' resolving to 198.211.125.160.

### Step 2: Verify Resolution

**Context**: Confirm the redirect works before proceeding.

**Command** (ping):
```bash
ping -c 1 poc.fogbugz.com
```

> Pings the domain; expected output shows packets to 198.211.125.160.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/add-hosts-entry-for-subdomain-redirect]]

## Tools Used


## Tags

- ssrf
- subdomain
- hosts-file
