---
id: 3012a915-0859-4be5-8ff7-931a8d4f7cb5
name: set-aws-environment-variables
type: command
executor: bash
data: >-
  export AWS_ACCESS_KEY_ID="$_ACCESS_KEY_ID" && export
  AWS_SECRET_ACCESS_KEY="$_SECRET_ACCESS_KEY" && export
  AWS_SESSION_TOKEN="$_SESSION_TOKEN"
output: null
created_at: '2023-04-06T03:55:53.511084+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - environment
  - aws
  - temporary-credentials
verified: true
validated: true
---

# set-aws-environment-variables

## Command

```bash
export AWS_ACCESS_KEY_ID="$_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="$_SECRET_ACCESS_KEY"
export AWS_SESSION_TOKEN="$_SESSION_TOKEN"
```

## Description

This command exports AWS credentials as environment variables for temporary or session-based authentication, overriding profile settings in the current shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `AWS_ACCESS_KEY_ID` | The access key value | Yes (for long-term) |
| `AWS_SECRET_ACCESS_KEY` | The secret key value | Yes (for long-term) |
| `AWS_SESSION_TOKEN` | Temporary token for assumed roles | Yes (for temp creds), No otherwise |

## Examples

### Basic Usage

```bash
export AWS_ACCESS_KEY_ID="ASIAZEXAMPLEKEY"
export AWS_SECRET_ACCESS_KEY="fPkEXAMPLESECRET"
export AWS_SESSION_TOKEN="FQoGZXIvYXdzEXAMPLETOKEN"
```

### Verification

```bash
env | grep AWS_
aws sts get-caller-identity
```

## Expected Output

No output from export; verification shows variables set and identity JSON.

## Related

- [[procedures/Configure-AWS-CLI-for-S3-Access]]
- [[tools/AWS-CLI]]
