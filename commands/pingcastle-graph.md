---
type: command
executor: powershell
data: pingcastle.exe --graph --server $_DOMAIN
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - visualization
  - active-directory
verified: true
validated: true
---

# pingcastle-graph

## Command

```powershell
pingcastle.exe --graph --server $_DOMAIN
```

## Description

Generates a graph of AD objects and relationships for path analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Domain FQDN | Yes |

## Examples

### Basic Usage

```powershell
pingcastle.exe --graph --server example.com
```

## Expected Output

.gpickle file for graph visualization tools.

## Related

- [[tools/PingCastle]]
