---
id: proc-uuid-4
tags:
  - dos
  - resource-exhaustion
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T05:32:10.117Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Execute DoS Attack with Multiple Simultaneous Uploads

## Summary

This procedure launches a denial-of-service attack by concurrently uploading large files (2.52 GB each) from multiple browser instances, exhausting server memory and causing temporary unavailability.

## Description

Exploiting the unrestricted upload, open several browser tabs or instances to initiate parallel uploads, overwhelming the server with data processing, potentially triggering memory leaks or overflows in the PHP application.

## Requirements

1. Multiple browser instances (e.g., 6 tabs/windows)
2. Large files ready (2.52 GB each)
3. Target upload endpoint accessible

## Defense

Defensive measures and detection strategies:

- Implement upload rate limiting and concurrency controls
- Use resource quotas per user/session
- Deploy WAF rules to block excessive uploads

## Objectives

1. Induce server resource exhaustion
2. Render site unresponsive
3. Demonstrate DoS impact

## Instructions

### Step 1: Setup Multiple Instances

**Context**: Prepare browsers for parallel attacks.

Open 6 instances of the upload page (e.g., https://staging.uzbey.com/user/406/edit).

> Ensure each is ready to upload independently.

### Step 2: Initiate Simultaneous Uploads

**Context**: Start uploads concurrently to maximize load.

In each instance, select and submit a 2.52 GB file at the same time.

> Expected: After minutes, site slows and goes offline due to overload.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques

- [[OS Exhaustion Flood]]

## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- [[dos]]
- [[resource-exhaustion]]
