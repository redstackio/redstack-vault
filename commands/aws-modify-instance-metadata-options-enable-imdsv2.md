---
id: 92b815ce-1f11-41e2-b9bc-bb2d6a68bf67
name: aws-modify-instance-metadata-options-enable-imdsv2
type: command
executor: bash
data: >-
  aws ec2 modify-instance-metadata-options --instance-id <INSTANCE-ID> --profile
  <AWS_PROFILE> --http-endpoint enabled --http-token required
output: null
created_at: '2023-04-06T03:56:09.189416+00:00'
updated_at: '2023-04-10T20:19:51.024180+00:00'
platforms:
  - AWS
tags:
  - aws
  - ec2
  - imdsv2
verified: true
validated: true
---

# aws-modify-instance-metadata-options-enable-imdsv2

## Command

```bash
aws ec2 modify-instance-metadata-options --instance-id <INSTANCE-ID> --profile <AWS_PROFILE> --http-endpoint enabled --http-token required
```

## Description

This AWS CLI command modifies the metadata options for a specified EC2 instance to enable IMDSv2, requiring session tokens for all metadata requests. Use this to harden instances against SSRF attacks targeting the metadata service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --instance-id <INSTANCE-ID> | The ID of the EC2 instance to modify (e.g., i-1234567890abcdef0) | Yes |
| --profile <AWS_PROFILE> | The name of the AWS CLI profile to use for authentication | No (defaults to default profile) |
| --http-endpoint enabled | Enables the HTTP endpoint for metadata requests | Yes (for this use case) |
| --http-token required | Requires a session token for all metadata requests (enforces IMDSv2) | Yes (for this use case) |

## Examples

### Basic Usage

```bash
aws ec2 modify-instance-metadata-options --instance-id i-1234567890abcdef0 --http-endpoint enabled --http-token required
```

### Advanced Usage

```bash
aws ec2 modify-instance-metadata-options --instance-id i-1234567890abcdef0 --profile my-prod-profile --http-endpoint enabled --http-token required --http-put-response-hop-limit 1
```

## Expected Output

Successful execution returns JSON like:

```json
{
    "InstanceId": "i-1234567890abcdef0",
    "InstanceMetadataOptions": {
        "State": "pending",
        "HttpTokens": "required",
        "HttpEndpoint": "enabled",
        "HttpPutResponseHopLimit": 1,
        "InstanceMetadataEndpointState": "enabled"
    }
}
```
The state changes to "applied" after a short time. Errors occur if the instance ID is invalid or permissions are insufficient.

## Related

- [[procedures/Protect-AWS-EC2-Metadata-from-SSRF-with-IMDSv2]]
