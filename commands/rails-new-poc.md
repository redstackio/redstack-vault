---
data: rails new rails_server -G -M -O -C -A -J -T
tags:
  - setup
  - rails
  - poc
type: command
output: Creates the Rails app directory structure
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:43.915Z'
id: 2a3fc2f1-c8ca-4265-8564-49d4089c586b
verified: false
validated: true
submitted: true
---
# rails-new-poc

## Command

```bash
rails new rails_server -G -M -O -C -A -J -T
```

## Description

Generates a new minimal Rails 7.1.2 application named 'rails_server', skipping git, minitest, ORM, cookies, action mailer, spring, and test framework for a lightweight PoC.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rails_server | App name | Yes |
| -G | Skip git | No |
| -M | Skip minitest | No |
| -O | Skip ORM | No |
| -C | Skip cookies | No |
| -A | Skip action mailer | No |
| -J | Skip spring | No |
| -T | Skip test framework | No |

## Examples

### Basic Usage

```bash
rails new rails_server -G -M -O -C -A -J -T
```

### Advanced Usage

```bash
rails new myapp --skip-all
```

## Expected Output

create
 create  README.md
 ... (directory structure created)

## Related

- [[commands/ruby-version-check]]
