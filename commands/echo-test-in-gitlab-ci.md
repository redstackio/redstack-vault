---
data: echo test
tags:
  - ci
  - dummy
type: command
executor: bash
platforms:
  - Linux
id: 35e98250-8ca9-4625-ae2e-d3116815b840
created_at: '2025-12-13T23:52:24.576Z'
updated_at: '2025-12-13T23:52:24.576Z'
verified: false
validated: true
submitted: true
---
# echo-test-in-gitlab-ci

## Command

```bash
echo test
```

## Description

A simple bash command used as a dummy script in GitLab CI jobs to ensure job completion and artifact generation without performing actual work, printing 'test' to logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Basic echo with string argument | No |

## Examples

### Basic Usage

```bash
echo test
```

### Advanced Usage

```bash
echo "Dummy output for CI"
```

## Expected Output

'test' printed to stdout, visible in GitLab CI job logs.

## Related

- [[Related Procedure]]
