---
data: npm install -g http-file-server
tags:
  - installation
  - nodejs
type: command
output: Installation logs and success message
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.253Z'
id: b7733909-eb97-44ae-a25a-ebc9d17f2f55
verified: false
validated: true
submitted: true
---
# npm-install-global-http-file-server

## Command

```bash
npm install -g http-file-server
```

## Description

Installs the http-file-server Node.js module globally via npm, allowing the 'http-file-server' CLI tool to be executed from any directory for vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Installs the package globally | Yes |

## Examples

### Basic Usage

```bash
npm install -g http-file-server
```

### Advanced Usage

```bash
npm install -g http-file-server@0.2.6
```

## Expected Output

npm WARN deprecated ... (warnings)
+ http-file-server@0.2.6
added 1 package in 2s

## Related

- [[Related Procedure|procedures/Install-http-file-server-Module]]
