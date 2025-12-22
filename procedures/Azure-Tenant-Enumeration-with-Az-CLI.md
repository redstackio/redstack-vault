---
id: b4c91da1-66f3-4550-8f5e-346c16e76dbf
name: Azure-Tenant-Enumeration-with-Az-CLI
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.024604+00:00'
updated_at: '2023-05-25T04:48:48.379198+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
platforms:
  - Cloud
tags:
  - '[[tags/az-cli]]'
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Enumerate tenant with az cli]]'
  - '[[tags/Enumeration]]'
commands:
  - '[[commands/az-login-with-username-password]]'
  - '[[commands/az-list-function-app-names]]'
  - '[[commands/az-list-key-vaults]]'
  - '[[commands/az-list-storage-accounts]]'
  - '[[commands/az-list-vm-names]]'
  - '[[commands/az-list-vms]]'
  - '[[commands/az-list-web-apps]]'
tools:
  - '[[tools/Azure-CLI]]'
validated: true
---

# Azure-Tenant-Enumeration-with-Az-CLI

## Summary

This procedure uses the Azure CLI (az-cli) to enumerate resources within an Azure tenant after authentication. It identifies key assets such as virtual machines, web apps, function apps, storage accounts, and key vaults, providing an attacker or red teamer with an overview of the tenant's infrastructure for further targeting.

## Description

Azure Tenant Enumeration with az-cli involves authenticating to an Azure subscription and querying the Azure Resource Manager (ARM) API via the command-line interface to discover deployed resources. This technique is useful in cloud environments for mapping the attack surface, identifying sensitive services like key vaults that may hold secrets, or spotting misconfigurations in storage and compute resources. It assumes the attacker has obtained valid credentials, such as through phishing or credential dumping, and requires the Azure CLI tool installed on the attacker's machine. The procedure focuses on listing resources in the current subscription, which can reveal the scope of access and potential lateral movement opportunities within the tenant.

## Requirements

1. Azure CLI installed and configured on the system (see [[tools/Azure-CLI]] for installation).
2. Valid Azure credentials (username and password) for a user account with at least Reader role in the target subscription.
3. Network access to Azure endpoints (no proxy issues blocking az-cli traffic).
4. PowerShell or bash environment for executing commands.

## Defense

- Implement least privilege with Azure RBAC, granting only necessary permissions to users and avoiding broad Reader roles.
- Monitor Azure Activity Logs and Sign-in Logs for unusual az-cli authentications or resource queries from unexpected IPs.
- Use multi-factor authentication (MFA) and conditional access policies to prevent credential-based logins.
- Enable Azure AD Privileged Identity Management (PIM) to just-in-time elevate permissions.

## Objectives

1. Authenticate to the Azure tenant using provided credentials.
2. Enumerate and list all discoverable resources in the subscription.
3. Identify potential high-value targets like key vaults and storage accounts for further exploitation.
4. Gather intelligence on the tenant's infrastructure layout.

## Instructions

### Step 1: Authenticate to Azure

**Context**: Begin by logging into the Azure tenant with the compromised credentials to establish a session for subsequent queries. This step verifies access and sets the context for the current subscription.

**Command** ([[commands/az-login-with-username-password]]):
```bash
az login -u $_USERNAME -p $_PASSWORD
```

This command prompts for interactive login but uses username/password for automation. Replace placeholders with actual values. If successful, it opens a browser for verification or directly authenticates.

### Step 2: List All Virtual Machines

**Context**: Query for all virtual machines (VMs) in the subscription to identify compute resources, which may serve as entry points for lateral movement or privilege escalation.

**Command** ([[commands/az-list-vms]]):
```bash
az vm list
```

This returns a JSON array of VM details including names, locations, and resource groups.

### Step 3: List Virtual Machine Names Only

**Context**: Extract just the names of VMs for a concise overview, useful for scripting or quick targeting without overwhelming output.

**Command** ([[commands/az-list-vm-names]]):
```bash
az vm list --query "[].[name]" -o table
```

This filters the output to a table of VM names only, making it easier to parse or reference.

### Step 4: List All Web Apps

**Context**: Enumerate web applications hosted in Azure App Service, which could expose web vulnerabilities or API endpoints for further testing.

**Command** ([[commands/az-list-web-apps]]):
```bash
az webapp list
```

This lists all web apps with details like hostnames and states.

### Step 5: List Function App Names

**Context**: Identify serverless function apps, which might contain custom code or integrations that can be abused for code execution or data access.

**Command** ([[commands/az-list-function-app-names]]):
```bash
az functionapp list --query "[].[name]" -o table
```

This provides a table of function app names for targeted follow-up.

### Step 6: List All Storage Accounts

**Context**: Discover storage accounts, which often hold sensitive data like blobs, files, or queues; check for public access or weak encryption.

**Command** ([[commands/az-list-storage-accounts]]):
```bash
az storage account list
```

This outputs storage account details including SKUs and locations.

### Step 7: List All Key Vaults

**Context**: Locate key vaults, critical for secret management; if accessible, they may yield certificates, keys, or passwords for escalation.

**Command** ([[commands/az-list-key-vaults]]):
```bash
az keyvault list
```

This lists key vaults with properties like vault URIs and access policies.
