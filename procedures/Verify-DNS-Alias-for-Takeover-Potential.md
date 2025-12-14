---
tags:
  - subdomain-takeover
  - dns
  - cname
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.307Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 81ce786a-2b17-48b3-9bf6-bb43f6ef3117
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
---
# Verify DNS Alias for Takeover Potential

## Summary

This procedure confirms a subdomain's DNS CNAME points to an unowned third-party instance, like support.trendrr.tv to trendrr.zendesk.com, enabling takeover assessment.

## Description

Dangling CNAME records to inactive services create takeover vectors. By verifying the alias, attackers evaluate control potential, such as redirecting to phishing sites. Outcomes include proof for reporting or exploitation, highlighting misconfigurations in post-acquisition environments.

## Requirements

1. DNS lookup capability (browser tools or online services)
2. Target subdomain identified
3. Basic understanding of DNS records

## Defense

Defensive measures and detection strategies:

- Audit DNS for unused CNAMEs quarterly
- Remove or redirect abandoned records
- Use certificate transparency logs to monitor subdomains

## Objectives

1. Confirm CNAME to vulnerable service
2. Evaluate post-claim impacts
3. Document for PoC

## Instructions

### Step 1: Query DNS Records

**Context**: Inspect the subdomain's resolution.

Use browser dev tools (Network tab) or a site like dnsdumpster.com to check support.trendrr.tv's CNAME.

### Step 2: Assess Takeover Feasibility

**Context**: Determine if the alias allows claiming.

Verify it points to trendrr.zendesk.com and cross-reference with Zendesk's claim process.

**Expected Output**: CNAME record showing alias; screenshots of verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
