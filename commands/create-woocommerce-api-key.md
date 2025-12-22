---
id: cmd-woocommerce-key-gen
data: >-
  wp woocommerce key generate --user=1 --permissions=read_write
  --description="Test Key"
tags:
  - api
  - woocommerce
type: command
output: null
executor: bash
platforms:
  - Linux
  - WordPress
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:14.191Z'
verified: false
validated: true
submitted: true
---
# create-woocommerce-api-key

## Command

```bash
wp woocommerce key generate --user=1 --permissions=read_write --description="Test Key"
```

## Description

Generates a WooCommerce REST API key using WP-CLI for a specified user with read_write permissions, useful for setting up access in security testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--user` | WordPress user ID | Yes |
| `--permissions` | Access level (read, write, read_write) | Yes |
| `--description` | Key description | No |

## Examples

### Basic Usage

```bash
wp woocommerce key generate --user=1 --permissions=read_write
```

### Advanced Usage

```bash
wp woocommerce key generate --user=1 --permissions=read_write --description="Audit Key" --user-friendly-name="Security Test"
```

## Expected Output

Success: Generated key: ck_xxxxxxxxxxxxxxxxxxxxxx, secret: cs_xxxxxxxxxxxxxxxxxxxxxx. Key added to database.

## Related

- [[Related Procedure]]
