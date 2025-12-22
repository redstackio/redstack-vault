---
tags:
  - azure
  - cloud
  - verification
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Azure
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:49.701Z'
sub_techniques: []
id: b39998c0-2a67-41de-84fb-5ed834eb0a6a
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify-Azure-Resource-Availability

## Summary

This procedure checks the availability of Azure Cloud App Virtual Machines via the portal API, confirming if resources pointed to by DNS records are unclaimed and exploitable for takeover.

## Description

Targeting resources like feuscspma3fcvapi.eastus.cloudapp.azure.com, this involves querying Azure's API in the eastus region to see if the VM is deregistered. No credentials are needed for public checks; success yields 'available: true', enabling registration. This step is crucial in cloud misconfiguration attacks to avoid false positives.

## Requirements

1. Azure portal access (browser-based)
2. Knowledge of the target resource name and region
3. API familiarity or CLI installation (optional)

## Defense

Defensive measures and detection strategies:

- Enable Azure Resource Manager locks on VMs to prevent unauthorized claims
- Monitor API queries for availability checks on legacy resources
- Integrate with SIEM for anomalous Azure portal activity

## Objectives

1. Confirm unclaimed status of the target Azure VM
2. Validate regional availability (e.g., eastus)
3. Prepare for registration without conflicts

## Instructions

### Step 1: Access Azure Portal API

**Context**: Use the Azure portal or CLI to query the specific Cloud App VM resource.

No CLI command specified; navigate to Azure portal > Virtual Machines > Search for feuscspma3fcvapi in eastus.

> The portal API response will show resource details; look for 'available: true' indicating no owner.

### Step 2: Interpret API Response

**Context**: Analyze the output for claimability.

If using CLI:
```bash
az resource list --resource-type "Microsoft.Compute/virtualMachines" --name "feuscspma3fcvapi" --location eastus
```

> Expected: Empty or available status, confirming the resource can be registered.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used


## Tools Used


## Tags

- [[azure]]
- [[cloud]]
- [[verification]]
