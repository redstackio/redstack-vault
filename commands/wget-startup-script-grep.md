---
id: cmd-4
data: >-
  wget --header 'Metadata-Flavor: Google'
  http://metadata.google.internal/computeMetadata/v1/instance/attributes/startup-script
  -O- | grep ConfigBase
tags:
  - metadata
  - bucket
type: command
output: Line with ConfigBase
executor: bash
platforms:
  - GCP
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.547Z'
verified: false
validated: true
submitted: true
---
# wget-startup-script-grep

## Command

```bash
wget --header 'Metadata-Flavor: Google' http://metadata.google.internal/computeMetadata/v1/instance/attributes/startup-script -O- | grep ConfigBase
```

## Description

Fetches and filters the instance startup script from metadata to extract kOps ConfigBase (state bucket) info.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header` | Metadata auth | Yes |
| `-O-` | Stdout output | Yes |
| `| grep ConfigBase` | Filter for bucket | Yes |

## Examples

### Basic Usage

```bash
wget ... -O- | grep ConfigBase
```

### Advanced Usage

```bash
wget ... -O script.txt | grep -i config
```

## Expected Output

Line like 'ConfigBase: gs://kops-state-test/'.

## Related

- [[commands/wget-metadata-token]]
