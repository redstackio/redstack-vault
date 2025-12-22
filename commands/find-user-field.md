---
id: 3bb68f75-9106-4210-990c-f1e6cc77dea0
type: command
executor: powershell
data: Find-UserField -SearchField $_SEARCH_FIELD -SearchTerm $_SEARCH_TERM
output: null
created_at: '2023-04-06T03:56:02.229229+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Find User Field

## Command

```powershell
Find-UserField -SearchField $_SEARCH_FIELD -SearchTerm $_SEARCH_TERM
```

## Description

Searches user attributes for specific terms, e.g., keywords in descriptions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -SearchField | Field to search (e.g., Description) | Yes |
| -SearchTerm | Term to find (e.g., 'admin') | Yes |

## Examples

### Basic Usage

```powershell
Find-UserField -SearchField Description -SearchTerm 'wtver'
```

## Expected Output

Matching user objects.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
