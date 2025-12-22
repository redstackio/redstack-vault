---
id: cmd-cd-snap-escape
data: cd snap-escape
tags:
  - navigation
  - cwd-setup
type: command
output: 'Prompt changes to itszn@ubuntu:snap-escape$'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.822Z'
verified: false
validated: true
submitted: true
---
# change-to-malicious-directory

## Command

```bash
cd snap-escape
```

## Description

Change current working directory to the extracted POC folder to enable library loading from malicious path.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| snap-escape | Target directory name | Yes |

## Examples

### Basic Usage

```bash
cd snap-escape
```

### Advanced Usage

```bash
cd snap-escape && ls
```

## Expected Output

Prompt changes to itszn@ubuntu:snap-escape$ with no stdout.

## Related

- [[commands/extract-snap-escape-poc]]
- [[procedures/Prepare-Malicious-Directory-for-Snap-RCE]]
