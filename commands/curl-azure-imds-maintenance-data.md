---
id: abae7a87-9b24-4f1b-9321-df7185a4c5e8
name: curl-azure-imds-maintenance-data
type: command
executor: bash
data: 'curl "http://169.254.169.254/metadata/v1/maintenance" -H "Metadata: true"'
output: null
created_at: '2023-04-06T03:56:38.548065+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
  - Linux
tags:
  - ssrf
  - metadata
  - maintenance
verified: true
validated: true
---

# curl-azure-imds-maintenance-data

## Command

```bash
curl -H $_METADATA_HEADER "http://$_IMDS_HOST/metadata/v1/maintenance"
```

## Description

Fetches maintenance event data from Azure IMDS, including scheduled and past events for the VM. In SSRF exploitation, this reveals operational insights for timing attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_METADATA_HEADER | Required IMDS header | Yes |
| $_IMDS_HOST | IMDS endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -H 'Metadata: true' "http://169.254.169.254/metadata/v1/maintenance"
```

## Expected Output

JSON with maintenance details:
```
{
  "data": "https://maintenance.example",
  "lang": "en",
  "instruction": "Check events",
  "explain": "Maintenance details"
}
```

## Related

- [[procedures/Exploit-Azure-SSRF-to-Access-VM-Metadata-Service]]
- [[commands/curl-azure-imds-instance-metadata]]
