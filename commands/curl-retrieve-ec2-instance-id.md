---
id: 09ba0559-7d08-4bc9-97a8-45861135d99f
name: curl-retrieve-ec2-instance-id
type: command
executor: bash
data: 'curl http://169.254.169.254/latest/meta-data/instance-id'
output: null
created_at: '2023-04-06T03:56:13.480813+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - cloud
  - ec2
  - discovery
verified: true
validated: true
---

# curl-retrieve-ec2-instance-id

## Command

```bash
curl http://169.254.169.254/latest/meta-data/instance-id
```

## Description

This command queries the EC2 instance metadata service to retrieve the current instance's ID. Use it from within an EC2 instance to gather contextual information for mapping IAM policies or roles.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| http://169.254.169.254/latest/meta-data/instance-id | Fixed IMDS endpoint for instance ID | Yes |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/meta-data/instance-id
```

### Advanced Usage

```bash
curl -s http://169.254.169.254/latest/meta-data/instance-id | tee instance_id.txt
```

## Expected Output

```
i-1234567890abcdef0
```

Returns a unique instance ID string on success; empty or error if not on EC2 or IMDS is inaccessible.

## Related

- [[procedures/Gather-AWS-IAM-Policy-Version-Information]]
