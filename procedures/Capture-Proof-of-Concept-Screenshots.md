---
tags:
  - subdomain-takeover
  - poc
  - screenshots
type: procedure
tools:
  - '[[tools/Grabilla]]'
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
updated_at: '2025-12-14T05:32:23.303Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c869786b-fabf-4a60-b5e2-cacd46bff247
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Capture Proof-of-Concept Screenshots

## Summary

This procedure documents the subdomain takeover vulnerability using screenshots of the unclaimed Zendesk page and DNS details, as done with Grabilla for support.trendrr.tv.

## Description

Visual evidence strengthens vulnerability reports or exploit demos. Capturing the claim message and alias confirmation proves the issue without execution, aiding in responsible disclosure to platforms like HackerOne.

## Requirements

1. Screenshot tool like Grabilla
2. Access to vulnerable page and DNS info
3. Annotation capability for clarity

## Defense

Defensive measures and detection strategies:

- N/A (documentation step)
- Monitor for anomalous subdomain access logs

## Objectives

1. Visually prove unclaimed status
2. Capture DNS verification
3. Prepare for reporting

## Instructions

### Step 1: Screenshot Unclaimed Page

**Context**: Record the Zendesk availability message.

Load support.trendrr.tv and use Grabilla to capture the full page showing the claim text.

### Step 2: Document DNS Alias

**Context**: Evidence the CNAME configuration.

Capture a DNS lookup result or browser network tab showing the alias to trendrr.zendesk.com.

**Expected Output**: Annotated images of page and DNS.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Grabilla]]

## Tags

- [[subdomain-takeover]]
- [[poc]]
