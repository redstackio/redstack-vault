---
data: >-
  az network traffic-manager profile list --query
  "[?dnsConfig.uniqueDnsName=='$1']" --output table
tags:
  - azure
  - cloud
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.811Z'
id: 2e78a186-26aa-4e4f-a886-c2e74d5f51c0
verified: false
validated: true
submitted: true
---
# az-traffic-manager-list

## Command

```bash
az network traffic-manager profile list --query "[?dnsConfig.uniqueDnsName=='$1']" --output table
```

## Description

This Azure CLI command lists Traffic Manager profiles filtered by unique DNS name to check if a specific profile exists, useful for verifying unclaimed resources in subdomain takeover scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --query | JMESPath query for filtering by dnsConfig.uniqueDnsName | Yes |
| $1 | The unique DNS name (e.g., mydailydev.trafficmanager.net) | Yes |
| --output table | Formats output as table | No |

## Examples

### Basic Usage

```bash
az network traffic-manager profile list --query "[?dnsConfig.uniqueDnsName=='mydailydev.trafficmanager.net']" --output table
```

### Advanced Usage

```bash
az network traffic-manager profile list --resource-group myRG --query "[?name=='mydailydev']"
```

## Expected Output

Empty table or no results if unclaimed, e.g., "No resources found."

## Related

- [[Related Procedure: Verify-Unclaimed-Azure-Traffic-Manager-Profile]]
