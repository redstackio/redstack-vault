---
type: command
executor: bash
data: 'git clone https://github.com/defparam/smuggler.git'
output: null
platforms:
  - linux
  - macos
tags:
  - setup
  - tool-install
verified: true
validated: true
---

# Git Clone Smuggler Repository

## Command

```bash
git clone https://github.com/defparam/smuggler.git
```

## Description

This command downloads the Smuggler tool repository from GitHub, which is used for HTTP Request Smuggling detection and exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/defparam/smuggler.git | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/defparam/smuggler.git
```

### With Specific Directory

```bash
git clone https://github.com/defparam/smuggler.git ./tools/smuggler
```

## Expected Output

Cloning into 'smuggler'...
remote: Enumerating objects: ..., done.
remote: Total ... (delta ...), reused ... (delta ...), pack-reused 0
Receiving objects: 100% (...), ... KiB | ... KiB/s, done.

## Related

- [[procedures/http-request-smuggling-detection-and-exploitation]]
- [[tools/smuggler]]
