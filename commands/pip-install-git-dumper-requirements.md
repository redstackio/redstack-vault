---
id: 7b09503d-3c08-4b27-8ba9-1b254fc30b58
name: pip-install-git-dumper-requirements
type: command
executor: bash
data: pip install -r requirements.txt
output: null
created_at: '2023-04-06T03:55:59.891815+00:00'
updated_at: '2023-04-10T20:33:54.555211+00:00'
platforms:
  - Linux
tags:
  - pip
  - installation
  - dependencies
verified: true
validated: true
---

# pip-install-git-dumper-requirements

## Command

```bash
pip install -r requirements.txt
```

## Description

This command installs the Python dependencies required by git-dumper, such as requests for HTTP handling and GitPython for repository manipulation, from the requirements.txt file in the cloned directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r requirements.txt | Path to the requirements file listing dependencies | Yes |

## Examples

### Basic Usage

```bash
pip install -r requirements.txt
```

### In Virtual Environment

```bash
python -m venv env && source env/bin/activate && pip install -r requirements.txt
```

## Expected Output

Collecting requests (from -r requirements.txt (line 1))
  Downloading requests-2.28.1-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.8/62.8 kB 1.2 MB/s eta 0:00:00
Collecting GitPython (from -r requirements.txt (line 2))
  Downloading GitPython-3.1.30-py3-none-any.whl (184 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 184.0/184.0 kB 2.1 MB/s eta 0:00:00
Successfully installed GitPython-3.1.30 requests-2.28.1

## Related

- [[procedures/Recover-Source-Code-from-Insecure-Git-Repository-Using-Git-Dumper]]
- [[tools/git-dumper]]
