---
data: npm install undici@5.13
tags:
  - setup
  - install
type: command
executor: bash
platforms:
  - Node.js
id: 26b243b2-1cd3-4404-a90b-4271e0b8d6f8
created_at: '2025-12-14T17:26:36.580Z'
updated_at: '2025-12-14T17:26:36.580Z'
verified: false
validated: true
submitted: true
---
# npm-install-undici-vulnerable

## Command

```bash
npm install undici@5.13
```

## Description

Installs the specific vulnerable version 5.13 of the undici npm package, which includes the ReDoS flaw in Headers processing. Use this in a Node.js project to set up exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| undici@5.13 | Specifies the exact vulnerable version to install | Yes |

## Examples

### Basic Usage

```bash
npm install undici@5.13
```

### Advanced Usage

```bash
npm install undici@5.13 --save
```

## Expected Output

Installation logs, e.g., 'added 1 package in 2s', with undici@5.13 in node_modules and package.json.

## Related

- [[Related Procedure: Install-Vulnerable-Undici-Version]]
