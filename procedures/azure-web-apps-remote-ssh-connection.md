---
id: 8d0da02b-a656-42cd-bd5a-5bd20843de9b
name: azure-web-apps-remote-ssh-connection
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.424582+00:00'
updated_at: '2023-05-24T21:55:54.554593+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
platforms:
  - Cloud
  - Azure
tags:
  - '[[tags/Azure Web App]]'
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Spawn SSH for Azure Web App]]'
  - '[[tags/SSH]]'
commands:
  - '[[commands/az-webapp-create-remote-connection]]'
tools:
  - '[[tools/azure-cli]]'
validated: true
---

# azure-web-apps-remote-ssh-connection

## Summary

This procedure demonstrates how to establish a remote SSH connection to an Azure Web App using the Azure CLI, enabling persistent access for executing commands, deploying code, or managing configurations on the target application. It assumes prior authentication and access to the Azure subscription containing the Web App, making it useful for lateral movement or maintaining access in cloud environments.

## Description

In Azure, Web Apps can be accessed remotely via SSH for administrative purposes, but attackers with compromised credentials can abuse this feature to gain shell access to the app's runtime environment. This procedure uses the `az webapp create-remote-connection` command to spawn an SSH tunnel, which forwards a local port to the Web App's SSH endpoint. Once connected, an attacker can SSH to localhost on the forwarded port to interact with the app's file system and processes. This technique is particularly effective after initial access via credential compromise or misconfiguration exploitation, allowing for data exfiltration, code injection, or further pivoting within the Azure tenant. The target environment is Azure App Service (Web Apps), and success depends on having contributor or owner roles on the resource.

## Requirements

1. Azure CLI installed and authenticated with `az login` using compromised or valid credentials that have access to the target subscription.
2. Knowledge of the target Web App's subscription ID, resource group name, and app service name.
3. Network access to Azure APIs (no direct inbound access to the Web App required).
4. Local SSH client available to connect to the forwarded port.

## Defense

- Restrict access to Azure Web Apps by implementing role-based access control (RBAC) and limiting SSH enablement to necessary scenarios.
- Monitor Azure Activity Logs and Web App diagnostics for unauthorized `create-remote-connection` API calls or unusual SSH activity.
- Enable Azure Defender for App Service to detect anomalous access patterns and enforce just-in-time access policies.
- Regularly audit and rotate credentials, and use Azure Private Link to restrict public API exposure.

## Objectives

1. Leverage obtained Azure credentials to target and connect to the Web App remotely.
2. Establish an SSH session for unauthorized control over the Web App environment.
3. Maintain persistent access for ongoing operations like data theft or configuration changes.

## Instructions

### Step 1: Authenticate to Azure (if not already done)

**Context**: Ensure the Azure CLI session is authenticated with credentials that have sufficient permissions on the target Web App. This step is prerequisite for API access.

Use the Azure CLI login command to authenticate interactively or with service principal.

> Note: If using service principal, provide tenant ID, client ID, and secret as parameters.

### Step 2: Create Remote SSH Connection

**Context**: Execute the command to initiate an SSH tunnel to the Web App. This binds a local port (default 8000 or specified) to the app's SSH service, allowing connection via `ssh -p <local-port> root@localhost`.

**Command** ([[commands/az-webapp-create-remote-connection]]):
```bash
az webapp create-remote-connection --subscription $_SUBSCRIPTION_ID --resource-group $_RESOURCE_GROUP_NAME -n $_APP_SERVICE_NAME
```

> This command creates a secure tunnel. Replace placeholders with actual values. The output includes connection details like the local port. Once running, open a new terminal and connect with SSH to the forwarded port to access the Web App shell. Press Ctrl+C to terminate the tunnel when done. Success is indicated by the tunnel starting without errors and successful SSH login.
