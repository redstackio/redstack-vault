---
id: proc-identify-subdomain-takeover
name: Identify-and-Verify-Subdomain-Takeover
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.318Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - subdomain-takeover
  - dns-recon
platforms:
  - Web
commands: []
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Identify-and-Verify-Subdomain-Takeover

## Summary

This procedure identifies dangling DNS records pointing to unclaimed third-party services like expired HubSpot instances, verifies takeover feasibility, and confirms control by hosting a proof-of-concept page, enabling initial access to a target's subdomain.

## Description

In the Roblox incident, the devrel.roblox.com subdomain had a CNAME record pointing to an expired HubSpot instance. Attackers query DNS to spot this, attempt to claim the resource via HubSpot registration, and verify by accessing a custom URL like https://devrel.roblox.com/subdomain-takeover. This grants full control for hosting arbitrary content, setting the stage for further exploits like phishing or script injection. Prerequisites include public DNS access and knowledge of common third-party services.

## Requirements

1. Access to DNS resolution tools (e.g., dig, nslookup)
2. Internet access to visit and claim third-party services like HubSpot
3. Basic understanding of DNS records and subdomain management

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMES using automated scanners
- Implement monitoring for subdomain access logs and third-party service expirations
- Use certificate transparency logs to detect unauthorized subdomain claims

## Objectives

1. Discover unclaimed subdomains for takeover
2. Verify control without alerting defenders
3. Establish a foothold for malicious content hosting

## Instructions

### Step 1: Query DNS Records

**Context**: Check for CNAME records pointing to potentially expired services.

**Command** (dig-cname-check):
```bash
dig CNAME devrel.roblox.com
```

> This command resolves the CNAME for the target subdomain. Expected output includes a record like "devrel.roblox.com. 3600 IN CNAME hs-sites.com" if pointing to HubSpot, indicating a potential dangling record.

### Step 2: Verify Takeover Feasibility

**Context**: Visit the subdomain to confirm it's unclaimed and accessible for takeover.

Navigate to https://devrel.roblox.com and look for HubSpot's expired page indicators. Register a free HubSpot account and link it to the detected instance.

**Expected Output**: Ability to upload and host a simple HTML page confirming takeover, e.g., displaying "Subdomain Taken Over" at https://devrel.roblox.com/subdomain-takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[dns-recon]]
