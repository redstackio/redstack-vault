---
id: 122ff930-17f5-4d35-b3ed-7a84a43501f9
type: command
executor: bash
data: 'run <module_name> [--keyword-arguments]'
output: null
created_at: '2023-04-06T03:56:08.937433+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - run
  - module
verified: true
validated: true
---

# Run Pacu Module with Arguments

## Command

```bash
run <module_name> [--keyword-arguments]
```

## Description

Executes a Pacu module with optional arguments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <module_name> | Name of module to run | Yes |
| --keyword-arguments | Module-specific options | No |

## Examples

### Basic Usage

```bash
run ec2_enum --usernames
```

## Expected Output

Running module... Results: X instances found.
