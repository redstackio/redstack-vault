---
id: cmd-uuid-placeholder
data: 'curl https://prow.k8s.io/config'
tags:
  - reconnaissance
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:12.542Z'
verified: false
validated: true
submitted: true
---
---

# curl-fetch-prow-config

## Command

```bash
curl https://prow.k8s.io/config
```

## Description

This command uses curl to fetch the publicly accessible YAML configuration file from the Kubernetes Prow system, disclosing internal details without authentication. It is useful for reconnaissance in cloud-native environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://prow.k8s.io/config` | The target URL for the Prow config endpoint | Yes |

## Examples

### Basic Usage

```bash
curl https://prow.k8s.io/config
```

### Advanced Usage

```bash
curl -o prow-config.yaml https://prow.k8s.io/config
```

> Saves the output to a file for offline analysis.

## Expected Output

A raw YAML stream starting with configuration sections like 'plank:', 'deck:', including details on jobs, secrets, and infrastructure. No errors if accessible; expect ~100KB+ of text with nested mappings.

## Related

- [[Related Procedure: Retrieve-Public-Prow-Config-YAML]]

---
