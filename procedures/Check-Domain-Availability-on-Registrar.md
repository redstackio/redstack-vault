---
id: proc-uuid-2
tags:
  - domain-check
  - availability
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
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:39.840Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Check-Domain-Availability-on-Registrar

## Summary

This procedure involves manually searching a domain registrar's website to confirm if a domain (identified from a dangling CNAME) is available for registration, enabling potential takeover.

## Description

After identifying a dangling CNAME, verify the pointed-to domain's status on public registrars. This step is crucial for subdomain takeover as it confirms exploitability. Target registrars like GoDaddy for .us or .com TLDs. No technical tools beyond a browser are needed, but results inform the decision to register. Expected outcomes: Clear indication of availability, paving the way for malicious registration.

## Requirements

1. Web browser with internet access
2. The dangling domain name from prior DNS lookup
3. Knowledge of common registrars (e.g., GoDaddy, Namecheap)

## Defense

Defensive measures and detection strategies:

- Monitor all referenced domains in DNS for registration status using services like DomainTools
- Automate availability checks with APIs from registrars
- Enforce policy to remove dangling DNS entries promptly

## Objectives

1. Confirm domain is unregistered
2. Assess feasibility of takeover
3. Document availability for reporting or exploitation

## Instructions

### Step 1: Search Domain on Registrar Site

**Context**: Navigate to a registrar and perform a domain search to check availability.

No command; use web browser:

1. Open browser and go to https://www.godaddy.com/domainsearch
2. Enter the dangling domain (e.g., example-domain.us)
3. Submit the search

> The page will display if the domain is available, showing purchase options. If taken, it lists alternatives or ownership hints.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[domain-availability]]
- [[Reconnaissance]]
