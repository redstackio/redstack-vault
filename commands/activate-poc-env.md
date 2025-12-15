---
data: .\poc_env\Scripts\activate
tags:
  - setup
  - python-env
type: command
output: Virtual environment activated in command prompt
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.576Z'
id: a529b293-e7fc-4544-9d7f-cee8bde3a802
verified: false
validated: true
submitted: true
---
# activate-poc-env

## Command

```cmd
.\poc_env\Scripts\activate
```

## Description

Activates a Python 3 virtual environment for running the CS:GO exploit PoC script, ensuring dependencies like struct and protobuf libraries are available.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| poc_env | Path to virtual environment directory | Yes |

## Examples

### Basic Usage

```cmd
.\poc_env\Scripts\activate
```

### Advanced Usage

Use full path if not in current dir:
```cmd
C:\path\to\poc_env\Scripts\activate
```

## Expected Output

Command prompt changes to (poc_env) C:\path\> indicating activation.

## Related

- [[commands/run-poc-script]]
