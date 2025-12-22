---
tags:
  - subdomain-takeover
  - recon
type: procedure
tools:
  - '[[tools/HubSpot]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-dns-lookup]]'
  - '[[commands/curl-host-content]]'
platforms:
  - Web
techniques:
  - '[[Compromise Infrastructure]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: b7ba33e5-46d2-419b-b23b-cfac8bc247e0
created_at: '2025-12-11T06:10:30.565Z'
updated_at: '2025-12-11T06:10:30.565Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1584]]'
---
# Identify Dangling CNAME for Subdomain Takeover

## Summary

This procedure identifies subdomains with dangling CNAME records pointing to unclaimed third-party services like HubSpot, enabling potential takeover by claiming the service.

## Description

In this attack scenario, DNS records are queried to find subdomains resolving to expired or unclaimed instances. For devrel.roblox.com, the CNAME pointed to an unclaimed HubSpot site, allowing an attacker to claim it and host content. This is common in web environments where services are decommissioned without removing DNS records.

## Requirements

1. Access to DNS query tools like dig
2. Target domain knowledge
3. Internet access

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs
- Monitor subdomain resolutions and third-party service claims

## Objectives

1. Discover vulnerable subdomains for takeover
2. Confirm dangling CNAME to unclaimed service
3. Prepare for claiming and exploitation

## Instructions

### Step 1: Query DNS Records

**Context**: Use DNS lookup to identify CNAME records.

**Command** ([[commands/dig-dns-lookup]]):

```bash
dig devrel.roblox.com
```

> This command retrieves DNS records, look for CNAME pointing to HubSpot.

### Step 2: Verify Unclaimed Status

**Context**: Check if the pointed service is unclaimed by attempting access or registration.

Manual verification via browser: Visit the HubSpot URL and see if it's available for claim.

> Expected: Error or claim prompt indicating it's unclaimed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Compromise Infrastructure]]

### Sub-Techniques



## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used



## Tags

- [[subdomain-takeover]]
- [[recon]]
