---
data: 'curl "http://localhost:3000/books/1"'
tags:
  - http
  - verification
type: command
output: HTML response with book details and escaped payload
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.408Z'
id: ac81cf53-0fea-4dca-ab97-5528c1f684af
verified: false
validated: true
submitted: true
---
# curl-book-show

## Command

```bash
curl "http://localhost:3000/books/1"
```

## Description

Fetches the book show page to trigger caching.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl "http://localhost:3000/books/1"
```

## Expected Output

HTML with cached content.

## Related

- [[commands/ls-public-dir]]
