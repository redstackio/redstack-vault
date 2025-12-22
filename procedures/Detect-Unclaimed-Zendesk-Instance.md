---
tags:
  - subdomain-takeover
  - zendesk
  - unclaimed
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
updated_at: '2025-12-14T05:32:23.313Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: e3e77268-d98b-4ab1-b1f3-7c8064dddde8
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Detect Unclaimed Zendesk Instance

## Summary

This procedure accesses a suspected subdomain to confirm it hosts an unclaimed Zendesk help desk, as seen with support.trendrr.tv displaying a claim-available message.

## Description

Zendesk subdomains left unclaimed after service decommissioning allow attackers to sign up and take control, potentially hijacking traffic under a trusted domain like Twitter's. This involves direct URL access to observe availability indicators, with outcomes including immediate takeover feasibility for malicious content hosting.

## Requirements

1. Web browser access
2. Identified target subdomain from prior recon
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Decommission third-party services fully post-acquisition
- Scan for unclaimed instances using service-specific tools
- Implement DNS sinkholing for abandoned records

## Objectives

1. Confirm unclaimed status
2. Identify claim process
3. Assess immediate takeover risk

## Instructions

### Step 1: Access Subdomain

**Context**: Load the subdomain to inspect content.

Navigate to support.trendrr.tv and read the displayed message.

### Step 2: Validate Claim Availability

**Context**: Look for explicit indicators of takeover opportunity.

Observe text like 'No help desk at support.trendrr.tv... available and that you can claim it at www.zendesk.com/signup'.

**Expected Output**: Clear claim invitation from Zendesk.

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
- [[zendesk]]
