---
id: 9dd58758-6265-4cd9-be75-430dae344974
name: git-clone-dvcs-ripper-repo
type: command
executor: bash
data: 'git clone https://github.com/kost/dvcs-ripper $_TARGET_DIR'
output: null
created_at: '2023-04-06T03:55:59.981694+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - git
  - clone
  - tool-install
verified: true
validated: true
---

# git-clone-dvcs-ripper-repo

## Command

```bash
git clone https://github.com/kost/dvcs-ripper $_TARGET_DIR
```

## Description

Clones the DVCS-Ripper repository from GitHub to obtain the rip-git tool for recovering exposed Git repositories. Use this as the first step in the recovery procedure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DIR | Local directory to clone into (optional; defaults to current dir) | No |

## Examples

### Basic Usage

```bash
git clone https://github.com/kost/dvcs-ripper
```

### Advanced Usage

```bash
git clone https://github.com/kost/dvcs-ripper ./tools/
```

## Expected Output

Cloning into 'dvcs-ripper'...
remote: Enumerating objects: 123, done.
remote: Total 123 (delta 0), reused 0 (delta 0), pack-reused 123
Receiving objects: 100% (123/123), done.

## Related

- [[procedures/Recover-Git-Repository-from-Exposed-Dot-Git-Directory]]
- [[tools/DVCS-Ripper]]
