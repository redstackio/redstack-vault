---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - reconnaissance
  - acquisitions
  - domain-discovery
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
updated_at: '2025-12-14T04:51:26.483Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Research-Company-Acquisitions-for-Domain-Takeover

## Summary

This procedure involves querying public databases to identify domains associated with company acquisitions, uncovering potential dangling DNS records left unmaintained post-acquisition for domain takeover opportunities.

## Description

In scenarios like Snapchat's acquisition of Obvious Engineering, original domains such as obviousengine.com may retain outdated DNS configurations pointing to services like GitHub Pages. This reconnaissance step uses free resources like Crunchbase to map acquisitions to domains, setting the stage for takeover exploitation. Prerequisites include internet access and basic research skills; outcomes include a list of candidate domains for further probing.

## Requirements

1. Access to acquisition databases like Crunchbase
2. Web browser for searching and reviewing profiles
3. Knowledge of the target company's acquisition history

## Defense

Defensive measures and detection strategies:

- Regularly audit acquired domains and update/remove DNS records
- Monitor for unauthorized GitHub repository creations matching owned domains
- Use domain monitoring services to alert on resolution changes

## Objectives

1. Discover abandoned domains from acquisitions
2. Identify potential takeover vectors via service pointers
3. Prioritize high-value targets like those linked to major companies

## Instructions

### Step 1: Query Acquisition Databases

**Context**: Search for the target company's (e.g., Snapchat) acquisitions to find associated domains.

Navigate to Crunchbase and search for "Snapchat acquisitions". Review results, such as Obvious Engineering at https://www.crunchbase.com/organization/obvious-engineering#section-overview, noting the domain obviousengine.com.

### Step 2: Document Candidate Domains

**Context**: Compile a list of domains for validation.

Record domains like obviousengine.com, along with acquisition details, in a notes file or spreadsheet for the next steps.

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
- [[acquisitions]]
- [[domain-discovery]]
