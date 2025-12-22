---
id: 88f5662a-87e4-495a-aaa0-f2aa471962da
name: npm-publish-malicious
type: command
executor: bash
data: npm publish
output: null
created_at: '2025-12-11T03:47:40.395Z'
updated_at: '2025-12-11T03:47:40.395Z'
platforms:
  - Node.js
tags:
  - npm
  - publish
verified: false
validated: true
submitted: true
---

# npm-publish-malicious

## Command

```bash
npm publish
```

## Description

Publishes a package to the NPM registry, used here to upload malicious versions for dependency confusion attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Publishes the current package | No |

## Examples

### Basic Usage

```bash
npm publish
```

### Advanced Usage

```bash
npm publish --access public
```

## Expected Output

Package successfully published to the registry with confirmation message.

## Related

- [[commands/npm-install]]
- [[procedures/Publishing-Malicious-Packages-to-Public-NPM-Registry]]
