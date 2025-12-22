---
id: 0214800a-e85d-4516-a6dd-338ebd0d9461
name: aws-ec2-describe-image-by-id
type: command
executor: bash
data: >
  aws ec2 describe-images --image-ids $_AMI_ID --profile $_PROFILE --region
  $_REGION
output: >-
  aws ec2 describe-images --image-ids ami-a123ee1f --profile staging --region
  us-east-1
created_at: '2020-07-31T04:25:19.326889+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - aws
  - ec2
  - discovery
verified: true
validated: true
---

# aws-ec2-describe-image-by-id

## Command

```bash
aws ec2 describe-images --image-ids $_AMI_ID --profile $_PROFILE --region $_REGION
```

## Description

This command retrieves detailed information about a specific AMI using its ImageId. It is useful for inspecting individual image configurations after initial enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --image-ids $_AMI_ID | The ID of the AMI to describe (e.g., ami-0abcdef1234567890). Multiple IDs can be comma-separated. | Yes |
| --profile $_PROFILE | AWS CLI profile name for authentication (e.g., staging). Defaults to 'default'. | No |
| --region $_REGION | AWS region to query (e.g., us-east-1). Defaults to profile's default. | No |

## Examples

### Basic Usage

```bash
aws ec2 describe-images --image-ids ami-0abcdef1234567890
```

### With Profile and Region

```bash
aws ec2 describe-images --image-ids ami-a123ee1f --profile staging --region us-east-1
```

## Expected Output

JSON object with an Images array containing details for the specified AMI, including BlockDeviceMappings, ProductCodes, RootDeviceType, and VirtualizationType.

Example:
```
{
    "Images": [
        {
            "ImageId": "ami-a123ee1f",
            "RootDeviceType": "ebs",
            "BlockDeviceMappings": [
                {
                    "DeviceName": "/dev/xvda",
                    "Ebs": {
                        "DeleteOnTermination": true,
                        "VolumeSize": 8
                    }
                }
            ]
        }
    ]
}
```

## Related

- [[procedures/Enumerate-AWS-EC2-AMIs]]
- [[commands/aws-ec2-describe-all-images]]
