---
data: npm install -g serve-here@3.2.0
tags:
  - installation
  - npm
type: command
output: null
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.890Z'
id: c0eeadd3-a590-44c4-a308-ab218fba66ec
verified: false
validated: true
submitted: true
---
# npm-install-serve-here

## Command

```bash
npm install -g serve-here@3.2.0
```

## Description

This command installs the serve-here package version 3.2.0 globally using npm, making the 'here' binary available system-wide for starting the vulnerable static web server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Install globally | Yes |
| `serve-here@3.2.0` | Package name and vulnerable version | Yes |

## Examples

### Basic Usage

```bash
npm install -g serve-here@3.2.0
```

### Advanced Usage

```bash
npm install serve-here@3.2.0 --save-dev
```

(Installs locally as a dev dependency)

## Expected Output

Installation progress and confirmation: "added 1 package in Xms" with no errors, and 'here --version' returns 3.2.0.

## Related

- [[commands/here-start-server]]
- [[procedures/Install-and-Setup-serve-here]]
