---
tags:
  - dos
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: ab050e86-e112-461a-84d3-f3480ac611b4
created_at: '2025-12-11T06:10:22.278Z'
updated_at: '2025-12-11T06:10:22.278Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1499]]'
---
# Load Affected Pages to Trigger DoS

## Summary

This procedure involves accessing platform pages that query and render malicious data, causing slow loads, timeouts, or crashes due to processing oversized responses.

## Description

Pages like profiles, reports, and thanks pages on HackerOne fetch user data via GraphQL, including oversized filenames, leading to denial of service for users and programs accessing them.

## Requirements

1. Access to affected pages
2. Prior setup of malicious profiles
3. Optional: Burp Suite for monitoring

## Defense

Defensive measures and detection strategies:

- Implement caching and size limits on query responses
- Monitor for page load anomalies and browser crashes

## Objectives

1. Induce timeouts and crashes
2. Demonstrate widespread impact
3. Validate DoS effectiveness

## Instructions

### Step 1: Access Profile Pages

**Context**: Load pages that fetch user images.

Navigate to affected user profiles or reports pages.

> Observe slow loading due to large GraphQL responses.

### Step 2: Monitor with Tools

**Context**: Use Burp Suite to inspect responses.

Intercept traffic while loading pages to confirm oversized data.

> Confirm timeouts or crashes occur.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[dos]]
- [[web]]
