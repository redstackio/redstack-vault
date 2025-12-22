---
id: p2b3c4d5-e6f7-8901-bcde-f23456789012
tags:
  - azure
  - traffic-manager
  - verification
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Cloud (Microsoft Azure)
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T04:38:49.555Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Verify-Unregistered-Azure-Traffic-Manager-Profile

## Summary

This procedure checks if an Azure Traffic Manager profile referenced by a dangling CNAME is unregistered, confirming availability for takeover.

## Description

After identifying a CNAME like s00149tmppcrpt.trafficmanager.net, verify its status in Azure. If deleted without updating DNS, it's claimable, leading to subdomain control. This step uses Azure's public interfaces to probe without authentication.

## Requirements

1. Web browser access to Azure portal
2. Azure CLI (optional) for programmatic checks
3. Knowledge of the endpoint name

## Defense

Defensive measures and detection strategies:

- Automate cloud resource audits to detect expired services
- Integrate DNS and cloud API monitoring for discrepancies
- Use Azure Advisor for dangling resource alerts

## Objectives

1. Confirm profile deletion or expiration
2. Validate takeover feasibility
3. Document the vulnerability

## Instructions

### Step 1: Search Azure Portal

**Context**: Log in to Azure (or use incognito for public search) and search for the profile to see if it exists.

Navigate to portal.azure.com, search for "s00149tmppcrpt", and check for existence.

> If no profile appears, it's unregistered.

### Step 2: Use Azure CLI Check (Optional)

**Context**: For scripted verification, attempt to describe the resource.

No command provided; use `az network traffic-manager profile show --name s00149tmppcrpt --resource-group <group>` which fails if unregistered.

> Expected error: Resource not found.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Gather Victim Network Information: DNS

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[azure]]
- [[traffic-manager]]
- [[verification]]
