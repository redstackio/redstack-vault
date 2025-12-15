---
data: 'rails generate scaffold book name:string'
tags:
  - scaffold
type: command
output: invoke  active_record ... create  app/models/book.rb ...
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.423Z'
id: e6d26ca0-5742-402b-9f10-815e235b2be4
verified: false
validated: true
submitted: true
---
# rails-generate-scaffold

## Command

```bash
rails generate scaffold book name:string
```

## Description

Generates a full scaffold for Book model with name attribute.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| book | Model name | Yes |
| name:string | Attribute | Yes |

## Examples

### Basic Usage

```bash
rails generate scaffold book name:string
```

## Expected Output

Model, controller, views, migration files created.

## Related

- [[commands/rails-db-migrate]]
