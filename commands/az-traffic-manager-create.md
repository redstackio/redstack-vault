---
data: >-
  az network traffic-manager profile create --resource-group $1 --name $2
  --routing-method Performance --unique-dns-name $3
tags:
  - azure
  - cloud
  - creation
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.809Z'
id: 745b4963-51b6-49df-9e2e-c97a386d7a4a
verified: false
validated: true
submitted: true
---
# az-traffic-manager-create

## Command

```bash
az network traffic-manager profile create --resource-group $1 --name $2 --routing-method Performance --unique-dns-name $3
```

## Description

This command creates a new Azure Traffic Manager profile, claiming an unclaimed DNS name for subdomain takeover by registering the resource and enabling traffic routing control.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --resource-group | Azure resource group name | Yes |
| $1 | Resource group value | Yes |
| --name | Profile name | Yes |
| $2 | Profile name value | Yes |
| --routing-method | Routing method (e.g., Performance) | Yes |
| --unique-dns-name | Unique DNS name for claiming | Yes |
| $3 | DNS name value | Yes |

## Examples

### Basic Usage

```bash
az network traffic-manager profile create --resource-group myRG --name mydailydev --routing-method Performance --unique-dns-name mydailydev.trafficmanager.net
```

### Advanced Usage

```bash
az network traffic-manager profile create --resource-group myRG --name mydailydev --routing-method Priority --unique-dns-name mydailydev.trafficmanager.net --ttl 30
```

## Expected Output

JSON output with created profile details, including provisioning state "Succeeded."

## Related

- [[Related Procedure: Claim-Azure-Traffic-Manager-Profile-for-Subdomain-Takeover]]
