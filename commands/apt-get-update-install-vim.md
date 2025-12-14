---
data: apt-get update && apt-get install -y vim
tags:
  - docker
  - install
type: command
output: Package installation output
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:16.314Z'
id: fdceba5e-821e-4a40-a8ad-8e40f5ff21f4
verified: false
validated: true
submitted: true
---
# apt-get-update-install-vim

## Command

```bash
apt-get update && apt-get install -y vim
```

## Description

Updates package list and installs vim in a Debian-based Docker image for editing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -y | Automatic yes | Yes |

## Examples

### Basic Usage

```bash
apt-get update && apt-get install -y vim
```

## Expected Output

Package installation output with no errors.

## Related

- [[commands/gem-install-rails-new-app]]
