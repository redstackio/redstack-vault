---
id: 123e4567-e89b-12d3-a456-426614174004
name: npm-install-hnzserver
type: command
executor: bash
data: npm install -g hnzserver
output: Installation logs and confirmation of successful install of version 2.0.6
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.462Z'
platforms:
  - Linux
tags:
  - installation
  - npm
verified: false
validated: true
submitted: true
---

# npm-install-hnzserver

## Command

```bash
npm install -g hnzserver
```

## Description

This command installs the hnzserver Node.js module globally using npm, making it available as a system command for starting the static server. It is used in vulnerability reproduction to set up the affected package (v2.0.6).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Installs the package globally, adding it to the system PATH | Yes |
| `hnzserver` | The package name to install (defaults to latest version, which is 2.0.6 in this context) | Yes |

## Examples

### Basic Usage

```bash
npm install -g hnzserver
```

### Advanced Usage

```bash
npm install -g hnzserver@2.0.6
```

## Expected Output

npm will display download progress, dependency installation, and end with a message like "+ hnzserver@2.0.6" confirming global installation. Errors may occur if network issues or permission denials arise.

## Related

- [[commands/hnzserver-start]]
- [[procedures/Install-Vulnerable-hnzserver-Module]]
