---
data: >-
  az webapp create --resource-group myGroup --plan myPlan --name
  s00397nasv101-datacafe-cert --runtime "DOTNET|6.0"
tags:
  - azure
  - webapp
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:01.964Z'
id: d1db71ea-cf59-4595-811f-cb02addd8cb5
verified: false
validated: true
submitted: true
---
# az-webapp-create

## Command

```bash
az webapp create --resource-group myGroup --plan myPlan --name s00397nasv101-datacafe-cert --runtime "DOTNET|6.0"
```

## Description

Creates a new Azure Web App, claiming an unclaimed name for takeover purposes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--resource-group` | RG name | Yes |
| `--plan` | App service plan | Yes |
| `--name` | Unique app name | Yes |
| `--runtime` | Runtime stack | Yes |

## Examples

### Basic Usage

```bash
az webapp create --resource-group rg --plan plan --name myapp --runtime "NODE|18"
```

### Advanced Usage

```bash
az webapp create --resource-group rg --plan plan --name dangling-app --runtime "DOTNET|6.0" --deployment-local-git
```

## Expected Output

Details of created app, including default host name.

## Related

- [[commands/az-login]]
