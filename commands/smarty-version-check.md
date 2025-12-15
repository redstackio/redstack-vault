---
id: cmd-uuid-2
data: '{$smarty.version}'
tags:
  - ssti
  - version-leak
type: command
output: Smarty version string
executor: smarty
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.577Z'
verified: false
validated: true
submitted: true
---
# smarty-version-check

## Command

```smarty
{$smarty.version}
```

## Description

Outputs the Smarty engine version via internal variable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Variable | $smarty.version | Yes |

## Examples

### Basic Usage

```smarty
{$smarty.version}
```

## Expected Output

Version like "Smarty-3.1.21" in email.

## Related

- [[procedures/Confirm-Smarty-Templating-Engine-Version]]
