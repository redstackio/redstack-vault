---
id: 123e4567-e89b-12d3-a456-426614174002
data: >-
  curl -X GET
  "https://api.mapbox.com/styles/v1/katilthe?access_token=pk.eyJ1Ijoia2F0aWx0aGUiLCJhIjoiY2lsbWJwcWpjNjhmNnZubWNhYXdwZm5obyJ9.2cPnaIiXcFnDRFMfrD1TRw"
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:44.0) Gecko/20100101
  Firefox/44.0" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Referer:
  https://www.mapbox.com/studio/styles/fonts/" -H "Accept-Language:
  en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br" -H "Origin:
  https://www.mapbox.com" --connect-timeout 10
tags:
  - api
  - recon
  - mapbox
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-04T00:00:00Z'
updated_at: '2025-12-14T17:32:10.133Z'
verified: false
validated: true
submitted: true
---
# get-mapbox-public-styles

## Command

```bash
curl -X GET "https://api.mapbox.com/styles/v1/katilthe?access_token=pk.eyJ1Ijoia2F0aWx0aGUiLCJhIjoiY2lsbWJwcWpjNjhmNnZubWNhYXdwZm5obyJ9.2cPnaIiXcFnDRFMfrD1TRw" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Referer: https://www.mapbox.com/studio/styles/fonts/" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Accept-Encoding: gzip, deflate, br" \
  -H "Origin: https://www.mapbox.com" \
  --connect-timeout 10
```

## Description

This curl command sends a GET request to the Mapbox API's styles endpoint to retrieve public map styles for a specified username using an access token. It is used to test implicit scope access in no-scope tokens, confirming unauthorized read permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `username` (in URL path) | Target Mapbox username, e.g., 'katilthe' | Yes |
| `access_token` (query param) | Mapbox API token with implicit public scopes | Yes |
| `-H "User-Agent: ..."` | Mimics browser user agent to avoid detection | No |
| `-H "Accept: ..."` | Specifies accepted content types | No |
| `-H "Referer: ..."` | Sets referer header for context | No |
| `--connect-timeout 10` | Limits connection time to 10 seconds | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.mapbox.com/styles/v1/exampleuser?access_token=pk.exampletoken" -H "User-Agent: curl/7.0"
```

### Advanced Usage

```bash
curl -X GET "https://api.mapbox.com/styles/v1/katilthe?access_token=pk.eyJ1Ijoia2F0aWx0aGUiLCJhIjoiY2lsbWJwcWpjNjhmNnZubWNhYXdwZm5obyJ9.2cPnaIiXcFnDRFMfrD1TRw" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Referer: https://www.mapbox.com/studio/styles/fonts/" \
  --silent --output styles.json
```

## Expected Output

HTTP 200 OK response with a JSON array of style objects, e.g., [{'version':8,'name':'test\'><svg/onload=alert(2)>-copy-copy','center':[-78.90145050000001,33.70101199999998],'zoom':12,'bearing':0,'pitch':0,'created':'2016-03-10T13:45:51.193Z','id':'cilmbusls00cvc6m23qpi69gg','modified':'2016-03-10T13:45:51.193Z','owner':'katilthe'}]. If access is denied, expect 401 Unauthorized.

## Related

- [[procedures/Retrieve-Public-Styles-with-Implicit-Token]]
