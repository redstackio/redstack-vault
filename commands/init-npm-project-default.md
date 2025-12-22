---
id: cmd-736522-npm-init
data: npm init -y
tags:
  - initialization
  - npm
type: command
output: package.json created with default settings
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.835Z'
verified: false
validated: true
submitted: true
---
# init-npm-project-default

## Command

```bash
npm init -y
```

## Description

Initializes a new Node.js project with default package.json settings, skipping interactive prompts; crucial to avoid naming conflicts in authmagic setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-y` | Yes flag to use defaults | Yes |

## Examples

### Basic Usage

```bash
npm init -y
```

### Advanced Usage

```bash
npm init -y && npm pkg set name="not-authmagic"
```

## Expected Output

'Wrote to .../package.json'. File includes basic fields like name, version.

## Related

- [[commands/install-authmagic-dependencies]]
- [[procedures/Initialize-and-Install-Authmagic-Example-App]]
