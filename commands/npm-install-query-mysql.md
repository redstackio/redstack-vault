---
data: npm install query-mysql
tags:
  - setup
  - npm
type: command
output: Module installed in node_modules
executor: bash
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.075Z'
id: 2ffdfb01-2459-44a5-81de-8b815c31453a
verified: false
validated: true
submitted: true
---
# npm-install-query-mysql

## Command

```bash
npm install query-mysql
```

## Description

Installs the query-mysql Node.js module from the npm registry, adding it as a dependency for projects vulnerable to SQL injection due to unsanitized query building.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| install | Installs package | Yes |
| query-mysql | Package name (v0.0.2 vulnerable) | Yes |

## Examples

### Basic Usage

```bash
npm install query-mysql
```

### With Save Flag

```bash
npm install query-mysql --save
```

## Expected Output

added 1 package in X s; query-mysql@0.0.2 in node_modules.

## Related

- [[Related Procedure|procedures/Install-query-mysql-Module]]
