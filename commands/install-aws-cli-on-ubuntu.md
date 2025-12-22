---
id: 6598bea2-6221-4656-bb94-06a0c2b6f0da
name: install-aws-cli-on-ubuntu
type: command
executor: bash
data: sudo apt update && sudo apt install awscli -y
output: null
created_at: '2023-04-06T03:55:53.510711+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - installation
  - aws
verified: true
validated: true
---

# install-aws-cli-on-ubuntu

## Command

```bash
sudo apt update && sudo apt install awscli -y
```

## Description

This command updates the package index and installs the AWS CLI on Ubuntu or Debian-based systems, enabling command-line access to AWS services like S3 for security testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sudo` | Elevates privileges for installation | Yes |
| `apt update` | Refreshes package lists | Yes (built-in) |
| `apt install awscli -y` | Installs AWS CLI without prompting for confirmation | Yes |

## Examples

### Basic Usage

```bash
sudo apt update && sudo apt install awscli -y
```

### Verification

```bash
aws --version
```

## Expected Output

Installation progress messages, ending with "awscli is already the newest version" or similar if successful. No errors on package fetch.

## Related

- [[procedures/Configure-AWS-CLI-for-S3-Access]]
- [[tools/AWS-CLI]]
