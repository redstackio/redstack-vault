---
id: 7997ce25-169b-431d-a1fb-288bb903f5f3
name: aws-ec2-remove-launch-permission-from-ami
type: command
executor: bash
data: >
  aws ec2 modify-image-attribute --image-id $AMI_ID --launch-permission
  "Remove=[{UserId=$TARGET_ACCOUNT_ID}]"
output: null
created_at: '2020-07-31T04:25:35.109762+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Cloud
tags:
  - AWS
  - EC2
verified: true
validated: true
---

# aws-ec2-remove-launch-permission-from-ami

## Command

```bash
aws ec2 modify-image-attribute --image-id $AMI_ID --launch-permission "Remove=[{UserId=$TARGET_ACCOUNT_ID}]"
```

## Description

This command removes launch permissions from an AWS AMI for a specified account, revoking their ability to launch instances from it. Use this for cleanup after sharing an AMI to minimize exposure and detection risks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --image-id $AMI_ID | The ID of the AMI to modify (e.g., ami-0abcdef1234567890) | Yes |
| --launch-permission "Remove=[{UserId=$TARGET_ACCOUNT_ID}]" | JSON structure removing permission for the target account ID (12-digit number) | Yes |

## Examples

### Basic Usage

```bash
aws ec2 modify-image-attribute --image-id ami-0abcdef1234567890 --launch-permission "Remove=[{UserId=123456789012}]"
```

### Advanced Usage

If permissions were added for multiple accounts, run this command once per account to revoke individually.

## Expected Output

On success, the command returns an empty response body with exit code 0. Verify removal using `aws ec2 describe-image-attribute --image-id $AMI_ID --attribute launchPermission` to confirm the account is no longer listed.

## Related

- [[commands/aws-ec2-add-launch-permission-to-ami]]
- [[procedures/Share-AWS-AMI-Image-with-Another-Account]]
