---
data: npm i
tags:
  - npm
  - dependencies
  - setup
type: command
output: null
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.247Z'
id: 51849216-1540-41f6-baca-2fa5c7494996
verified: false
validated: true
submitted: true
---
# install-npm-dependencies

## Command

```bash
npm i
```

## Description

Installs Node.js dependencies listed in package.json for the meemo app.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| npm | Node Package Manager | Yes |
| i | Alias for install | Yes |

## Examples

### Basic Usage

```bash
npm i
```

### With Production Only

```bash
npm i --production
```

## Expected Output

Installation logs for packages like ldapjs, express; node_modules directory populated.

## Related

- [[commands/build-meemo-app]]
- [[procedures/Setup-Meemo-Environment-with-LDAP]]
