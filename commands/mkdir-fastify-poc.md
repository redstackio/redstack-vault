---
data: mkdir fastify-rce-poc && cd fastify-rce-poc
tags:
  - setup
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.776Z'
id: db0c93de-4a9d-4e2a-a727-c9b98a8e2dc0
verified: false
validated: true
submitted: true
---
# mkdir-fastify-poc

## Command

```bash
mkdir fastify-rce-poc && cd fastify-rce-poc
```

## Description

Creates a new directory for the Fastify RCE PoC and changes the current working directory into it, preparing the environment for dependency installation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| fastify-rce-poc | Directory name for the PoC project | Yes |

## Examples

### Basic Usage

```bash
mkdir fastify-rce-poc && cd fastify-rce-poc
```

### Advanced Usage

```bash
mkdir my-poc && cd my-poc
```

## Expected Output

New directory created and current working directory changed to /path/to/fastify-rce-poc.

## Related

- [[Related Procedure: Setup-Vulnerable-Fastify-Environment]]
