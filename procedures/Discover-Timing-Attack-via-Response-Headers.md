---
id: proc-885539-timing-discovery
tags:
  - timing-attack
  - side-channel
  - headers
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - GraphQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Scanning IP Blocks]]'
updated_at: '2025-12-14T17:26:00.363Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Scanning IP Blocks]]'
---
# Discover Timing Attack via Response Headers

## Summary

This procedure observes differences in the x-response-time header (10-20ms longer for valid private lists) to detect existence without direct content leaks.

## Description

During GraphQL queries, server processing for valid private list IDs involves additional checks or data fetching, causing measurable delays. Using Burp Suite, compare headers for known valid/invalid IDs. A 137ms example delay confirmed a private list. This side-channel enables efficient brute-forcing.

## Requirements

1. Proxy tool for header inspection.
2. Sample valid and invalid list IDs.
3. Timing measurement capability.

## Defense

Defensive measures and detection strategies:

- Normalize response times with padding or caching.
- Disable or obfuscate timing-revealing headers.
- Detect rapid sequential queries for timing probes.

## Objectives

1. Identify timing differentials.
2. Validate side-channel for ID detection.
3. Enable targeted brute-force.

## Instructions

### Step 1: Monitor Headers for Test Queries

**Context**: Send requests for known non-existent and private list IDs.

Use Burp to capture x-response-time on POST to ListMembers.

**Expected Output**: ~50ms for invalid, 60-70ms for valid.

### Step 2: Measure and Compare

**Context**: Repeat with variations to confirm pattern.

Log times and calculate averages.

**Expected Output**: Consistent 10-20ms delta.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Scanning IP Blocks]] Gather Victim Org Information: Credentials (adapted for timing)

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[timing-attack]]
- [[side-channel]]
