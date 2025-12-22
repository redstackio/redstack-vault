---
tags:
  - reconnaissance
  - subdomain
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:38:39.877Z'
sub_techniques: []
id: 7f37ccbd-a6c9-4b72-aa12-6c85e88d7c6a
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Verify-Subdomain-Accessibility

## Summary

This procedure checks the accessibility of a target subdomain to identify potential misconfigurations, such as 'Not Found' errors indicating unused or dangling resources.

## Description

In subdomain takeover attacks, the first step is to verify if the subdomain is active. Accessing the URL via a browser reveals errors like 404, suggesting the backend service is no longer operational, which is a key indicator for further DNS investigation. This applies to web-based environments where DNS points to external services.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Public internet access to the target subdomain
3. No credentials needed

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsdumpster or subjack
- Monitor subdomain access logs for unusual 404 patterns
- Implement DNSSEC to prevent unauthorized claims

## Objectives

1. Confirm subdomain misconfiguration
2. Identify potential takeover vectors
3. Gather initial evidence for escalation

## Instructions

### Step 1: Access the Subdomain

**Context**: Navigate to the target subdomain to observe its response.

No command required; use a browser to visit https://brand.zen.ly/.

> This should display a 'Not Found' error, confirming the service is inactive.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[subdomain]]
