---
id: f30d0188-ff3f-4743-9599-c64a262b358b
name: attach-ebs-volume-to-ec2-instance
type: command
executor: bash
data: >-
  aws ec2 attach-volume --volume-id $_VOLUME_ID --instance-id $_INSTANCE_ID
  --device $_DEVICE_NAME
output: null
created_at: '2023-04-06T03:56:13.827098+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - aws
  - ebs
  - ec2
  - cloud
verified: true
validated: true
---

# attach-ebs-volume-to-ec2-instance

## Command

```bash
aws ec2 attach-volume --volume-id $_VOLUME_ID --instance-id $_INSTANCE_ID --device $_DEVICE_NAME
```

## Description

This command attaches an existing EBS volume to a running EC2 instance as a specified block device, enabling the instance to access the volume's data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --volume-id $_VOLUME_ID | ID of the EBS volume (e.g., vol-0123456789abcdef0) | Yes |
| --instance-id $_INSTANCE_ID | ID of the EC2 instance (e.g., i-0123456789abcdef0) | Yes |
| --device $_DEVICE_NAME | Device name on the instance (e.g., /dev/sdf; becomes /dev/xvdf) | Yes |

## Examples

### Basic Usage

```bash
aws ec2 attach-volume --volume-id vol-0123456789abcdef0 --instance-id i-0123456789abcdef0 --device /dev/sdf
```

### Advanced Usage

```bash
aws ec2 attach-volume --volume-id vol-0123456789abcdef0 --instance-id i-0123456789abcdef0 --device /dev/sdg
```

## Expected Output

{
    "AttachTime": "2023-10-01T12:00:00+00:00",
    "Device": "/dev/sdf",
    "InstanceId": "i-0123456789abcdef0",
    "State": "attaching",
    "VolumeId": "vol-0123456789abcdef0"
}

## Related

- [[procedures/Mount-EBS-Volume-to-EC2-Linux-Instance]]
- [[commands/create-ebs-volume-from-snapshot]]
