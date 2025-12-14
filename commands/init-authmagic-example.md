---
id: cmd-736522-authmagic-init
data: authmagic init -e
tags:
  - initialization
  - authmagic
type: command
output: Example app structure set up
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.832Z'
verified: false
validated: true
submitted: true
---
# init-authmagic-example

## Command

```bash
authmagic init -e
```

## Description

Initializes the authmagic example application, configuring the project with the vulnerable timerange-stateless-core dependency for JWT auth testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-e` | Flag for example app initialization | Yes |

## Examples

### Basic Usage

```bash
authmagic init -e
```

### Advanced Usage

```bash
authmagic init -e --no-git
```

## Expected Output

Project files like server.js and config created; vulnerable module referenced in package.json.

## Related

- [[commands/install-authmagic-dependencies]]
- [[procedures/Initialize-and-Install-Authmagic-Example-App]]
