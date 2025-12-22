---
id: c7d58cdc-384e-4f4d-a81b-40407104e70e
name: aws-glue-upload-ssh-public-key
type: command
executor: bash
data: >-
  aws glue update-dev-endpoint --endpoint-name $_ENDPOINT_NAME --public-key
  file://$_KEY_FILE
output: null
created_at: '2023-04-06T03:56:09.319146+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - glue
  - ssh
verified: true
validated: true
---

# aws-glue-upload-ssh-public-key

## Command

```bash
aws glue update-dev-endpoint --endpoint-name $_ENDPOINT_NAME --public-key file://$_KEY_FILE
```

## Description

Uploads an SSH public key to a Glue development endpoint for remote access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --endpoint-name $_ENDPOINT_NAME | Name of Glue endpoint | Yes |
| --public-key file://$_KEY_FILE | Path to public key file | Yes |

## Examples

### Basic Usage

```bash
aws glue update-dev-endpoint --endpoint-name target_endpoint --public-key file://key.pub
```

## Expected Output

Updated endpoint details.

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
