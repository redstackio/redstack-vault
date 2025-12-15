---
id: cmd-018
data: ./src/curl --version
tags:
  - verify
  - version
type: command
output: 'curl 8.16.1-DEV ... Protocols: ...'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:27.998Z'
verified: false
validated: true
submitted: true
---
# curl-version-check

## Command

```bash
./src/curl --version
```

## Description

Displays cURL version and supported features.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--version` | Version info | Yes |

## Examples

### Basic Usage

```bash
./src/curl --version
```

## Expected Output

curl 8.16.1-DEV with protocols.

## Related

- [[procedures/Building-cURL-with-Security-Debugging-Flags]]
