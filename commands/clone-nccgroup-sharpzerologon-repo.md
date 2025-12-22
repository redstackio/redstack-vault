---
id: ee86cbc8-633d-4048-ad23-c3a9d6c4eb3c
name: clone-nccgroup-sharpzerologon-repo
type: command
executor: bash
data: 'git clone https://github.com/nccgroup/nccfsas'
output: null
created_at: '2023-04-06T03:56:02.673309+00:00'
updated_at: '2023-04-10T20:36:01.289773+00:00'
platforms:
  - Linux
tags:
  - git
  - sharpzerologon
verified: true
validated: true
---

# clone-nccgroup-sharpzerologon-repo

## Command

```bash
git clone https://github.com/nccgroup/nccfsas
```

## Description

Clones the NCC Group repository containing the SharpZeroLogon .NET exploit binary.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/nccgroup/nccfsas | Repo URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/nccgroup/nccfsas
```

## Expected Output

```
Cloning into 'nccfsas'...
...
```

## Related

- [[procedures/ZeroLogon-Exploitation-and-Post-Exploitation]]
- [[commands/execute-sharpzerologon-check]]
