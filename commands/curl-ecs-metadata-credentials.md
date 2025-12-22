---
id: 6c744863-d1a8-42c9-8e21-801c307cbd20
name: curl-ecs-metadata-credentials
type: command
executor: bash
data: 'curl http://169.254.170.2/v2/credentials/$_TASK_UUID'
output: null
created_at: '2023-04-06T03:56:38.241183+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
  - Linux
tags:
  - aws
  - metadata
  - credentials
verified: true
validated: true
---

# curl-ecs-metadata-credentials

## Command

```bash
curl http://169.254.170.2/v2/credentials/$_TASK_UUID
```

## Description

This command queries the AWS ECS task metadata service (version 2) to retrieve temporary IAM credentials for the specified task UUID. It is typically used internally on the ECS container to obtain role-based access keys without static credentials. In SSRF contexts, this is triggered via payloads to leak the output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TASK_UUID | The UUID or relative URI of the ECS task (e.g., from environment variables) | Yes |
| -s | Silent mode (optional, suppresses progress) | No |

## Examples

### Basic Usage

```bash
curl http://169.254.170.2/v2/credentials/my-task-uuid
```

### With Token (for IMDSv2)

First get token: curl -X PUT "http://169.254.170.2/v2/metadata" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" -d ""
Then: curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.170.2/v2/credentials/$_TASK_UUID

## Expected Output

JSON with credentials:

{
  "AccessKeyId" : "ASIA...",
  "SecretAccessKey" : "...",
  "Token" : "...",
  "Expiration" : "2023-..."
}

Success is valid JSON without 404 or auth errors; credentials can be tested with AWS CLI.
