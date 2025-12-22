---
type: command
executor: bash
data: >-
  wget https://github.com/DominicBreuker/pspy/releases/latest/download/pspy64 -O
  $_OUTPUT_FILE
output: null
platforms:
  - Linux
tags:
  - download
  - recon
verified: true
validated: true
---

# pspy-download-x86-64-binary

## Command

```bash
wget https://github.com/DominicBreuker/pspy/releases/latest/download/pspy64 -O $_OUTPUT_FILE
```

## Description

Downloads the static pspy64 binary for x86_64 Linux architecture from the official GitHub releases page. This binary allows process monitoring without root privileges and is saved to a specified location for immediate use during reconnaissance or post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_OUTPUT_FILE | Path where the binary will be saved (e.g., /tmp/pspy) | Yes |

## Examples

### Basic Usage

```bash
wget https://github.com/DominicBreuker/pspy/releases/latest/download/pspy64 -O /tmp/pspy
```

### Advanced Usage

For a different output location:

```bash
wget https://github.com/DominicBreuker/pspy/releases/latest/download/pspy64 -O ~/tools/pspy
```

## Expected Output

Successful download indicates the binary has been retrieved:

```
--2023-10-01 12:00:00--  https://github.com/DominicBreuker/pspy/releases/latest/download/pspy64
Resolving github.com (github.com)... 140.82.121.3
Connecting to github.com (github.com)|140.82.121.3|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2500000 (2.4M) [application/octet-stream]
Saving to: '/tmp/pspy'

/tmp/pspy  100%[===================>]   2.38M  --.-KB/s    in 0.5s

2023-10-01 12:00:01 (4.8 MB/s) - '/tmp/pspy' saved [2500000/2500000]
```

## Related

- [[tools/pspy]]
