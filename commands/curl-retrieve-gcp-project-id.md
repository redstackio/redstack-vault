---
id: cmd-uuid-4
data: 'curl http://metadata.google.internal/computeMetadata/v1/project/project-id'
tags:
  - project-discovery
  - metadata
type: command
output: 'Project ID string, e.g., gitlab-ci-155816'
executor: bash
platforms:
  - Linux
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.511Z'
verified: false
validated: true
submitted: true
---
# curl-retrieve-gcp-project-id

## Command

```bash
curl http://metadata.google.internal/computeMetadata/v1/project/project-id
```

## Description

Retrieve the Google Cloud project ID from instance metadata via SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Metadata endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://metadata.google.internal/computeMetadata/v1/project/project-id
```

## Expected Output

Project ID string, e.g., gitlab-ci-155816.

## Related

- [[Related Procedure: Inspect-Token-Scopes-and-Retrieve-Project-ID]]
