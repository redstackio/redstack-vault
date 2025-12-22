---
type: command
executor: bash
data: az account get-access-token --resource-type $_RESOURCE_TYPE
output: null
created_at: '2023-05-24T07:13:54Z'
updated_at: '2023-05-24T07:13:54Z'
platforms:
  - Cloud
tags:
  - azure-cli
  - token-retrieval
verified: true
validated: true
---

# az-account-get-access-token

## Command

```bash
az account get-access-token --resource-type $_RESOURCE_TYPE
```

## Description

Retrieves an access token from the currently logged-in Azure account, optionally for a specific resource type. When executed in a managed identity context, it uses the identity's credentials. Use this in Azure resources to obtain tokens without explicit login.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--resource-type` | Specifies the resource type (e.g., 'aad-graph' for Microsoft Graph, defaults to Azure Resource Manager if omitted) | No |
| $_RESOURCE_TYPE | Placeholder for the resource type value | No |

## Examples

### Basic Usage

```bash
az account get-access-token
```

### Advanced Usage

```bash
az account get-access-token --resource-type aad-graph
```

## Expected Output

```json
{
  "accessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...");
  "expiresOn": "2023-05-24T15:00:00Z",
  "subscription": "...",
  "tenant": "...",
  "tokenType": "Bearer",
  "user": {
    "name": "...",
    "type": "servicePrincipal"
  }
}
```

A JSON object with the access token and metadata. Success: Valid JWT in accessToken field; failure: Error like "authentication required."

## Related

- [[procedures/Retrieve-Access-Tokens-from-Azure-Managed-Identity]]
- [[commands/get-az-access-token]]
