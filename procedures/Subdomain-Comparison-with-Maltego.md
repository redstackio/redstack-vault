---
id: proc-maltego-compare-zomato
tags:
  - osint
  - subdomain-compare
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
  - '[[Hardware]]'
updated_at: '2025-12-14T03:46:32.257Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Subdomain-Comparison-with-Maltego

## Summary

Compare Aquatone results with Maltego to validate and expand subdomain reconnaissance on Zomato.

## Description

Maltego provides link analysis; import Aquatone output and run transforms to note differences.

## Requirements

1. Maltego CE installed
2. Subdomain list from prior tool

## Defense

- Limit public entity exposure
- Monitor OSINT tool usage

## Objectives

1. Cross-verify subdomains
2. Identify additional links
3. Document variances

## Instructions

### Step 1: Import and Transform

**Context**: Load domains into Maltego graph.

Use GUI: Add entity 'Domain' for zomato.com, run 'To Subdomain' transform.

**Expected Output**: Graph with subdomains, differences from Aquatone.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Maltego]]

## Tags

- [[osint]]
- [[subdomain-compare]]
