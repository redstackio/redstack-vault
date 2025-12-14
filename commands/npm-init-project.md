---
data: npm init -y
tags:
  - setup
  - node-js
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: bb61e4bb-c37f-48e8-a34f-015e44f36cea
created_at: '2025-12-13T23:56:19.652Z'
updated_at: '2025-12-13T23:56:19.652Z'
verified: false
validated: true
submitted: true
---
# npm-init-project

## Command

```bash
npm init -y
```

## Description

Initializes a new Node.js project with default settings, creating a package.json file without interactive prompts. Used in attack setups to prepare for dependency installation like Express for hosting malicious content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-y` | Accepts all defaults without prompting | Yes |

## Examples

### Basic Usage

```bash
npm init -y
```

### Advanced Usage

```bash
npm init -y --scope=@attacker
```

## Expected Output

Creates package.json with basic configuration, e.g., {"name":"xss-server","version":"1.0.0",...}. May warn about missing fields like README.

## Related

- [[commands/npm-install-express]]
- [[procedures/Set-Up-Malicious-Express-Server-for-XSS]]
