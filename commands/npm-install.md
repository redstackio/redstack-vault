---
id: 46e90f66-7aaa-44a7-9baf-87a5d4aeeba8
name: npm-install
type: command
executor: bash
data: npm install
output: null
created_at: '2025-12-11T03:47:40.254Z'
updated_at: '2025-12-11T03:47:40.254Z'
platforms:
  - Node.js
tags:
  - npm
  - install
verified: false
validated: true
submitted: true
---

# npm-install

## Command

```bash
npm install
```

## Description

Installs dependencies for a Node.js project, which in this context pulls malicious packages due to misconfiguration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Installs from package.json | No |

## Examples

### Basic Usage

```bash
npm install
```

### Advanced Usage

```bash
npm install --production
```

## Expected Output

Dependencies installed, potentially including malicious ones.

## Related

- [[commands/npm-publish-malicious]]
- [[procedures/Triggering-Malicious-Package-Installation-in-Node.js-Builds]]
