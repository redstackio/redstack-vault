---
tags:
  - proof-archiving
  - evidence-preservation
type: procedure
tools:
  - '[[tools/Wayback-Machine]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Archive via Utility]]'
updated_at: '2025-12-14T04:51:26.761Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c6c088a3-ead2-4489-a299-03f96836390f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Archive via Utility]]'
---
# Archive-Takeover-Proof-with-Wayback-Machine

## Summary

This procedure archives a snapshot of the taken-over subdomain to preserve proof of control for reporting purposes.

## Description

Using the Internet Archive's Wayback Machine, attackers capture the hosted content without direct interaction that might alert the target. In the scenario, this snapshots the HTML with HackerOne link. Outcomes: Timestamped evidence.

## Requirements

1. Public access to the subdomain
2. Wayback Machine account (optional)

## Defense

Defensive measures and detection strategies:

- Monitor archive.org for snapshots of your domains
- Use robots.txt to discourage archiving sensitive subdomains
- Rapid response to takeover reports to remove content

## Objectives

1. Preserve takeover evidence
2. Provide verifiable proof
3. Avoid direct notification

## Instructions

### Step 1: Submit Snapshot

**Context**: Request archive of the controlled subdomain.

No command; go to https://web.archive.org/ and enter http://svcardproxydevus.starbucks.com/ to save.

> Creates a snapshot, e.g., on 2018-07-10, capturing the HTML comment with profile link.

### Step 2: Verify Archive

**Context**: Confirm the snapshot includes the proof.

Browse the archived URL to check content preservation.

> Expected: Full page with malicious/hosted elements visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Archive via Utility]] Archive Collected Data: Archive via Library

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Wayback-Machine]]

## Tags

- [[proof-archiving]]
