---
id: efd4a182-fcc6-4eaf-a04d-6d8b8bd452b0
name: check-aws-credentials-file-existence
type: command
executor: bash
data: ls ~/.aws/credentials
output: null
created_at: '2023-04-06T03:56:09.911280+00:00'
updated_at: '2023-04-10T20:19:56.523437+00:00'
platforms:
  - Linux
  - macOS
tags:
  - aws-cli
  - verification
verified: true
validated: true
---

# check-aws-credentials-file-existence

## Command

```bash
ls ~/.aws/credentials
```

## Description

This command checks if the AWS credentials file exists in the default location (~/.aws/credentials), which stores access keys after configuration. It is a quick verification step post-setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ~/.aws/credentials | Path to the credentials file | Yes (fixed) |

## Examples

### Basic Usage

```bash
ls ~/.aws/credentials
```

If the file exists, it lists the file name.

### Advanced Usage

Combine with error handling: `ls ~/.aws/credentials || echo 'File missing'`. On Windows, use `dir %USERPROFILE%\.aws\credentials`.

## Expected Output

credentials (if file exists) or `ls: cannot access '~/.aws/credentials': No such file or directory` (if missing).

## Related

- [[procedures/AWS-CLI-Configuration]]
- [[commands/aws-configure-default-profile]]
