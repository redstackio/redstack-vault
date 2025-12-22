---
tags:
  - device-association
  - lorawan
  - ssrf-trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.126Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 6a993ed5-438b-4aac-81e4-1dede21df085
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Associate Integration with LoRaWAN Device

## Summary

This procedure links the malicious custom integration to an existing LoRaWAN device in the Helium organization, ensuring that device uplink packets route through the SSRF-configured endpoint.

## Description

In the Helium Console, devices can be tagged with integration labels to forward packet data to specified HTTP endpoints. Associating the SSRF integration label with a device prepares the environment for exploitation: when the device transmits, the server issues a request to the internal URL. This step is straightforward post-integration creation and requires no additional tools, but relies on an active device.

## Requirements

1. Created custom integration with a unique label
2. Active LoRaWAN device in the organization
3. Admin session access to Devices section

## Defense

Defensive measures and detection strategies:

- Audit device associations for suspicious labels or integrations
- Require approval workflows for integration-device links
- Monitor device packet forwarding logs for anomalous endpoints

## Objectives

1. Apply the integration label to a target device
2. Verify the association in device settings
3. Set up for packet-triggered SSRF

## Instructions

### Step 1: Navigate to Devices

**Context**: Access the device management interface.

From the dashboard, click on the 'Devices' tab.

> List of LoRaWAN devices appears; select one that is active and connected.

### Step 2: Select Device and Associate

**Context**: Link the SSRF integration to the device.

In the device details, find the integrations or labels section and apply the label (e.g., 'ssrf-test') from the custom integration.

> The association updates the device's configuration to use the endpoint for uplinks.

### Step 3: Confirm Association

**Context**: Validate the link to ensure readiness.

Refresh the device page and check that the integration label is listed.

> Expected: Label visible under device integrations; no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- device-association
- lorawan
- ssrf-trigger
