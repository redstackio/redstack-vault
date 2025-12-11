---
data: >-
  jfrog rt config --url=https://snapchat.jfrog.io/artifactory --user=username
  --password=password

  jfrog rt ping
tags:
  - artifactory
  - login
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 52454a4c-a45a-4e76-b7d9-bf75e019c60b
created_at: '2025-12-11T03:47:56.520Z'
updated_at: '2025-12-11T03:47:56.520Z'
verified: false
validated: true
submitted: true
---
# jfrog-cli-login

## Command

```bash
jfrog rt config --url=https://snapchat.jfrog.io/artifactory --user=username --password=password
jfrog rt ping
```

## Description

Configures JFrog CLI with credentials and pings the Artifactory server to validate access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url=https://...` | Artifactory URL | Yes |
| `--user=username` | Username | Yes |
| `--password=password` | Password | Yes |

## Examples

### Basic Usage

```bash
jfrog rt config --url=https://snapchat.jfrog.io/artifactory --user=username --password=password
jfrog rt ping
```

### Advanced Usage

```bash
jfrog rt config --interactive
```

## Expected Output

'OK' from ping if configuration is successful.

## Related

- [[commands/jfrog-cli-push-artifact]]
- [[procedures/Access-and-Manipulate-JFrog-Artifactory-Instance]]
