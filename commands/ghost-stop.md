---
data: ghost stop
tags:
  - management
  - ghost-cms
type: command
executor: bash
platforms:
  - Node.js
  - Linux
  - macOS
id: dcfeba0c-0319-46f3-900e-13f931d6a878
created_at: '2025-12-14T04:39:09.651Z'
updated_at: '2025-12-14T04:39:09.651Z'
verified: false
validated: true
submitted: true
---
# ghost-stop

## Command

```bash
ghost stop
```

## Description

Stops a running Ghost server instance, useful for restarting or troubleshooting during setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
ghost stop
```

### Advanced Usage

```bash
ghost stop --local
```

## Expected Output

Confirmation message like "Ghost has been stopped".

## Related

- [[commands/ghost-install-local]]
- [[procedures/Install-and-Setup-Ghost-Locally]]
