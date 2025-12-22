---
data: >-
  curl -G "http://velodrome.k8s.io/api/datasources/proxy/4/query"
  --data-urlencode "db=metrics" --data-urlencode "q=SHOW DATABASES"
tags:
  - influxql
  - discovery
  - admin
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.889Z'
id: 0445bbc9-166d-476e-ac87-a27897debd35
verified: false
validated: true
submitted: true
---
# influxdb-show-databases

## Command

```bash
curl -G "http://velodrome.k8s.io/api/datasources/proxy/4/query" \
  --data-urlencode "db=metrics" \
  --data-urlencode "q=SHOW DATABASES"
```

## Description

This command executes an InfluxQL SHOW DATABASES query via the Grafana proxy to list all available databases in the InfluxDB instance, confirming admin privileges if internal databases are visible.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data-urlencode db=metrics` | Target database for proxy context | Yes |
| `--data-urlencode q=SHOW DATABASES` | The InfluxQL command | Yes |

## Examples

### Basic Usage

```bash
curl -G "http://velodrome.k8s.io/api/datasources/proxy/4/query" --data-urlencode "db=metrics" --data-urlencode "q=SHOW DATABASES"
```

### Advanced Usage

N/A; simple command.

## Expected Output

JSON response listing databases, e.g., {"results":[{"series":[{"name":"databases","columns":["name"],"values":[["metrics"],["internal"]]}]}]. Admin access shows all; read-only may limit to one.

## Related

- [[commands/influxql-flake-rate-query]]
