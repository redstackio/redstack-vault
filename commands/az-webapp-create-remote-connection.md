---
id: 1b9f109d-fe5e-4cd5-9b34-7ec05a7adba4
name: az-webapp-create-remote-connection
type: command
executor: bash
data: >-
  az webapp create-remote-connection --subscription $_SUBSCRIPTION_ID
  --resource-group $_RESOURCE_GROUP_NAME -n $_APP_SERVICE_NAME
output: null
created_at: '2023-05-24T21:54:19.190472+00:00'
updated_at: '2023-05-24T21:54:19.220258+00:00'
platforms:
  - Cloud
  - Azure
tags:
  - azure
  - ssh
  - webapp
verified: true
validated: true
---

# az-webapp-create-remote-connection

## Command

```bash
az webapp create-remote-connection --subscription $_SUBSCRIPTION_ID --resource-group $_RESOURCE_GROUP_NAME -n $_APP_SERVICE_NAME
```

## Description

This command creates a remote debugging connection (SSH tunnel) to an Azure Web App, allowing secure shell access to the app's containerized environment. It is used for troubleshooting or administrative access but can be abused for persistent remote control. The command must be run from an authenticated Azure CLI session with appropriate permissions on the Web App resource.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --subscription $_SUBSCRIPTION_ID | The Azure subscription ID containing the Web App | Yes |
| --resource-group $_RESOURCE_GROUP_NAME | The resource group name hosting the Web App | Yes |
| -n $_APP_SERVICE_NAME | The name of the target App Service (Web App) | Yes |
| --port $_LOCAL_PORT | Optional local port for the SSH tunnel (default: 8000) | No |

## Examples

### Basic Usage

```bash
az webapp create-remote-connection --subscription 12345678-1234-1234-1234-1234567890ab --resource-group myResourceGroup -n myWebApp
```

### Advanced Usage with Custom Port

```bash
az webapp create-remote-connection --subscription 12345678-1234-1234-1234-1234567890ab --resource-group myResourceGroup -n myWebApp --port 9000
```

## Expected Output

The command outputs connection details in JSON format, including the forwarded port and status. Successful execution shows:

```json
{
  "port": 8000,
  "url": "https://mywebapp.scm.azurewebsites.net:2222",
  "status": "Connected"
}
```

It then enters a persistent mode, keeping the tunnel open until interrupted (Ctrl+C). Errors include authentication failures or insufficient permissions, e.g., "AuthorizationFailed" if RBAC is lacking.

## Related

- [[Related Procedure: azure-web-apps-remote-ssh-connection]]
- [[Related Tool: azure-cli]]
