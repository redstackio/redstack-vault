---
id: 25f9af39-ec4d-4267-abba-463e2222fa86
name: aws-ec2-delete-volume
type: command
executor: bash
data: |
  aws ec2 delete-volume --region $_AWS_REGION --volume-id $_AWS_VOLUME_ID
output: null
created_at: '2020-07-31T04:25:34.139559+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - AWS
  - EC2
verified: true
validated: true
---

# aws-ec2-delete-volume

## Command

```bash
aws ec2 delete-volume --region $_AWS_REGION --volume-id $_AWS_VOLUME_ID
```

## Description

This command deletes a specified EBS volume in AWS EC2. Use it for cleanup after testing or to remove unused storage. The volume must be detached and available; in-use volumes will fail deletion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --region $_AWS_REGION | AWS region where the volume exists (e.g., us-east-1) | Yes |
| --volume-id $_AWS_VOLUME_ID | The ID of the EBS volume to delete (e.g., vol-049df61146c4d7901) | Yes |

## Examples

### Basic Usage

```bash
aws ec2 delete-volume --region us-east-1 --volume-id vol-049df61146c4d7901
```

### Advanced Usage

```bash
aws ec2 delete-volume --region us-east-1 --volume-id vol-049df61146c4d7901 --profile my-aws-profile
```

## Expected Output

Successful deletion returns:

```json
{
    "FailedItems": []
}
```

If the volume is in-use:

```json
{
    "FailedItems": [
        {
            "VolumeId": "vol-049df61146c4d7901",
            "Message": "The volume 'vol-049df61146c4d7901' is currently attached to an instance."
        }
    ]
}
```

## Related

- [[procedures/aws-delete-ebs-volumes]]
- [[tools/aws-cli]]
