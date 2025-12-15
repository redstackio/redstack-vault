---
id: cmd-npm-install
data: npm install simplehttpserver -g
tags:
  - package-manager
  - installation
type: command
output: Installation progress and 'added X packages'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.616Z'
verified: false
validated: true
submitted: true
---
# npm-install-simplehttpserver

## Command

```bash
npm install simplehttpserver -g
```

## Description

Installs the simplehttpserver Node.js package globally from the npm registry, enabling the vulnerable HTTP server for path traversal exploitation setups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Global installation (system-wide access) | Yes |
| `simplehttpserver` | Package name (v0.2.1 vulnerable version) | Yes |

## Examples

### Basic Usage

```bash
npm install simplehttpserver -g
```

### Advanced Usage

```bash
npm install simplehttpserver@0.2.1 -g  # Pin to vulnerable version
```

## Expected Output

Logs show fetching and installing, ending with 'added 1 package in Xs'. Verify with `which simplehttpserver`.

## Related

- [[Related Procedure: Install Vulnerable simplehttpserver Module]]
