---
id: cmd-woo-meta-unserialize
data: >-
  $value = wc_clean($_POST["name"]); ... $value = esc_sql($value); ...
  update_metadata('post', $_id, $key, $value );
tags:
  - sqli
  - wordpress
  - woocommerce
type: command
output: null
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.573Z'
verified: false
validated: true
submitted: true
---
# wc-clean-esc-update-meta

## Command

```php
$value = wc_clean($_POST["name"]); ... $value = esc_sql($value); ... update_metadata('post', $_id, $key, $value );
```

## Description

From WooCommerce, processes product name with wc_clean and esc_sql before update_metadata, vulnerable to unserialize attacks if % replacements allow crafted serialized payloads to survive prepare().

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| esc_sql($value) | Escaped value for query | Yes |
| wc_clean($_POST["name"]) | Cleaned WooCommerce POST input | Yes |

## Examples

### Basic Usage

```php
$value = wc_clean($_POST["name"]);
$value = esc_sql($value);
update_metadata('post', $_id, $key, $value);
```

### Advanced Usage

```php
// Craft serialized payload with %
$payload = 'O:1:"a":1:{s:3:"b";s:1:"1";}';
```

## Expected Output

Metadata update, but % replacement allows crafted serialized payloads to survive and unserialize, e.g., object injection.

## Related

- [[Related Procedure]]
