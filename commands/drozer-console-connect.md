---
data: drozer console connect
tags:
  - drozer
  - connection
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.866Z'
id: 604a2657-6b93-438b-a5e5-d6c04d47147d
verified: false
validated: true
submitted: true
---
# drozer-console-connect

## Command

```bash
drozer console connect
```

## Description

This command connects the Drozer console on the host to the Drozer agent running on an Android device, enabling interactive security assessment sessions after the embedded server is started.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Connects to the default agent (assumes server running on device) | Yes |

## Examples

### Basic Usage

```bash
drozer console connect
```

### Advanced Usage

For remote devices, specify host: `drozer console connect --server <device_ip>:31415`

## Expected Output

'Drozer Console connected to <device>' or similar confirmation, followed by the Drozer prompt (dz>).

## Related

- [[Related Procedure: Connect-to-Drozer-Console]]
