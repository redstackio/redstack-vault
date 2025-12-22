---
id: 4aacb8cc-5c90-4e68-8926-ce8af86e5504
name: aws-ec2-describe-images-with-filters
type: command
executor: bash
data: >
  aws ec2 describe-images --filters "Name=$_FILTER_NAME1,Values=$_FILTER_VALUE1"
  "Name=$_FILTER_NAME2,Values=$_FILTER_VALUE2"
output: >-
  aws ec2 describe-images --filters "Name=platform,Values=windows"
  "Name=root-device-type,Values=ebs"
created_at: '2020-07-31T04:25:19.327136+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - aws
  - ec2
  - discovery
  - filter
verified: true
validated: true
---

# aws-ec2-describe-images-with-filters

## Command

```bash
aws ec2 describe-images --filters "Name=$_FILTER_NAME1,Values=$_FILTER_VALUE1" "Name=$_FILTER_NAME2,Values=$_FILTER_VALUE2"
```

## Description

This command lists AMIs matching specified filters, such as OS platform or root device type. It narrows down results for targeted discovery in large accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --filters | Key-value filters for AMI attributes (e.g., "Name=platform,Values=windows"). Multiple filters can be AND-ed. Common names: architecture, platform, root-device-type, virtualization-type. | Yes |

## Examples

### Basic Usage for Windows EBS AMIs

```bash
aws ec2 describe-images --filters "Name=platform,Values=windows" "Name=root-device-type,Values=ebs"
```

### Filter by Architecture

```bash
aws ec2 describe-images --filters "Name=architecture,Values=arm64"
```

## Expected Output

JSON with an Images array filtered by the criteria, showing matching AMIs' details.

Example:
```
{
    "Images": [
        {
            "ImageId": "ami-0123456789abcdef0",
            "Platform": "windows",
            "RootDeviceType": "ebs",
            "Architecture": "x86_64"
        }
    ]
}
```

## Related

- [[procedures/Enumerate-AWS-EC2-AMIs]]
- [[commands/aws-ec2-describe-all-images]]
