---
id: 0c4f1589-f1f9-4f96-8b52-840d4d295d9a
type: command
executor: powershell
data: Invoke-ACLScanner -ResolveGUIDs
output: null
created_at: '2023-04-06T03:56:02.230588+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Search for Interesting ACEs

## Command

```powershell
Invoke-ACLScanner -ResolveGUIDs
```

## Description

Scans for interesting (abusable) ACEs in AD.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ResolveGUIDs | Resolves SIDs | No |

## Examples

### Basic Usage

```powershell
Invoke-ACLScanner -ResolveGUIDs
```

## Expected Output

Potentially abusive permissions.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
