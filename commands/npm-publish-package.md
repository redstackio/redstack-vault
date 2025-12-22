---
data: npm publish
tags:
  - npm
  - publish
type: command
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
id: 0ebd8c55-71ba-4efc-b769-02f5ec7a559a
created_at: '2025-12-11T06:10:40.142Z'
updated_at: '2025-12-11T06:10:40.143Z'
verified: false
validated: true
submitted: true
---
# npm-publish-package

## Command

```bash
npm publish
```

## Description

Publishes the current package to the public NPM registry.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses current directory's package.json | N/A |

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

Confirmation of successful publish with version info.

## Related

- [[commands/npm-init]]
- [[procedures/Register-and-Upload-Malicious-NPM-Packages]]
