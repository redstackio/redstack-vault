---
tags:
  - domain
  - whois
  - availability
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/DomainTools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.789Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 0a3bc741-496b-44d8-8274-b97c5189a5c7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Domain Availability for Takeover

## Summary

This procedure checks the registration status of a domain identified as a CNAME target to confirm if it can be purchased for subdomain takeover, allowing control over the aliased subdomain.

## Description

Following CNAME enumeration, this step uses WHOIS and domain status checks to verify if the target domain (e.g., recommendation.us) is unregistered or lapsing. If available, an attacker can register it via a registrar like GoDaddy, inheriting the subdomain's traffic. This targets environments with DNS misconfigurations in web applications. Prerequisites: Access to domain lookup services. Outcomes: Confirmation of takeover feasibility, leading to reputation risks like phishing site hosting.

## Requirements

1. Access to WHOIS and domain search tools
2. The CNAME target domain name from prior enumeration
3. Optional: Account with a domain registrar for purchase simulation

## Defense

Defensive measures and detection strategies:

- Proactively register all CNAME target domains or use internal ones
- Use subdomain takeover scanners like Sublist3r or Takeover in CI/CD pipelines
- Set up monitoring for subdomain traffic anomalies post-takeover

## Objectives

1. Confirm domain availability
2. Assess takeover risk
3. Prepare for exploitation or reporting

## Instructions

### Step 1: Perform WHOIS Lookup

**Context**: Query registration details to check if the domain is owned, expired, or available.

Use [[tools/DomainTools]] WHOIS search:

Enter the domain (e.g., recommendation.us) in the WHOIS tool.

> Output shows registrar, creation date, and status; availability is indicated by no active registration.

### Step 2: Check Domain Status and DNS

**Context**: Verify no active hosting or DNS records that might indicate ownership.

Use DomainTools domain info and DNS sections to inspect for active records.

> Success if no NS/A records and status confirms purchase availability; this enables immediate registration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/DomainTools]]

## Tags

- [[WHOIS]]
- [[domain-takeover]]
