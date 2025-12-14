---
data: ls
tags:
  - recon
  - file-system
type: command
output: >-
  app bin config config.ru db deploy dev.yml doc Gemfile Gemfile.lock
  integration lib log misc package.json public railgun.yml Rakefile README.md
  script service.yml spec tmp vendor yarn.lock
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.383Z'
id: b64fc16f-2a2b-497d-8ba0-b5d835e09c45
verified: false
validated: true
submitted: true
---
# ls-directory

## Command

```bash
ls
```

## Description

Lists contents of the current directory in the shell to explore the Rails application structure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
ls
```

## Expected Output

app bin config ... yarn.lock

## Related

- [[commands/cat-readme-md]]
