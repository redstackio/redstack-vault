---
id: cmd-echo-after
data: >-
  echo "After script section" && echo "For example you might do some cleanup
  here"
tags:
  - setup
  - ci
type: command
output: |-
  "After script section"
  "For example you might do some cleanup here"
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:46.064Z'
verified: false
validated: true
submitted: true
---
# echo-after-script

## Command

```bash
echo "After script section" && echo "For example you might do some cleanup here"
```

## Description

Prints post-execution messages in GitLab CI after_script for pipeline validation during setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Echo statements | No |

## Examples

### Basic Usage

```bash
echo "After script section"
```

### Advanced Usage

```bash
echo "After script section" && echo "Cleanup"
```

## Expected Output

Echoed cleanup messages in pipeline logs.

## Related

- [[commands/echo-before-script]]
- [[procedures/Set-Up-GitLab-Project-with-CI-Pipeline]]
