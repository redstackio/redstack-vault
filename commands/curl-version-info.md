---
data: curl -V
tags:
  - version
  - curl
type: command
executor: bash
platforms:
  - Linux
  - POSIX
id: 493fa220-5aac-4e3a-afaa-3b564b5c2ef5
created_at: '2025-12-14T17:23:31.200Z'
updated_at: '2025-12-14T17:23:31.200Z'
verified: false
validated: true
submitted: true
---
# curl-version-info

## Command

```bash
curl -V
```

## Description

Displays detailed version information for curl, including libcurl version, supported protocols, and features, used to confirm vulnerability in --engine option.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-V` | Verbose version output with libcurl details, protocols, and features | Yes |

## Examples

### Basic Usage

```bash
curl -V
```

### Advanced Usage

Not applicable; single flag.

## Expected Output

curl 8.13.0 (x86_64-pc-linux-gnu) libcurl/8.13.0 OpenSSL/3.5.0 ... (full version string with protocols and features)

## Related

- [[Related Procedure]]
