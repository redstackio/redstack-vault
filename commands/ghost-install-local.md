---
data: ghost install local
tags:
  - setup
  - ghost-cms
type: command
executor: bash
platforms:
  - Node.js
  - Linux
  - macOS
id: 81d32972-e5cb-4e73-9a43-9b41039ba9b2
created_at: '2025-12-14T04:39:09.656Z'
updated_at: '2025-12-14T04:39:09.656Z'
verified: false
validated: true
submitted: true
---
# ghost-install-local

## Command

```bash
ghost install local
```

## Description

Deploys Ghost CMS in a local development environment, setting up a SQLite database by default and starting the server on port 2368.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `local` | Specifies the installation mode for local/dev setup | Yes |

## Examples

### Basic Usage

```bash
ghost install local
```

### Advanced Usage

```bash
ghost install local --db mysql --dbhost localhost
```

## Expected Output

Interactive prompts for config, followed by "Ghost installed" and server start message with admin URL.

## Related

- [[commands/npm-install-ghost-cli]]
- [[procedures/Install-and-Setup-Ghost-Locally]]
