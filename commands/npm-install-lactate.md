---
id: cmd-npm-install-001
name: npm-install-lactate
type: command
executor: bash
data: npm install -g lactate
output: Installation logs and confirmation of lactate version 0.13.12
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.001Z'
platforms:
  - Linux
tags:
  - installation
  - npm
verified: false
validated: true
submitted: true
---

# npm-install-lactate

## Command

```bash
npm install -g lactate
```

## Description

Globally installs the lactate Node.js package via npm, making the vulnerable web server binary available system-wide for setup in a test environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Installs globally | Yes |
| `lactate` | Package name | Yes |

## Examples

### Basic Usage

```bash
npm install -g lactate
```

### Advanced Usage

```bash
npm install -g lactate@0.13.12
```

## Expected Output

npm WARN deprecated ... (warnings if any), then "+ lactate@0.13.12" and "added X packages".

## Related

- [[commands/lactate-start-server]]
- [[procedures/Install-and-Setup-Lactate-Server]]
