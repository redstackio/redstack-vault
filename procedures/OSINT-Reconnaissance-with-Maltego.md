---
id: proc-maltego-osint-927413
tags:
  - osint
  - link-analysis
type: procedure
tools:
  - '[[tools/Maltego]]'
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
updated_at: '2025-12-14T17:27:35.648Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# OSINT-Reconnaissance-with-Maltego

## Summary

Maltego performs OSINT and link analysis to compare subdomain results from tools like Aquatone, gathering broader intel on Zomato.

## Description

Maltego visualizes relationships between domains, IPs, and entities. Here, it's used to cross-verify subdomain findings, noting differences and expanding recon scope without direct interaction.

## Requirements

1. Maltego Community Edition installed
2. API keys for transforms (optional)
3. Target domain

## Defense

Defensive measures and detection strategies:

- Limit public OSINT exposure
- Monitor for entity graphing tools

## Objectives

1. Visualize domain relationships
2. Compare enum results
3. Uncover additional targets

## Instructions

### Step 1: Create Graph

**Context**: Start a new investigation in Maltego.

Add entity for 'Domain' zomato.com and run transforms like 'To Subdomain'.

> Builds graph showing linked subdomains and differences from Aquatone.

### Step 2: Analyze Results

**Context**: Review and export findings.

Export graph; note variances in subdomain lists.

> Expected: Enhanced recon data.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Maltego]]

## Tags

- [[osint]]
- [[link-analysis]]
