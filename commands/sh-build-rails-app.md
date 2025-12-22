---
data: sh ./build-rails-app.sh
tags:
  - script
  - rails
type: command
output: Script execution output including Rails generate commands
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:16.306Z'
id: de7563dc-9db8-445e-9c2b-a766075cccf5
verified: false
validated: true
submitted: true
---
# sh-build-rails-app

## Command

```bash
sh ./build-rails-app.sh
```

## Description

Executes a shell script to configure the Rails app with vulnerable endpoints, routes, and controllers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters | No |

## Examples

### Basic Usage

```bash
sh ./build-rails-app.sh
```

## Expected Output

Script output with generates for Poc1 and Poc2.

## Related

- [[commands/generate-poc1-controller]]
