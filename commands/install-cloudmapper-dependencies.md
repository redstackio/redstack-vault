---
id: 52c54e08-8a58-4a4f-aea0-61e68d345ae2
type: command
executor: bash
data: >-
  sudo apt-get install autoconf automake libtool python3.7-dev python3-tk jq
  awscli && pipenv install --skip-lock
output: null
created_at: '2023-04-06T03:56:08.940167+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - install
  - cloudmapper
verified: true
validated: true
---

# Install CloudMapper Dependencies

## Command

```bash
sudo apt-get install autoconf automake libtool python3.7-dev python3-tk jq awscli && pipenv install --skip-lock
```

## Description

Installs system packages and Pipenv dependencies for CloudMapper.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Various packages | System deps | Yes |
| --skip-lock | Pipenv option | Yes |

## Examples

### Basic Usage

```bash
sudo apt-get install autoconf automake libtool python3.7-dev python3-tk jq awscli && pipenv install --skip-lock
```

## Expected Output

Installed packages... Pipenv environment created.
