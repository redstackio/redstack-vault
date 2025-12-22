---
data: cat /etc/cron.daily/zzz-backdoor
tags:
  - verification
type: command
output: |-
  #!/bin/bash
  echo "Backdoor executed" > /tmp/backdoor.log
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.431Z'
id: 39d3e329-62fb-46a0-8040-82696594aa2a
verified: false
validated: true
submitted: true
---
# cat-cron-backdoor

## Command

```bash
cat /etc/cron.daily/zzz-backdoor
```

## Description

Displays the contents of the written backdoor file to confirm payload integrity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/etc/cron.daily/zzz-backdoor` | File path | Yes |

## Examples

### Basic Usage

```bash
cat /etc/cron.daily/zzz-backdoor
```

### Advanced Usage

```bash
cat /etc/cron.daily/zzz-backdoor | grep nc
```

## Expected Output

Script contents, e.g., shell code for reverse shell.

## Related

- [[commands/ls-cron-backdoor]]
