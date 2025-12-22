---
tags:
  - dos
  - data-upload
  - crashplan
  - storage-exhaustion
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Network Denial of Service]]'
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Direct Network Flood]]'
id: 19f73bb8-f5ff-4855-bb63-c7197db342c7
created_at: '2025-12-14T17:26:30.450Z'
updated_at: '2025-12-14T17:26:30.450Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Remote File Copy]]'
---
# Upload-Malicious-Data-to-CrashPlan-for-DoS

## Summary

Using a discovered CrashPlan friend code, this procedure uploads large volumes of arbitrary data to the target server (e.g., backup.uber.com:443), exhausting storage and causing denial-of-service for legitimate backups.

## Description

Once authorized via the friend code, the CrashPlan client allows inbound backups from external sources. Attackers can generate and upload dummy files (e.g., multi-GB archives) in parallel sessions to fill quotas rapidly. This targets web-based backup services without upload limits. Prerequisites: Valid friend code and CrashPlan client software. Outcome: Server storage saturation, blocking Uber employee backups.

## Requirements

1. CrashPlan client configured with the friend code
2. Large data sources (e.g., file generators)
3. Multiple machines for parallel uploads

## Defense

Defensive measures and detection strategies:

- Set strict upload quotas and monitor storage usage
- Validate inbound connections against trusted IPs
- Alert on sudden spikes in backup volume from unknown sources

## Objectives

1. Initiate unauthorized backups
2. Exhaust server storage resources
3. Disrupt legitimate backup operations

## Instructions

### Step 1: Configure Client with Friend Code

**Context**: Authorize the external client to connect to Uber's server.

Install CrashPlan client, enter the brute-forced friend code during setup, and point to backup.uber.com:443 as the destination.

> Expected output: Client connects successfully, ready for backups.

### Step 2: Generate and Upload Data

**Context**: Flood the server with data to cause DoS.

Create large files (e.g., using dd or file fillers) and initiate backup jobs. Run multiple instances to upload concurrently.

> Expected output: Uploads progress, server storage fills; eventual quota errors for new sessions.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques

- [[Direct Network Flood]] Direct Network Flood

## Commands Used


## Tools Used


## Tags

- [[dos]]
- [[storage-exhaustion]]
