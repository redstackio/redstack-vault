---
id: 0d006c55-e7fa-40e0-a90e-d21b68c14d00-rewritten
name: view-bloodhound-customqueries-linux
type: command
executor: bash
data: cat ~/.config/bloodhound/customqueries.json
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - recon
  - active-directory
verified: true
validated: true
---

# view-bloodhound-customqueries-linux

## Command

```bash
cat ~/.config/bloodhound/customqueries.json
```

## Description

This command displays the contents of BloodHound's customqueries.json file on Linux systems, allowing inspection of defined Cypher queries for AD reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses default home directory path | No |

## Examples

### Basic Usage

```bash
cat ~/.config/bloodhound/customqueries.json
```

### With Error Handling

```bash
cat ~/.config/bloodhound/customqueries.json || echo "File not found"
```

## Expected Output

A JSON array of query objects, e.g.:

```json
[
  {
    "name": "Example",
    "query": "MATCH (n) RETURN n"
  }
]
```

If the file doesn't exist, it outputs an error like "No such file or directory".

## Related

- [[procedures/Active-Directory-Recon-Using-BloodHound-Custom-Queries]]
- [[tools/BloodHound]]
