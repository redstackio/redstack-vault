---
id: identify-cisco-sx80-device
tags:
  - reconnaissance
  - ip-lookup
  - asn
  - cisco
type: procedure
tools:
  - '[[tools/ipinfo-io]]'
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Network
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:31:31.082Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Exposed Cisco TelePresence Device

## Summary

This procedure uses IP information lookup services to identify and confirm the presence of a Cisco TelePresence SX80 device associated with a target Autonomous System Number (ASN), enabling scoping of the attack surface for video conferencing systems.

## Description

In scenarios involving networked hardware like Cisco's TelePresence endpoints, reconnaissance begins with querying public IP details to link addresses to organizational ownership. This step confirms if a discovered IP hosts an SX80 device, which is vulnerable to default credential exploits. Prerequisites include a suspected IP address from prior scanning or OSINT. Expected outcomes: Verification of device type and scope inclusion, setting up for direct interface access.

## Requirements

1. Access to an IP lookup tool like ipinfo.io
2. Known or suspected IP address of the target network
3. Target ASN details for scope confirmation

## Defense

Defensive measures and detection strategies:

- Implement network access controls to block unauthorized IP queries
- Monitor for anomalous reconnaissance traffic to public lookup services
- Use ASN-level filtering in firewalls to obscure organizational exposure

## Objectives

1. Confirm device identity and scope association
2. Gather preliminary network ownership data
3. Prepare for targeted exploitation of exposed endpoints

## Instructions

### Step 1: Query IP Information

**Context**: Use a web-based IP lookup to retrieve ASN and device association details.

Access [[tools/ipinfo-io]] and input the target IP (e.g., █████).

> This returns JSON or web output showing ASN ID (e.g., ██████) and potential device hints like hostname or organization.

### Step 2: Verify Device Type

**Context**: Cross-reference results to identify the SX80 web interface.

Locate the HTTPS endpoint (e.g., https://█████) from the IP and confirm via banner or title indicating Cisco TelePresence SX80.

> Successful verification shows the device is in-scope and exposed.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ipinfo-io]]

## Tags

- [[Reconnaissance]]
- [[ip-lookup]]
