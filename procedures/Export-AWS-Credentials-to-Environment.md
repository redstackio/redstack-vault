---
id: 2bf21879-c244-4f30-bcac-ae4843631164
name: export-aws-credentials-to-environment
type: command
executor: bash
data: |-
  export AWS_ACCESS_KEY_ID=$($_ACCESS_KEY_ID)
  export AWS_SECRET_ACCESS_KEY=$($_SECRET_ACCESS_KEY)
  export AWS_SESSION_TOKEN=$($_SESSION_TOKEN)
output: null
created_at: '2023-04-06T03:56:10.928456+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - aws
  - credentials
  - cloud
verified: true
validated: true
---

# export-aws-credentials-to-environment

## Command

```bash
export AWS_ACCESS_KEY_ID=$($_ACCESS_KEY_ID)
export AWS_SECRET_ACCESS_KEY=$($_SECRET_ACCESS_KEY)
export AWS_SESSION_TOKEN=$($_SESSION_TOKEN)
```

## Description

This command exports AWS authentication credentials as environment variables in the current bash shell session, enabling AWS CLI and SDK tools to authenticate requests without configuration files. Use it after obtaining credentials to quickly set up access for AWS operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ACCESS_KEY_ID | The AWS access key ID (e.g., AKIAIOSFODNN7EXAMPLE) | Yes |
| $_SECRET_ACCESS_KEY | The AWS secret access key (e.g., wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY) | Yes |
| $_SESSION_TOKEN | The temporary session token for assumed roles or STS credentials (optional for long-term keys) | No |

## Examples

### Basic Usage

```bash
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

### Advanced Usage (with Session Token)

```bash
export AWS_ACCESS_KEY_ID=ASIA...\nexport AWS_SECRET_ACCESS_KEY=...\nexport AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjE...\n```

## Expected Output

No direct output from the export commands themselves, as they silently set environment variables. Verify success by checking variables with `echo $AWS_ACCESS_KEY_ID` (should print the key) or testing with `aws sts get-caller-identity` (should return account details without authentication errors).

## Related

- [[procedures/Export-AWS-Credentials-to-Environment]] (procedure that uses this command)
- [[tools/AWS-CLI]] (tool for subsequent AWS operations)
