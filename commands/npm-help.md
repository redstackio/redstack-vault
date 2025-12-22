---
data: npm help
tags:
  - npm
  - recon
type: command
output: npm help documentation
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.388Z'
id: a01cb514-c266-495c-b834-14d1faa77704
verified: false
validated: true
submitted: true
---
# npm-help

## Command

```bash
npm help
```

## Description

Displays the npm help information, but in an attack context, triggers loading of local .npmrc files, potentially executing onload-scripts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; shows general help | No |

## Examples

### Basic Usage

```bash
npm help
```

### Advanced Usage

```bash
npm help install
```

## Expected Output

npm help documentation, including usage and commands list.

## Related

- [[commands/npm-whoami]]
- [[procedures/Trick-Victim-to-Run-npm]]
