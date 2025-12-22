---
id: cmd-run-scaling-script
data: ./run.sh
tags:
  - kubernetes
  - script
  - dos
type: command
output: Curl responses from scales
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.538Z'
verified: false
validated: true
submitted: true
---
# ./run.sh

## Command

```bash
./run.sh
```

## Description

Executes the bash script performing ~50 scale up/down cycles via curl.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| none | Runs as-is | No |

## Examples

### Basic Usage

```bash
./run.sh
```

### Advanced Usage

```bash
./run.sh > output.log 2>&1
```

## Expected Output

Series of HTTP 200/201 from curls; no summary, but leads to spikes.

## Related

- [[commands/curl-scale-up-deployment]]
- [[procedures/execute-kubernetes-scaling-script]]
