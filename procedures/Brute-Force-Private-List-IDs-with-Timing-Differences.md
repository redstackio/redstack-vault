---
id: proc-885539-timing-brute-force
tags:
  - brute-force
  - timing-attack
  - enumeration
type: procedure
tools:
  - '[[tools/AWS-EC2]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - GraphQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:26:00.360Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Vulnerability Scanning]]'
---
# Brute-Force Private List IDs with Timing Differences

## Summary

This procedure deploys a Ruby script (twileak.rb) on AWS EC2 to generate snowflake IDs, query ListMembers, and use x-response-time delays to identify valid private lists.

## Description

The script iterates over potential IDs, measures response times, and flags delays >100ms as valid. Deployed on EC2 for scalability, it successfully detected a private list with 137ms delay. Combines brute-force with side-channel exploitation for efficient enumeration.

## Requirements

1. Ruby script for ID generation and timing.
2. AWS EC2 instance with network access.
3. Authenticated Twitter API token.

## Defense

Defensive measures and detection strategies:

- Add noise to response times or use constant-time processing.
- Rate-limit timing-sensitive queries.
- Monitor EC2-like deployments probing APIs.

## Objectives

1. Generate and test thousands of IDs.
2. Detect valid private lists via delays.
3. Obtain exploitable list IDs.

## Instructions

### Step 1: Develop and Deploy Script

**Context**: Write twileak.rb to loop IDs and parse headers.

Upload to EC2 and run: ruby twileak.rb --start-timestamp [epoch] --range 10000.

**Expected Output**: Logs of response times.

### Step 2: Execute Brute-Force

**Context**: Run on EC2 for parallel processing.

Monitor for delays exceeding threshold.

**Expected Output**: Valid ID like "1234567890" with 137ms.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery
- [[Vulnerability Scanning]] Gather Victim Org Information: Domains

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- [[tools/AWS-EC2]]

## Tags

- [[brute-force]]
- [[timing-attack]]
