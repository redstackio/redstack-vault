---
id: cmd-uuid-1
data: npm install public
tags:
  - installation
  - npm
type: command
output: 'Installation logs, places module in node_modules/public'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.873Z'
verified: false
validated: true
submitted: true
---
# npm-install-public

## Command

```bash
npm install public
```

## Description

Installs the 'public' Node.js module from the npm registry, used for setting up the vulnerable static file server in XSS exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| public | Package name to install (vulnerable v0.1.3 by default) | Yes |
| -g (optional) | Install globally instead of locally | No |

## Examples

### Basic Usage

```bash
npm install public
```

### Advanced Usage

```bash
npm install public@0.1.3
```

## Expected Output

npm WARN deprecated ... (warnings), then added 1 package in X s, with node_modules/public created containing bin/public.

## Related

- [[commands/run-public-server]]
- [[procedures/Install-Vulnerable-Public-Module]]
