---
data: 'git clone https://github.com/whotwagner/logrotten.git /tmp/logrotten'
tags:
  - clone
  - exploit
type: command
output: |-
  Cloning into '/tmp/logrotten'...
  Unpacking objects: 100% (84/84), done.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.983Z'
id: e5601d86-413b-4e41-8170-a6ec427114bd
verified: false
validated: true
submitted: true
---
# git-clone-logrotten

## Command

```bash
git clone https://github.com/whotwagner/logrotten.git /tmp/logrotten
```

## Description

Clones the logrotten exploit repository from GitHub to /tmp/logrotten for building the race condition tool.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/whotwagner/logrotten.git | Repository URL | Yes |
| /tmp/logrotten | Target directory | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/whotwagner/logrotten.git /tmp/logrotten
```

### Advanced Usage

```bash
git clone --depth 1 https://github.com/whotwagner/logrotten.git /tmp/logrotten
```

## Expected Output

'Cloning into '/tmp/logrotten'... Unpacking objects: 100% (84/84), done.'

## Related

- [[commands/gcc-compile-logrotten]]
- [[procedures/Compile-and-Execute-Logrotten-Exploit]]
