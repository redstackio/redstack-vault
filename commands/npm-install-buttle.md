---
data: npm i buttle
tags:
  - install
  - npm
type: command
output: Installation logs and confirmation
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:30.831Z'
id: bdd14c9f-a1b7-4a24-9eb4-8361ed2fc94b
verified: false
validated: true
submitted: true
---
# npm-install-buttle

## Command

```bash
npm i buttle
```

## Description

Installs the buttle npm package (version 0.2.0 by default), a simple static file server vulnerable to XSS via directory listings. Use this in a Node.js project to set up the exploit environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Shorthand for install | Yes |
| `buttle` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm i buttle
```

### Advanced Usage

```bash
npm i buttle@0.2.0
```

## Expected Output

npm WARN deprecated ... (warnings), then added 1 package and audited X packages. Confirms installation in node_modules.

## Related

- [[Related Procedure]]
