---
id: 1ee14c23-ae91-4a0a-864f-051c7fec39d6
name: aws-ec2-describe-volumes
type: command
executor: bash
data: aws ec2 describe-volumes
output: null
created_at: '2023-04-06T03:56:13.701189+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - enumeration
  - discovery
verified: true
validated: true
---

# aws-ec2-describe-volumes

## Command

```bash
aws ec2 describe-volumes
```

## Description

This command queries the AWS EC2 API to retrieve detailed information about all Elastic Block Store (EBS) volumes in the specified region. It is used for discovering storage resources, including volume IDs, sizes, states, and attachments, which aids in identifying potential targets for data access or manipulation in cloud environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region to query (e.g., us-east-1); defaults to configured region | No |
| `--filters` | Key-value filters for volumes (e.g., Name=volume-id,Values=vol-12345) | No |
| `--output` | Format of output (json, text, table); defaults to json | No |
| `--query` | JMESPath query to filter output (e.g., Volumes[].VolumeId) | No |

## Examples

### Basic Usage

```bash
aws ec2 describe-volumes
```

Retrieves all volumes in the default region.

### Advanced Usage

```bash
aws ec2 describe-volumes --region us-west-2 --filters "Name=state,Values=available" --output table
```

Lists only available volumes in us-west-2 in table format.

## Expected Output

Successful execution returns JSON with a 'Volumes' array, each containing fields like:

```json
{
  "Volumes": [
    {
      "AvailabilityZone": "us-east-1a",
      "VolumeId": "vol-049df61146c4d7901",
      "State": "in-use",
      "Size": 8,
      "Attachments": [
        {
          "AttachTime": "2023-01-01T00:00:00.000Z",
          "InstanceId": "i-1234567890abcdef0",
          "VolumeId": "vol-049df61146c4d7901"
        }
      ]
    }
  ]
}
```

Errors (e.g., AccessDenied) indicate permission issues.

## Related

- [[procedures/Enumerate-EBS-Volumes-via-AWS-CLI]]
- [[tools/aws-cli]]
