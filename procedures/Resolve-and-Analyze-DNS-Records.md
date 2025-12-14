---
id: proc-uuid-2
tags:
  - dns-resolution
  - cname-analysis
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-cname-resolve]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:10.836Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Resolve-and-Analyze-DNS-Records

## Summary

This procedure resolves DNS records for identified subdomains to uncover CNAME pointers to cloud services, revealing potential takeover vectors like AWS S3 endpoints.

## Description

DNS resolution exposes how subdomains are delegated, often via CNAME to services like S3. For Khan Academy subdomains, this reveals pointers to bucket endpoints. The attack scenario targets misconfigurations where services are retired but DNS lingers. Prerequisites include identified subdomains; outcomes are confirmed cloud dependencies.

## Requirements

1. Public DNS access
2. List of target subdomains
3. Tools for CNAME extraction

## Defense

Defensive measures and detection strategies:

- Automate DNS cleanup post-event
- Monitor for anomalous CNAME resolutions
- Use certificate transparency logs to track subdomain usage

## Objectives

1. Extract CNAME records
2. Identify cloud provider endpoints
3. Flag potential dangling pointers

## Instructions

### Step 1: Perform CNAME Lookup

**Context**: Query specifically for CNAME to see delegation targets.

**Command** ([[commands/dig-cname-resolve]]):
```bash
 dig +short CNAME healthyhackathon.khanacademy.org
```

> Returns the CNAME target, e.g., healthyhackathon.khanacademy.org.s3.amazonaws.com, indicating S3 usage. Analyze for S3 patterns.

### Step 2: Validate Resolution Chain

**Context**: Follow the CNAME to confirm the full pointer.

Use the same command on hackweek.khanacademy.org to reveal similar S3 endpoints.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/dig-cname-resolve]]

## Tools Used


## Tags

- [[dns-resolution]]
- [[cname-analysis]]
