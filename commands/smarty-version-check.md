---
data: '{$smarty.version}'
tags:
  - ssti
  - version-check
type: command
executor: bash
platforms:
  - Web
id: 228f36c1-5725-44b2-8d0f-364d1e4eea39
created_at: '2025-12-13T09:01:17.028Z'
updated_at: '2025-12-13T09:01:17.028Z'
verified: false
validated: true
submitted: true
---
# Smarty Version Check

## Command

```bash
{$smarty.version}
```

## Description

Retrieves the version of the Smarty templating engine when injected into templates.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Version variable | Yes |

## Examples

### Basic Usage

```bash
{$smarty.version}
```

## Expected Output

Smarty version string.

## Related

- [[procedures/Confirm-Smarty-Version]]
