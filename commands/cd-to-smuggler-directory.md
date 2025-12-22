---
type: command
executor: bash
data: cd smuggler
output: null
platforms:
  - linux
  - macos
tags:
  - setup
  - navigation
verified: true
validated: true
---

# Cd to Smuggler Directory

## Command

```bash
cd smuggler
```

## Description

This command changes the current working directory to the cloned Smuggler tool folder, allowing execution of the Python script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| smuggler | Directory name | Yes |

## Examples

### Basic Usage

```bash
cd smuggler
```

## Expected Output

No output; the prompt changes to reflect the new directory (verify with `pwd`).

## Related

- [[procedures/http-request-smuggling-detection-and-exploitation]]
- [[commands/git-clone-smuggler-repository]]
