---
id: cmd-736522-authmagic-install
data: authmagic install
tags:
  - installation
  - dependencies
type: command
output: 'All npm dependencies installed, including authmagic-timerange-stateless-core'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.829Z'
verified: false
validated: true
submitted: true
---
# install-authmagic-dependencies

## Command

```bash
authmagic install
```

## Description

Installs all project dependencies, including the vulnerable authmagic-timerange-stateless-core@0.0.9, preparing the app for vulnerability testing.

## Parameters

None.

## Examples

### Basic Usage

```bash
authmagic install
```

### Advanced Usage

```bash
authmagic install --production
```

## Expected Output

npm install progress; 'added X packages'. node_modules folder created.

## Related

- [[commands/start-authmagic-server]]
- [[procedures/Initialize-and-Install-Authmagic-Example-App]]
