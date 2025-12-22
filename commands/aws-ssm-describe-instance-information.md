---
id: 2618a402-6f00-4e8e-949b-8c9bd2dda472
name: aws-ssm-describe-instance-information
type: command
executor: bash
data: aws ssm describe-instance-information --profile $_PROFILE --region $_REGION
output: null
created_at: '2023-04-06T03:56:09.691366Z'
updated_at: '2023-04-10T20:20:49.939502Z'
platforms:
  - AWS
tags:
  - aws
  - ssm
  - recon
verified: true
validated: true
---

# aws-ssm-describe-instance-information

## Command

```bash
aws ssm describe-instance-information --profile $_PROFILE --region $_REGION
```

## Description

This command queries AWS Systems Manager to list all EC2 instances registered for management, including their IDs, ping status, and platform details. Use it to identify accessible targets for remote execution in cloud environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --profile $_PROFILE | AWS CLI profile with SSM permissions (e.g., stolencreds) | Yes |
| --region $_REGION | AWS region where instances are located (e.g., eu-west-1) | Yes |
| --query | JMESPath query to filter output (e.g., InstanceInformationList[*].InstanceId) | No |

## Examples

### Basic Usage

```bash
aws ssm describe-instance-information --profile stolencreds --region eu-west-1
```

### Filtered Usage

```bash
aws ssm describe-instance-information --profile stolencreds --region us-east-1 --query 'InstanceInformationList[?PingStatus==`Online`].{ID:InstanceId,Platform:PlatformType}'
```

## Expected Output

```
{
    "InstanceInformationList": [
        {
            "InstanceId": "i-1234567890abcdef0",
            "PingStatus": "Online",
            "LastPingDateTime": "2023-04-10T20:00:00Z",
            "PlatformType": "Linux",
            "PlatformName": "Ubuntu",
            "PlatformVersion": "20.04",
            "IPAddress": "10.0.1.100",
            "IsLatestVersion": true
        }
    ]
}
```

A successful run lists instances with Online ping status, indicating they are ready for commands.

## Related

- [[commands/aws-ssm-send-shell-script-command]]
- [[procedures/aws-ssm-command-execution-ec2-shell-script]]
