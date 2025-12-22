---
id: proc-claim-azure-service
tags:
  - azure
  - infrastructure
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/Azure-Portal]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Azure
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Virtual Private Server]]'
updated_at: '2025-12-14T04:38:49.773Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Virtual Private Server]]'
---
# Claim-Azure-Cloud-Service-with-Dangling-Name

## Summary

This procedure claims an unowned Azure Cloud Service name derived from a dangling CNAME record, allowing the attacker to control DNS resolution for the target subdomain.

## Description

Targeting Azure's classic Cloud Services, this step registers a new service using the exact name from the CNAME (e.g., 3edbac0a-5c43-428a-b451-a5eb268f888b). Performed via the Azure Portal, it exploits the fact that deleted services leave names available for reuse. Prerequisites include an Azure subscription. Outcomes include ownership of the service, enabling deployment of content that resolves under the victim's subdomain.

## Requirements

1. Active Azure subscription with permissions to create Cloud Services (classic)
2. Identified dangling CNAME name from prior enumeration
3. Access to Azure Portal

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected Cloud Service creations in Azure logs
- Use Azure Policy to restrict classic Cloud Service deployments
- Audit and delete dangling DNS records promptly after resource decommissioning

## Objectives

1. Acquire control over the cloud infrastructure tied to the CNAME
2. Enable DNS hijacking for the subdomain
3. Prepare for payload deployment

## Instructions

### Step 1: Access Azure Portal

**Context**: Log in and navigate to create a new Cloud Service.

**Instructions**: Go to https://portal.azure.com, search for "Cloud Services (classic)", and select "Create".

> Enter the subscription, resource group, and service name matching the dangling CNAME (without .cloudapp.net).

### Step 2: Configure and Deploy Initial Package

**Context**: Complete the creation wizard with minimal configuration to claim the name.

**Instructions**: Provide a DNS name prefix (reuse the service name), select a region, and upload an empty or basic .cspkg package. Submit to create the service.

> Wait for deployment; DNS propagation may take 5-10 minutes. Verify by re-running dig on the subdomain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Virtual Private Server]] Acquire Infrastructure: Virtual Private Server

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Azure-Portal]]

## Tags

- [[azure]]
- [[infrastructure]]
- [[subdomain-takeover]]
