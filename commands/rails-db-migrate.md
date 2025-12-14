---
data: 'rails db:migrate'
tags:
  - database
type: command
output: '== 20231001000000 CreateBooks: migrating ... == CreateBooks: migrated'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.420Z'
id: ff262a0d-8886-4f34-9cdb-61da35be20ac
verified: false
validated: true
submitted: true
---
# rails-db-migrate

## Command

```bash
rails db:migrate
```

## Description

Runs pending database migrations for the scaffold.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses db/migrate files | No |

## Examples

### Basic Usage

```bash
rails db:migrate
```

## Expected Output

Database schema updated with books table.

## Related

- [[commands/rails-generate-scaffold]]
