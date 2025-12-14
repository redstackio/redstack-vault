---
data: cat /h/etc/docker/server.pem
tags:
  - file-read
type: command
executor: bash
platforms:
  - Linux
id: 54fd1064-0ea1-4159-ad26-e1acf39ba86a
created_at: '2025-12-14T04:08:48.048Z'
updated_at: '2025-12-14T04:08:48.048Z'
verified: false
validated: true
submitted: true
---
# Cat Docker Server Pem

## Command

```bash
cat /h/etc/docker/server.pem
```

## Description

Displays Docker TLS server certificate.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /h/etc/docker/server.pem | Cert file path | Yes |

## Examples

### Basic Usage

```bash
cat /h/etc/docker/server.pem
```

## Expected Output

PEM certificate content.

## Related

- [[commands/cat-docker-server-key-pem]]
