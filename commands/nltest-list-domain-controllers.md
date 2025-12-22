---
type: command
executor: cmd
data: 'nltest /dclist:domain.com'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - reconnaissance
  - active-directory
verified: true
validated: true
---

# nltest-list-domain-controllers

## Command

```cmd
nltest /dclist:domain.com
```

## Description

Lists all domain controllers in the specified AD domain using the nltest diagnostic tool.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /dclist:domain.com | Domain controller list flag with target domain | Yes |

## Examples

### Basic Usage

```cmd
nltest /dclist:contoso.com
```

## Expected Output

DC Site Results:

    DC01                    CONTOSO-DC-SITE
    DC02                    CONTOSO-DC-SITE

The command completed successfully

## Related

- [[procedures/Active-Directory-Domain-Controller-Lookup]]
