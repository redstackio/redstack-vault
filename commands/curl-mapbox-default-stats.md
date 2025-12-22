---
id: cmd-curl-mapbox-default
data: >-
  curl -H "Cookie: session=your_session_cookie"
  "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=day&period=1461766083142,1462370883143&metrics=countries,browsers,hosts,maps,version&services=mapview,tile,static,geocode,permanentgeocode,directions,surface&_=1462370883155"
  -o default_response.json
tags:
  - api
  - query
  - dos
type: command
output: JSON response ~2.5 KB with default metrics
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.042Z'
verified: false
validated: true
submitted: true
---
# curl-mapbox-default-stats

## Command

```bash
curl -H "Cookie: session=your_session_cookie" "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=day&period=1461766083142,1462370883143&metrics=countries,browsers,hosts,maps,version&services=mapview,tile,static,geocode,permanentgeocode,directions,surface&_=1462370883155" -o default_response.json
```

## Description

Queries the Mapbox statistics endpoint with default parameters to retrieve baseline user metrics data. Use this to verify access and measure normal response size before manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: ..."` | Auth session cookie | Yes |
| `yourusername` | Mapbox username | Yes |
| `period=...` | Unix timestamps for start/end (default short period) | Yes |
| `-o default_response.json` | Output file | No |

## Examples

### Basic Usage

```bash
curl -H "Cookie: session=abc123" "https://www.mapbox.com/core/statistics/v1/apokh11/account?interval=day&period=1461766083142,1462370883143&..." 
```

### With Output File

```bash
curl -H "Cookie: session=abc123" "https://..." -o response.json
```

## Expected Output

JSON object with metrics arrays for countries, browsers, etc., approximately 2.5 KB in size for the short period.

## Related

- [[commands/curl-mapbox-dos-params]]
- [[procedures/Query-Default-Statistics-Endpoint]]
