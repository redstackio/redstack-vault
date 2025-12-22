---
id: 3c80fa7f-0316-4f14-98b8-21cea6babbf4
name: aws-ec2-add-launch-permission-to-ami
type: command
executor: bash
data: >
  aws ec2 modify-image-attribute --image-id $AMI_ID --launch-permission
  "Add=[{UserId=$TARGET_ACCOUNT_ID}]"
output: null
created_at: '2020-07-31T04:25:35.109593+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Cloud
tags:
  - AWS
  - EC2
verified: true
validated: true
---

# aws-ec2-add-launch-permission-to-ami

## Command

```bash
aws ec2 modify-image-attribute --image-id $AMI_ID --launch-permission "Add=[{UserId=$TARGET_ACCOUNT_ID}]"
```

## Description

This command adds launch permissions to an AWS AMI, allowing a specified AWS account to launch instances from it. Use this to share AMIs across accounts in scenarios requiring stealthy deployment, such as evading instance-launch monitoring.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --image-id $AMI_ID | The ID of the AMI to modify (e.g., ami-0abcdef1234567890) | Yes |
| --launch-permission "Add=[{UserId=$TARGET_ACCOUNT_ID}]" | JSON structure adding permission for the target account ID (12-digit number) | Yes |

## Examples

### Basic Usage

```bash
aws ec2 modify-image-attribute --image-id ami-0abcdef1234567890 --launch-permission "Add=[{UserId=123456789012}]"
```

### Advanced Usage

For multiple accounts, chain adds in separate commands or use AWS console for bulk, but CLI supports single additions per invocation.

## Expected Output

On success, the command returns an empty response body with exit code 0, indicating the attribute was modified. No detailed output is provided; verify with `aws ec2 describe-image-attribute`.

## Related

- [[commands/aws-ec2-remove-launch-permission-from-ami]]
- [[procedures/Share-AWS-AMI-Image-with-Another-Account]]
