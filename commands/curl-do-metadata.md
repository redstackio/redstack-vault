---
id: 0106888f-57a7-4375-b470-3ecd952acb5b
type: command
executor: bash
data: 'curl -H ''Metadata-Flavor: DigitalOcean'' http://169.254.169.254/metadata/v1/'
output: null
created_at: '2023-04-06T03:56:38.436450+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - DigitalOcean
  - Linux
tags:
  - ssrf
  - metadata
verified: true
validated: true
---

# curl-do-metadata

## Command

```bash
curl -H 'Metadata-Flavor: DigitalOcean' http://169.254.169.254/metadata/v1/
```

## Description

Accesses the root metadata endpoint for a DigitalOcean Droplet, requiring the Metadata-Flavor header. Use in SSRF to list available data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H 'Metadata-Flavor: DigitalOcean' | Authenticates the metadata request | Yes |

## Examples

### Basic Usage

```bash
curl -H 'Metadata-Flavor: DigitalOcean' http://169.254.169.254/metadata/v1/
```

## Expected Output

id
hostname
region
...

## Related

- [[procedures/Exploit-SSRF-to-Access-Cloud-Metadata]]
- [[commands/curl-do-metadata-json]]
