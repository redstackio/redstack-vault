---
data: 'git clone https://github.com/transloadit/uppy'
tags:
  - setup
  - clone
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f10ed91a-8966-4459-829e-5e5e11d5d75a
created_at: '2025-12-14T03:16:14.070Z'
updated_at: '2025-12-14T03:16:14.070Z'
verified: false
validated: true
submitted: true
---
# git-clone-uppy

## Command

```bash
git clone https://github.com/transloadit/uppy
```

## Description

Clones the Uppy repository from GitHub to obtain the source code for local testing of the dashboard and vulnerability reproduction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/transloadit/uppy
```

### Advanced Usage

```bash
git clone https://github.com/transloadit/uppy.git uppy-local
```

## Expected Output

Downloads the source code into a local 'uppy' directory, showing progress and completion messages.

## Related

- [[Related Procedure: Setup-Uppy-Development-Environment]]
