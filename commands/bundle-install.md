---
data: bundle install
tags:
  - dependencies
type: command
output: >-
  Fetching gem metadata... Installing actionpack-page_caching... Bundle
  complete!
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.425Z'
id: 3d6df762-a6f0-4144-ab06-c671c53b459d
verified: false
validated: true
submitted: true
---
# bundle-install

## Command

```bash
bundle install
```

## Description

Installs Ruby gems from Gemfile, including the vulnerable actionpack-page_caching.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses Gemfile | No |

## Examples

### Basic Usage

```bash
bundle install
```

## Expected Output

Gems installed successfully.

## Related

- [[commands/cd-app-dir]]
