---
id: cmd-uuid-004
data: >-
  // In miner.php: Process timings from data/*.txt; use 185B avg record size;
  cluster with cosine similarity, filter outliers, calc records = (est_size /
  185); adjust for subject=security
tags:
  - data-analysis
type: command
output: Calculated number of records based on (response size estimate / 185B)
executor: php
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.079Z'
verified: false
validated: true
submitted: true
---
# miner-php-process

## Command

```php
// In miner.php: Process timings from data/*.txt; use 185B avg record size; cluster with cosine similarity, filter outliers, calc records = (est_size / 185); adjust for subject=security
```

## Description

PHP script processes timing files to infer record counts using average JSON record size, clustering for accuracy.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 185B | Gzip-adjusted record size | Yes |
| data dir | Writable for .txt inputs | Yes |

## Examples

### Basic Usage

php miner.php

## Expected Output

"Estimated 3 records for triaged reports"

## Related

- [[Related Procedure: Process-Timings-for-Data-Inference]]
