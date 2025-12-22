---
id: bf534e21-0042-4fde-8af5-8912e974adf1
type: command
executor: bash
data: 'curl -H ''Metadata-Flavor: DigitalOcean'' http://169.254.169.254/metadata/v1/'
output: null
created_at: '2023-04-06T03:56:38.436689+00:00'
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

# curl-do-metadata-from-droplet

## Command

```bash
curl -H 'Metadata-Flavor: DigitalOcean' http://169.254.169.254/metadata/v1/
```

## Description

General command to retrieve metadata from within a DigitalOcean Droplet using the required header. Adapt the path for specific data in SSRF payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H 'Metadata-Flavor: DigitalOcean' | Authenticates internal request | Yes |
| Path | Append to /metadata/v1/ for specific data | No |

## Examples

### Basic Usage

```bash
curl -H 'Metadata-Flavor: DigitalOcean' http://169.254.169.254/metadata/v1/
```

## Expected Output

Available endpoints list

## Related

- [[procedures/Exploit-SSRF-to-Access-Cloud-Metadata]]
- [[commands/curl-do-metadata]]
