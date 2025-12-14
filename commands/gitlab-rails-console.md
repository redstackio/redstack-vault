---
id: uuid-rails-console
data: gitlab-rails console
tags:
  - rails
  - console
type: command
output: 'Rails console prompt (irb(main):001:0>)'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:24.483Z'
verified: false
validated: true
submitted: true
---
# gitlab-rails-console

## Command

```bash
gitlab-rails console
```

## Description

Starts an interactive Rails console session within GitLab for executing Ruby code, managing features, and querying the database.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
gitlab-rails console
```

### Advanced Usage

Run non-interactively:

```bash
gitlab-rails console -e production
```

## Expected Output

IRB prompt like irb(main):001:0> for entering Ruby commands.

## Related

- [[Related Procedure: Enable-Vue-Issuables-List-Feature-Flag]]
