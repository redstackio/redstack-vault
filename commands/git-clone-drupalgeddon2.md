---
id: cmd-001
data: 'git clone https://github.com/dreadlocked/Drupalgeddon2.git && cd Drupalgeddon2'
tags:
  - setup
  - git
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.686Z'
verified: false
validated: true
submitted: true
---
# git-clone-drupalgeddon2

## Command

```bash
git clone https://github.com/dreadlocked/Drupalgeddon2.git && cd Drupalgeddon2
```

## Description

Clones the Drupalgeddon2 exploit repository from GitHub and changes into the directory for setup. Use this to obtain the RCE exploit script for CVE-2018-7600.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| repository_url | GitHub URL for Drupalgeddon2 | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/dreadlocked/Drupalgeddon2.git && cd Drupalgeddon2
```

### Advanced Usage

Not applicable; single clone operation.

## Expected Output

Downloads the exploit files into a new directory named Drupalgeddon2, with output like 'Cloning into 'Drupalgeddon2'...'

## Related

- [[Related Procedure: Download-and-Setup-Drupalgeddon2-Exploit]]
