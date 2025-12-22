---
tags:
  - azure
  - cloud-verification
  - resource-check
type: procedure
tools:
  - '[[tools/Azure-CLI]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/az-traffic-manager-list]]'
verified: false
platforms:
  - Azure
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:49.820Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2353b090-c48c-453b-bd9d-05b30ec40f69
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify Unclaimed Azure Traffic Manager Profile

## Summary

This procedure checks if an Azure Traffic Manager profile referenced by a dangling DNS CNAME is unclaimed or abandoned. By querying Azure resources via the portal or CLI, attackers confirm availability for takeover, ensuring the subdomain can be hijacked without conflicts.

## Description

Attackers extract the profile name from the CNAME (e.g., mydailydev.trafficmanager.net) and use Azure tools to search for existing resources. If none exist across subscriptions, the name is available for creation. This step targets Azure's global namespace for Traffic Manager DNS names, which are unique. Prerequisites: Azure CLI installed and logged in (for API access), or browser access to the Azure portal. Outcomes: Confirmation of claimability, paving the way for resource creation.

## Requirements

1. Azure CLI installed and authenticated (az login)
2. The exact unique DNS name from the CNAME record
3. Permissions to query Azure resources (read access)

## Defense

Defensive measures and detection strategies:

- Use Azure Resource Graph to audit for unused Traffic Manager profiles
- Enable Azure Defender for Cloud to monitor for anomalous resource creations
- Implement naming conventions and automate cleanup of dangling cloud records

## Objectives

1. Confirm the absence of the target Azure Traffic Manager profile
2. Validate that the DNS name is available for registration
3. Assess takeover feasibility without alerting defenders

## Instructions

### Step 1: Login to Azure CLI

**Context**: Authenticate to access Azure APIs for resource queries.

**Command**:
```bash
az login
```

> This opens a browser for authentication. Expected output: JSON with subscription details.

### Step 2: Query for Traffic Manager Profiles

**Context**: Search for profiles matching the dangling name to verify unclaimed status.

**Command** ([[commands/az-traffic-manager-list]]):
```bash
az network traffic-manager profile list --query "[?dnsConfig.uniqueDnsName=='mydailydev.trafficmanager.net']" --output table
```

> If no results or empty array, the profile is unclaimed. Use --resource-group if scoped, but global search may require scripting across subscriptions.

### Step 3: Manual Portal Check

**Context**: As a fallback, use the Azure portal for visual confirmation.

Navigate to Azure Portal > Traffic Manager profiles > Search for "mydailydev". If no profile appears, it's available.

> Expected: No matching resource found.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domain Name

### Sub-Techniques

-

## Commands Used

- [[commands/az-traffic-manager-list]]

## Tools Used

- [[tools/Azure-CLI]]

## Tags

- [[azure]]
- [[cloud-verification]]
- [[resource-check]]
