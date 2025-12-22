---
id: cmd-woocommerce-metadata
data: >-
  $value = wc_clean($_POST["name"]); ... $value = esc_sql($value); ...
  update_metadata('post', $_id, $key, $value );
tags:
  - sqli
  - unserialize
  - woocommerce
type: command
output: 'Metadata update, but potential unserialize of crafted payload'
executor: php
platforms:
  - WordPress
  - PHP
  - WooCommerce
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.713Z'
verified: false
validated: true
submitted: true
---
# update-metadata-with-esc-sql-in-woocommerce

## Command

```php
$value = wc_clean($_POST["name"]); ... $value = esc_sql($value); ... update_metadata('post', $_id, $key, $value );
```

## Description

Processes WooCommerce product name input, cleans and escapes it, then updates metadata; vulnerable to unserialize attacks via prepare() flaws when metadata is later queried/removed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| wc_clean($_POST["name"]) | Cleaned POST name | Yes |
| esc_sql($value) | Escaped value for SQL | Yes |

## Examples

### Basic Usage

```php
$value = wc_clean($_POST["name"]);
$value = esc_sql($value);
update_metadata('post', $id, 'product_name', $value);
```

### Advanced Usage

```php
// With payload in POST['name']
$_POST["name"] = "O:1:\"s\":1:\"{RCE}\";";
```

## Expected Output

Updated metadata row, but if payload unserializes on retrieval, leads to code execution.

## Related

- [[Related Procedure]]
