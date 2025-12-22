---
tags:
  - dns
  - registration
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.881Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 587492a8-1c65-41ec-9e59-515e65bcc1b3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-Dangling-DNS-Record

## Summary

This procedure claims ownership of a dangling DNS record by registering the pointed-to resource on its provider, thereby taking control of the associated subdomain.

## Description

Following discovery of a dangling record under mozgcp.net, the attacker registered the expired service (e.g., on a DNS provider like AWS Route 53 or a hosting platform). This allows redirection of the subdomain traffic to attacker-controlled infrastructure, enabling spoofing under Mozilla's domain.

## Requirements

1. Identification of the dangling record's provider (e.g., AWS, Heroku)
2. Account on the provider with registration privileges
3. No existing ownership conflicts

## Defense

Defensive measures and detection strategies:

- Monitor for new registrations on historical DNS targets
- Implement certificate transparency monitoring for subdomains
- Use automated alerts for changes in DNS resolutions

## Objectives

1. Gain control over the subdomain
2. Redirect traffic to controlled resources
3. Establish persistence for further exploitation

## Instructions

### Step 1: Identify Provider and Availability

**Context**: Determine the DNS record type and the service it points to, then check availability on the provider's site.

Search for the hostname in the provider's search interface.

### Step 2: Create Account and Register

**Context**: If available, sign up or log in to the provider and register the resource.

Follow the provider's onboarding to claim the subdomain alias.

### Step 3: Update DNS Configuration

**Context**: Point the new resource to your hosting setup.

Configure the service to serve content and verify resolution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[DNS]]
- [[registration]]
- [[subdomain-takeover]]
