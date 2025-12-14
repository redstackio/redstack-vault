---
tags:
  - subdomain-takeover
  - reconnaissance
  - acquisition
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
updated_at: '2025-12-14T05:32:23.318Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 20c6001d-8041-4e4d-961e-69bc08278cba
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Abandoned Subdomains Post-Acquisition

## Summary

This procedure involves researching domain acquisition history and manually checking subdomain status to identify remnants like support.trendrr.tv that were not properly decommissioned after Twitter's shutdown of Trendrr.tv domains.

## Description

In scenarios where a company acquires another and shuts down legacy domains, subdomains pointing to third-party services like Zendesk may be overlooked. This procedure targets such misconfigurations by verifying active subdomains, enabling subdomain takeover attacks where an attacker claims control under the parent domain (e.g., Twitter). Expected outcomes include discovering vulnerable aliases for further exploitation, such as traffic redirection or phishing.

## Requirements

1. Public internet access for domain queries
2. Knowledge of target acquisition events (e.g., via news or WHOIS)
3. Web browser for manual verification

## Defense

Defensive measures and detection strategies:

- Regularly audit and decommission all subdomains post-acquisition
- Monitor DNS records for dangling CNAMEs to third-party services
- Use automated tools like subdomain scanners to identify orphans

## Objectives

1. Locate active subdomains on defunct domains
2. Confirm non-shutdown status for takeover potential
3. Map legacy service integrations

## Instructions

### Step 1: Research Domain History

**Context**: Gather background on the target's domain shutdowns and acquisitions to prioritize subdomains.

Review public sources for events like Twitter's acquisition of Trendrr.tv and subsequent domain decommissioning. Focus on common subdomains like 'support', 'help', or 'api'.

### Step 2: Check Subdomain Status

**Context**: Manually verify if subdomains resolve and load content.

Visit support.trendrr.tv in a browser or use a DNS lookup tool to check resolution. Note if it aliases to trendrr.zendesk.com while the main domain is inactive.

**Expected Output**: Active resolution to a third-party service page.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[Reconnaissance]]
