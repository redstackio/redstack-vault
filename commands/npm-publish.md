---
id: cmd-003
data: npm publish
tags:
  - publish
  - npm
type: command
output: |-
  npm notice 
  npm notice package: yelp-js-infra@1.0.0
  npm notice === Tarball Contents ===
  ... + yelp-js-infra@1.0.0
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:17.610Z'
verified: false
validated: true
submitted: true
---
---
# npm-publish

## Command

```bash
npm publish
```

## Description

Publishes an NPM package to the public registry, allowing hijacking of unclaimed internal names for malicious code execution during installs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses package.json for details | No |

## Examples

### Basic Usage

```bash
npm publish
```

### Advanced Usage

```bash
npm publish --tag beta
```

## Expected Output

Confirmation of package publication with version.

## Related

- [[Related Procedure: Exploit-NPM-Dependency-Confusion-on-Developer-Machines]]
---
