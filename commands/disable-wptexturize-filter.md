---
id: cmd-disable-wptexturize
data: 'add_filter( ''run_wptexturize'', ''__return_false'' );'
tags:
  - wordpress
  - filter
  - bypass
type: command
output: null
executor: php
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.101Z'
verified: false
validated: true
submitted: true
---
# disable-wptexturize-filter

## Command

```php
add_filter( 'run_wptexturize', '__return_false' );
```

## Description

This WordPress PHP function adds a filter hook that disables the wptexturize process, preventing automatic conversion of plain text to styled HTML entities, which is useful for injecting raw HTML/JS in content fields without escaping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `run_wptexturize` | The filter name to hook into, controlling texturize execution | Yes |
| `__return_false` | Built-in callback that returns false to block the filter | Yes |

## Examples

### Basic Usage

```php
add_filter( 'run_wptexturize', '__return_false' );
```

### Advanced Usage

```php
// Conditional disable, e.g., only on specific post types
add_filter( 'run_wptexturize', function() { return false; }, 10, 1 );
```

## Expected Output

No direct output; the filter is silently disabled site-wide after saving functions.php and reloading. Verify by inputting raw HTML in a form and checking database storage.

## Related

- [[Related Procedure|procedures/Disable-WPTexturize-Filter]]
