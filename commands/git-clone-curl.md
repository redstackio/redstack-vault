---
id: cmd-004
data: 'git clone https://github.com/curl/curl.git'
tags:
  - clone
  - source
type: command
output: Cloned repository into curl directory
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.070Z'
verified: false
validated: true
submitted: true
---
# git-clone-curl

## Command

```bash
git clone https://github.com/curl/curl.git
```

## Description

Clones the official cURL GitHub repository for source code access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://github.com/curl/curl.git` | Repo URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/curl/curl.git
```

### Advanced Usage

```bash
git clone --depth 1 https://github.com/curl/curl.git
```

## Expected Output

Cloning into 'curl'... done.

## Related

- [[procedures/Building-cURL-with-Security-Debugging-Flags]]
- [[tools/git]]
