---
id: 35b790eb-00a1-4dac-afe8-8eee2cdf7542
type: command
executor: bash
data: python ssbackend.pyz
output: null
created_at: '2023-04-06T03:56:14.585156+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - stormspotter
  - backend
verified: true
validated: true
---

# stormspotter-start-backend

## Command

```bash
python ssbackend.pyz
```

## Description

Starts the Neo4j backend server for StormSpotter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs on default port 7687 | No |

## Examples

### Basic Usage

```bash
python ssbackend.pyz
```

## Expected Output

Server listening on bolt://localhost:7687.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/Azure-StormSpotter]]
