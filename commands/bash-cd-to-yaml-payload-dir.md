---
id: 3e5fdb44-1522-4c26-9741-e194f1a2093a
type: command
executor: bash
data: cd yaml-payload
output: null
platforms:
  - Linux
  - macOS
tags:
  - bash
  - directory
created_at: '2023-04-06T03:55:59.656686+00:00'
updated_at: '2023-04-10T20:22:30.128005+00:00'
verified: true
validated: true
---

# bash-cd-to-yaml-payload-dir

## Command

```bash
cd yaml-payload
```

## Description

Changes the current working directory to the yaml-payload folder cloned from the repository, preparing for editing and compilation of the deserialization gadget.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| yaml-payload | Directory name | Yes |

## Examples

### Basic Usage

```bash
cd yaml-payload
```

### Verify Change

```bash
cd yaml-payload && pwd
```

## Expected Output

No output; shell prompt changes to reflect the new directory (e.g., /path/to/yaml-payload$).

## Related

- [[procedures/Remote-Code-Execution-via-Spring-Boot-Actuator-Env]]
