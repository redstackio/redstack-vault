---
id: 1dcccc4e-fed1-43a6-b52d-2cbf465547e7
name: bash-display-environment-variables
type: command
executor: bash
data: env
output: null
created_at: '2023-05-24T16:00:22.701740+00:00'
updated_at: '2023-05-24T16:00:22.979060+00:00'
platforms:
  - Linux
tags:
  - environment-variables
  - discovery
verified: true
validated: true
---

# bash-display-environment-variables

## Command

```bash
env
```

## Description

This command displays all environment variables in the current shell session, useful for discovering sensitive values like Azure Managed Identity tokens in a compromised Linux host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; lists all variables | No |

## Examples

### Basic Usage

```bash
env
```

### Advanced Usage

```bash
env | grep IDENTITY
```

## Expected Output

A list of environment variables in KEY=VALUE format, such as:

```
PATH=/usr/local/bin:/usr/bin
IDENTITY_ENDPOINT=http://169.254.169.254/metadata/identity/oauth2/token
IDENTITY_HEADER=secret_value_here
HOME=/home/user
```

## Related

- [[procedures/Azure-Managed-Identity-Token-Theft-via-Environment-Variables]]
