---
data: >-
  curl -G "http://velodrome.k8s.io/api/datasources/proxy/4/query"
  --data-urlencode "db=metrics" --data-urlencode "q=SELECT
  1-(sum(\"consistent_builds\")/sum(\"builds\")) FROM \"flakes_daily\" WHERE
  time > now() - 30d AND \"job\" =~
  /\^(pr:pull-kubernetes-kubemark-e2e-gce-big|pr:pull-kubernetes-bazel-build|pr:pull-kubernetes-bazel-test|pr:pull-kubernetes-dependencies|pr:pull-kubernetes-e2e-gce|pr:pull-kubernetes-e2e-gce-100-performance|pr:pull-kubernetes-e2e-kind|pr:pull-kubernetes-integration|pr:pull-kubernetes-node-e2e|pr:pull-kubernetes-typecheck|pr:pull-kubernetes-verify)$/
  group by job, time(20m) fill(none)" --data-urlencode "epoch=ms"
tags:
  - influxql
  - metrics
  - proxy
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.890Z'
id: 5b617fef-4a1f-4f74-9dff-50b7ada06f97
verified: false
validated: true
submitted: true
---
# influxql-flake-rate-query

## Command

```bash
curl -G "http://velodrome.k8s.io/api/datasources/proxy/4/query" \
  --data-urlencode "db=metrics" \
  --data-urlencode "q=SELECT 1-(sum(\"consistent_builds\")/sum(\"builds\")) FROM \"flakes_daily\" WHERE time > now() - 30d AND \"job\" =~ /\^(pr:pull-kubernetes-kubemark-e2e-gce-big|pr:pull-kubernetes-bazel-build|pr:pull-kubernetes-bazel-test|pr:pull-kubernetes-dependencies|pr:pull-kubernetes-e2e-gce|pr:pull-kubernetes-e2e-gce-100-performance|pr:pull-kubernetes-e2e-kind|pr:pull-kubernetes-integration|pr:pull-kubernetes-node-e2e|pr:pull-kubernetes-typecheck|pr:pull-kubernetes-verify)$/ group by job, time(20m) fill(none)" \
  --data-urlencode "epoch=ms"
```

## Description

This command sends an InfluxQL query via Grafana's proxy to calculate the flake rate (inconsistent builds) for specific Kubernetes CI jobs over the last 30 days, grouped by job and 20-minute intervals. Used to demonstrate proxy access and basic query execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data-urlencode db=metrics` | Specifies the InfluxDB database | Yes |
| `--data-urlencode q=...` | The InfluxQL SELECT query string | Yes |
| `--data-urlencode epoch=ms` | Output timestamps in milliseconds | No |

## Examples

### Basic Usage

```bash
curl -G "http://velodrome.k8s.io/api/datasources/proxy/4/query" --data-urlencode "db=metrics" --data-urlencode "q=SELECT 1-(sum(\"consistent_builds\")/sum(\"builds\")) FROM \"flakes_daily\" WHERE time > now() - 30d AND \"job\" =~ /\^(pr:pull-kubernetes-kubemark-e2e-gce-big)$/ group by job, time(20m) fill(none)" --data-urlencode "epoch=ms"
```

### Advanced Usage

Modify the regex in q for different job filters.

```bash
# As above, but with full job list
curl ... (full query)
```

## Expected Output

JSON response with an array of results containing time, job, and flake rate values, e.g., {"results":[{"series":[{"name":"","columns":["time","job","mean"],"values":[[timestamp,"job_name",0.05]]}]}]}

## Related

- [[commands/influxdb-show-databases]]
