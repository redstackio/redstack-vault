---
data: cat /h/etc/docker/server-key.pem
tags:
  - file-read
type: command
executor: bash
platforms:
  - Linux
id: a98d64e0-6fc0-4bff-b4fb-318338ff2c79
created_at: '2025-12-14T04:08:48.043Z'
updated_at: '2025-12-14T04:08:48.043Z'
verified: false
validated: true
submitted: true
---
# Cat Docker Server Key Pem

## Command

```bash
cat /h/etc/docker/server-key.pem
```

## Description

Displays Docker TLS private key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /h/etc/docker/server-key.pem | Key file path | Yes |

## Examples

### Basic Usage

```bash
cat /h/etc/docker/server-key.pem
```

## Expected Output

PEM key content.

## Related

- [[commands/cat-docker-server-pem]]
