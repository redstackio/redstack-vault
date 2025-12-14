---
id: cmd-uuid-2
data: curl ipinfo.io/IP-address-of-victim
tags:
  - geolocation
  - recon
  - ssrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.259Z'
verified: false
validated: true
submitted: true
---
# curl-ip-geolocation-query

## Command

```bash
curl ipinfo.io/IP-address-of-victim
```

## Description

Queries the ipinfo.io API to retrieve geolocation and network details for a given IP address leaked via SSRF, aiding in victim tracing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ipinfo.io/IP-address-of-victim` | IP geolocation endpoint with target IP | Yes |

## Examples

### Basic Usage

```bash
curl ipinfo.io/192.0.2.1
```

### Advanced Usage

```bash
curl -s ipinfo.io/192.0.2.1 | jq '.city'
```

## Expected Output

{
  "ip": "192.0.2.1",
  "city": "Washington",
  "region": "District of Columbia",
  "country": "US",
  "loc": "38.8951,-77.0364",
  "org": "AS12345 Example ISP",
  "postal": "20001",
  "timezone": "America/New_York"
}

## Related

- [[Related Procedure: Analyze-Exfiltrated-Data-and-Trace-Victim-Location]]
