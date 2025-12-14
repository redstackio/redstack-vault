---
tags:
  - ssrf-trigger
  - packet-transmission
  - metadata-exfil
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.124Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 03593bca-e631-49bf-a9f0-48a27a9f3b88
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger SSRF via Device Packet

## Summary

This procedure activates the SSRF by having a LoRaWAN device transmit a packet, causing the Helium server to request the configured internal AWS metadata endpoint and display the sensitive response in the console.

## Description

Once associated, device uplinks trigger the server to forward HTTP requests to the custom endpoint. Using the AWS metadata URL, this results in retrieval of EC2 instance details like instance ID, region, and IAM credentials. The response is embedded in the uplink message visible in the console, confirming exploitation. This demonstrates unauthorized internal access without direct server control.

## Requirements

1. Device associated with the malicious integration
2. Ability to trigger a device packet (physical device or simulator)
3. Access to console for monitoring uplinks
4. AWS backend environment with metadata service

## Defense

Defensive measures and detection strategies:

- Disable or sandbox custom integrations in production
- Proxy internal requests through a secure gateway that blocks metadata access
- Alert on HTTP requests to link-local IPs (169.254.x.x) from application servers
- Use IMDSv2 for AWS metadata to require session tokens

## Objectives

1. Initiate device transmission to proxy the SSRF request
2. Capture and view the metadata response
3. Validate unauthorized internal access

## Instructions

### Step 1: Prepare Device Transmission

**Context**: Ensure the device is ready to send an uplink packet.

If using a physical LoRaWAN device, power it on and configure for transmission (e.g., send a test payload).

> Alternatively, use Helium's device simulator if available in the console.

### Step 2: Trigger Packet Send

**Context**: Cause the server to process the uplink and issue the SSRF request.

Have the device transmit data via LoRaWAN (e.g., uplink message).

> The server receives the packet and makes a GET request to http://169.254.169.254/latest/meta-data.

### Step 3: Monitor and Retrieve Response

**Context**: Observe the exfiltrated data in the console.

Navigate to the device's uplink history in the console.

> Expected: Uplink message includes AWS metadata JSON (e.g., {"instance-id": "i-1234567890abcdef0"}); this confirms SSRF success.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf-trigger
- packet-transmission
- metadata-exfil
