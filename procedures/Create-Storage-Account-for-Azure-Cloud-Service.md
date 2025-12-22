---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - azure-storage
  - cloud-provisioning
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
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.794Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Storage Account for Azure Cloud Service

## Summary

This procedure provisions a storage account linked to the newly registered Azure Cloud Service, enabling persistent data and application support for the hijacked subdomain.

## Description

Azure Cloud Services require associated storage for deployments and runtime. After registering the domain, creating a storage account ensures the service can host applications. This step is crucial for the takeover, as it completes the infrastructure needed to serve content on the subdomain like svcgatewayus.starbucks.com.

## Requirements

1. Existing Azure Cloud Service
2. Azure subscription with storage permissions
3. Access to Azure Portal

## Defense

Defensive measures and detection strategies:

- Enable Azure Storage analytics and alerts for unusual provisioning
- Implement resource tagging and approval workflows
- Scan for orphaned storage post-deletion

## Objectives

1. Provide backend storage for the Cloud Service
2. Enable application deployment capabilities
3. Ensure hijacked subdomain functionality

## Instructions

### Step 1: Navigate to Storage Creation

**Context**: From the Cloud Service dashboard, initiate storage setup.

In Azure Portal, go to the created Cloud Service > Settings > Storage accounts > Add.

### Step 2: Provision Account

**Context**: Configure and create the storage account.

Name: e.g., hijackedstorage01 > Replication: Locally-redundant > Create.

> Expected: Storage account listed under the service, ready for use.

### Step 3: Link to Service

**Context**: Verify association.

Check Cloud Service configuration to confirm storage endpoint usage.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Azure-Portal]]

## Tags

- [[azure-storage]]
- [[subdomain-takeover]]
