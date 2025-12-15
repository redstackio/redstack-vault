---
data: RAILS_ENV=production bundle exec rails runner traversal.rb
tags:
  - rails
  - token
type: command
output: >-
  Outputs serializer type, read token, read curl command, write target, write
  token, write curl command
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.362Z'
id: eca842ea-03c4-4048-8239-9fb9a53baf0a
verified: false
validated: true
submitted: true
---
# rails-runner-traversal

## Command

```bash
RAILS_ENV=production bundle exec rails runner traversal.rb
```

## Description

Execute a Ruby script to generate signed traversal tokens using MessageVerifier.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| RAILS_ENV=production | Environment | Yes |

## Examples

### Basic Usage

```bash
RAILS_ENV=production bundle exec rails runner traversal.rb
```

## Expected Output

Serializer: json
Read token: eyJfcmFpbHMiOnsiZGF0YSI6... 
Read curl: curl "http://..."

## Related

- [[commands/curl-read-traversal]]
