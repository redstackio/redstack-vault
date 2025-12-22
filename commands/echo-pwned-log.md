---
id: cmd-008
data: echo pwned >> /opt/out/snapshot/log/build.log
tags:
  - logging
type: command
output: '''pwned'' added to log'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.201Z'
verified: false
validated: true
submitted: true
---
# echo-pwned-log

## Command

```bash
echo pwned >> /opt/out/snapshot/log/build.log
```

## Description

Appends a success marker to the build log after prepare.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pwned | String to append | Yes |
| /opt/out/snapshot/log/build.log | Log file | Yes |

## Examples

### Basic Usage

```bash
echo pwned >> /opt/out/snapshot/log/build.log
```

## Expected Output

'pwned' appended.

## Related

- [[commands/apt-install-malicious-deb]]
