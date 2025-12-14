---
tags:
  - azure-registration
  - resource-takeover
  - cloud
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Cloud (Azure)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.001Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: cb971d6b-59af-4757-8989-c087e536a67f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register Unclaimed Azure App Service

## Summary

This procedure claims an unclaimed Azure App Service by creating a new Web App with the dangling resource's name, gaining control over the associated subdomain.

## Description

Azure App Services are globally unique by name. Registering s00397nasv101-datacafe-cert provisions the resource under the attacker's account, redirecting the CNAME traffic. This enables serving arbitrary content on the subdomain.

## Requirements

1. Active Azure subscription (free tier works)
2. Azure CLI or portal access
3. Exact unclaimed name from verification

## Defense

Defensive measures and detection strategies:

- Pre-register all potential App Service names in use
- Enable Azure Defender for cloud resource monitoring
- Alert on new App Service creations matching known patterns

## Objectives

1. Provision the resource successfully
2. Redirect DNS traffic to attacker-controlled instance
3. Establish subdomain control

## Instructions

### Step 1: Login to Azure CLI

**Context**: Authenticate to Azure for resource creation.

**Command** ([[commands/az-login]]):

```bash
az login
```

> Prompts for authentication; select subscription.

### Step 2: Create Web App

**Context**: Deploy the App Service with the target name.

**Command** ([[commands/az-webapp-create]]):

```bash
az webapp create --resource-group myGroup --plan myPlan --name s00397nasv101-datacafe-cert --runtime "DOTNET|6.0"
```

> Confirms creation; name uniqueness ensures takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/az-login]]
- [[commands/az-webapp-create]]

## Tools Used

- Azure CLI

## Tags

- [[azure-registration]]
- [[resource-takeover]]
