---
id: cmd-uuid-1
data: npm install hekto
tags:
  - install
  - npm
type: command
output: Installation logs and confirmation of package installation
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:27.095Z'
verified: false
validated: true
submitted: true
---
# install-hekto-module

## Command

```bash
npm install hekto
```

## Description

Installs the hekto Node.js module from the npm registry, used in the initial setup to reproduce the open redirect vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hekto | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm install hekto
```

### Advanced Usage

```bash
npm install hekto@0.2.3
```

## Expected Output

npm WARN deprecated logs if any, followed by added 1 package in X seconds, with hekto at version 0.2.3.

## Related

- [[Related Procedure|procedures/Install-Hekto-Module]]
