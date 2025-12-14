---
data: env
tags:
  - recon
type: command
output: List of environment variables
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.966Z'
id: 9a8d07df-da5e-478e-a7b2-da9d69823414
verified: false
validated: true
submitted: true
---
# env-shell

## Command

```bash
env
```

## Description

Prints all environment variables, revealing paths, credentials, or AWS metadata in RCE scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
env
```

## Expected Output

PATH=/usr/local/bin:... AIRFLOW_HOME=...

## Related

- [[commands/id-shell]]
