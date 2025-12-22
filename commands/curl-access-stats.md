---
data: 'curl https://influxdb.quality.gitlab.net/stats.json'
tags:
  - recon
  - http
  - json
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.172Z'
id: 5c6ea84a-4533-43d1-9a22-de2055f4553a
verified: false
validated: true
submitted: true
---
# curl-access-stats

## Command

```bash
curl https://influxdb.quality.gitlab.net/stats.json
```

## Description

Fetches InfluxDB stats in JSON format.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
curl https://influxdb.quality.gitlab.net/stats.json
```

### Advanced Usage

```bash
curl https://influxdb.quality.gitlab.net/stats.json | jq .
```

## Expected Output

JSON like {"stats": {"numDatabases": 1}}.

## Related

- [[Related Procedure: Access-Stats-Endpoint]]
