---
id: 4c21033a-0b09-40f9-94a1-47866fb31e98
name: check-user-rights-for-automation
type: command
executor: bash
data: az extension add --upgrade -n automation
output: null
created_at: '2023-05-24T22:50:53.196372+00:00'
updated_at: '2023-05-24T22:50:54.391095+00:00'
platforms:
  - Cloud
tags:
  - azure
  - discovery
verified: true
validated: true
---

# check-user-rights-for-automation

## Command

```bash
az extension add --upgrade -n automation
```

## Description

This Azure CLI command installs or upgrades the 'automation' extension, enabling subsequent commands to query Automation Account access. Run it first to prepare the environment for privilege checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --upgrade | Upgrades the extension if already installed | No |
| -n automation | Specifies the extension name | Yes |

## Examples

### Basic Usage

```bash
az extension add --upgrade -n automation
```

### Advanced Usage

Run before listing accounts: az extension add --upgrade -n automation && az automation account list

## Expected Output

JSON response indicating the extension was added or upgraded, e.g., {"name": "automation", "version": "0.1.0"}. No errors indicate readiness.

## Related

- [[procedures/Create-and-Execute-Malicious-Azure-Runbook]]
- [[commands/list-automation-accounts]]
