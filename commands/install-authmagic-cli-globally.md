---
id: cmd-736522-npm-install-cli
data: npm install -g authmagic-cli
tags:
  - installation
  - npm
  - global
type: command
output: authmagic-cli installed globally
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.838Z'
verified: false
validated: true
submitted: true
---
# install-authmagic-cli-globally

## Command

```bash
npm install -g authmagic-cli
```

## Description

Installs the authmagic CLI tool globally via npm, enabling commands like 'authmagic init' for setting up the example app with the vulnerable module.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Global installation flag | Yes |
| `authmagic-cli` | Package name | Yes |

## Examples

### Basic Usage

```bash
npm install -g authmagic-cli
```

### Advanced Usage

```bash
npm install -g authmagic-cli --registry https://registry.npmjs.org
```

## Expected Output

Progress indicators and 'added X packages in Ys'. Verify with `authmagic --version`.

## Related

- [[commands/init-authmagic-example]]
- [[procedures/Initialize-and-Install-Authmagic-Example-App]]
