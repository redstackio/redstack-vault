---
type: command
executor: bash
data: >-
  aws ec2 attach-volume --volume-id $_VOLUME_ID --instance-id $_INSTANCE_ID
  --device $_DEVICE_NAME
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - cloud
  - ec2
  - ebs
verified: true
validated: true
---

# aws-ec2-attach-volume

## Command

```bash
aws ec2 attach-volume --volume-id $_VOLUME_ID --instance-id $_INSTANCE_ID --device $_DEVICE_NAME
```

## Description

This command attaches a specified EBS volume to an EC2 instance at a given device name, enabling access to the volume's storage from the instance. Use it in scenarios requiring persistent data access or modification in cloud environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --volume-id $_VOLUME_ID | The ID of the EBS volume (e.g., vol-1234567890abcdef0) | Yes |
| --instance-id $_INSTANCE_ID | The ID of the target EC2 instance (e.g., i-0abcd1234efgh5678); instance must be running | Yes |
| --device $_DEVICE_NAME | Device name on the instance (e.g., /dev/sdf); must be available and follow OS conventions | Yes |

## Examples

### Basic Usage

```bash
aws ec2 attach-volume --volume-id vol-1234567890abcdef0 --instance-id i-0abcd1234efgh5678 --device /dev/sdf
```

### Advanced Usage

Attach with dry-run for testing (add --dry-run flag if supported in context):

```bash
aws ec2 attach-volume --volume-id vol-1234567890abcdef0 --instance-id i-0abcd1234efgh5678 --device /dev/sdf --dry-run
```

## Expected Output

On success, returns JSON with attachment details:

```json
{
    "AttachmentSet": [
        {
            "AttachTime": "2023-10-01T12:00:00.000Z",
            "Device": "/dev/sdf",
            "InstanceId": "i-0abcd1234efgh5678",
            "State": "attaching",
            "VolumeId": "vol-1234567890abcdef0"
        }
    ]
}
```

Query status with `aws ec2 describe-volumes --volume-ids $_VOLUME_ID` to confirm "attached" state.

## Related

- [[procedures/Attach-EBS-Volume-to-EC2-Instance]]
- [[tools/AWS-CLI]]
