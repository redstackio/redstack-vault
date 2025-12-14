---
data: 'estk --url=https://elasticsearch.example.com:9200 list'
tags:
  - elasticsearch
  - discovery
type: command
output: |-
  2023/10/29 17:24:51 Detecting version...
  2023/10/29 17:24:51 Trying elasticsearch
  2023/10/29 17:24:53 Found elasticsearch, major version 2
  Indices: 3, document count: 2212, size: 5.9 MB
  Found index aim_high with 2211 documents (5.9 MB)
  Found index .opensearch-observability with 0 documents (208 B)
  Found index .kibana_1 with 1 documents (5.3 kB)
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-30T00:00:00Z'
updated_at: '2025-12-14T17:31:19.282Z'
id: 0873c51e-e8e3-4471-a99c-ce9f1e25583e
verified: false
validated: true
submitted: true
---
# estk-list-indexes

## Command

```bash
estk --url=https://elasticsearch.example.com:9200 list
```

## Description

Lists all available Elasticsearch indexes, including document counts and sizes, to verify unauthenticated access and map data stores.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | Specifies the target Elasticsearch URL (e.g., https://elasticsearch.example.com:9200) | Yes |
| `list` | Subcommand to retrieve index information | Yes |

## Examples

### Basic Usage

```bash
estk --url=https://elasticsearch.example.com:9200 list
```

### Advanced Usage

```bash
estk --url=https://elasticsearch.example.com:9200 list --verbose
```
(If verbose flag supported for more details)

## Expected Output

Detection logs followed by index summary: version confirmation, total indices, counts, and per-index details like "Found index aim_high with 2211 documents (5.9 MB)".

## Related

- [[Related Procedure: Enumerate-Elasticsearch-Indexes-with-estk]]
