---
data: npm search package-name
tags:
  - npm
  - recon
type: command
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
id: ccc32aa8-2e28-431d-8345-ed0bbbf1d765
created_at: '2025-12-11T06:10:40.147Z'
updated_at: '2025-12-11T06:10:40.147Z'
verified: false
validated: true
submitted: true
---
# npm-search

## Command

```bash
npm search package-name
```

## Description

Searches the public NPM registry for a given package name to check if it's registered.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `package-name` | Name of the package to search | Yes |

## Examples

### Basic Usage

```bash
npm search internal-package
```

### Advanced Usage

```bash
npm search internal-package --json
```

## Expected Output

List of matching packages or 'No matches found' if unregistered.

## Related

- [[commands/npm-publish-package]]
- [[procedures/Identify-Unregistered-Internal-NPM-Packages]]
