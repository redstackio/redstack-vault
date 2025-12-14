---
data: 'bin/rails active_storage:install'
tags:
  - rails
  - activestorage
type: command
output: ActiveStorage installation complete
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.371Z'
id: 8929ffb4-35f4-4b0a-a345-210a1998c175
verified: false
validated: true
submitted: true
---
# rails-activestorage-install

## Command

```bash
bin/rails active_storage:install
```

## Description

Install ActiveStorage by generating migrations and configurations for blob storage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
bin/rails active_storage:install
```

## Expected Output

create  db/migrate/..._active_storage_create_table.rb

## Related

- [[commands/rails-db-migrate]]
