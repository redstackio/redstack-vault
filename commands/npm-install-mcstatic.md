---
data: npm install mcstatic
tags:
  - installation
  - node.js
type: command
executor: bash
platforms:
  - Linux
  - Node.js
id: ce6330bd-d81d-4657-9917-d9224614d5ca
created_at: '2025-12-14T17:26:12.251Z'
updated_at: '2025-12-14T17:26:12.251Z'
verified: false
validated: true
submitted: true
---
# npm-install-mcstatic

## Command

```bash
npm install mcstatic
```

## Description

This command installs the mcstatic Node.js package from the npm registry, specifically version 0.0.20 which contains the path traversal vulnerability, into the local node_modules directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `mcstatic` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm install mcstatic
```

### Advanced Usage

```bash
npm install mcstatic@0.0.20 --save
```

## Expected Output

Installation logs showing download progress, dependency resolution, and confirmation like "+ mcstatic@0.0.20 added 1 package in X s".

## Related

- [[Related Procedure|procedures/Install-mcstatic-Module]]
