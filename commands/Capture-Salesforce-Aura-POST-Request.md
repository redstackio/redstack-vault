---
data: >-
  POST
  ███████?r=3&ui-comm-runtime-components-aura-components-siteforce-controller.PubliclyCacheableAttributeLoader.getComponentAttributes=1
  HTTP/1.1

  Host: ███

  Cookie: ███

  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/█████████
  Firefox/119.0

  Accept: */*

  Accept-Language: en-GB,en;q=0.5

  Accept-Encoding: gzip, deflate

  Referer: ██████████t=1703212778793

  X-Sfdc-Page-Scope-Id: ab32d6b8-b3fc-4612-8bc1-3b0c8163e8f0

  X-Sfdc-Request-Id: 251200000054548e63

  X-Sfdc-Page-Cache: 44256e663456d3d8

  Content-Type: application/x-www-form-urlencoded;charset=UTF-8

  Content-Length: 1336

  Origin: █████████

  Dnt: 1

  Sec-Fetch-Dest: empty

  Sec-Fetch-Mode: cors

  Sec-Fetch-Site: same-origin

  Te: trailers

  Connection: close


  message=%7B%22actions%22%3A%5B%7B%22id%22%3A%2283%3Ba%22%2C%22descriptor%22%3A%22serviceComponent%3A%2F%2Fui.comm.runtime.components.aura.components.siteforce.controller.PubliclyCacheableAttributeLoaderController%2FACTION%24getComponentAttributes%22%2C%22callingDescriptor%22%3A%22markup%3A%2F%2Fsiteforce%3ApageLoader%22%2C%22params%22%3A%7B%22viewOrThemeLayoutId%22%3A%228c568ef8-3954-4997-930c-542a81f9e8eb%22%2C%22publishedChangelistNum%22%3A61%2C%22audienceKey%22%3A%22cp38y0onxM9f4QchAW2Mkg%22%7D%2C%22version%22%3A%2259.0%22%2C%22storable%22%3Atrue%7D%5D%7D&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%22Q0FGdjJNU2hrWnJiekVjWXdRVlJ4d08ySzBfZjVsY04wOG9fYlRpVWRXUEEyNDYuMTUuNS0zLjAuNA%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AcommunityApp%22%3A%22xUUH_isHmNQqCOJ9yNTV7A%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Afalse%7D&aura.pageURI=%2F████%2Fs%2F%3Ft%3D1703212778793&aura.token=█████..█████████
tags:
  - http-request
  - aura-capture
type: command
output: null
executor: http
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.146Z'
id: 7963da3d-c01b-48ff-9226-561e20e4619b
verified: false
validated: true
submitted: true
---
# Capture-Salesforce-Aura-POST-Request

## Command

```http
POST ███████?r=3&ui-comm-runtime-components-aura-components-siteforce-controller.PubliclyCacheableAttributeLoader.getComponentAttributes=1 HTTP/1.1
Host: ███
Cookie: ███
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/█████████ Firefox/119.0
Accept: */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: ██████████t=1703212778793
X-Sfdc-Page-Scope-Id: ab32d6b8-b3fc-4612-8bc1-3b0c8163e8f0
X-Sfdc-Request-Id: 251200000054548e63
X-Sfdc-Page-Cache: 44256e663456d3d8
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Content-Length: 1336
Origin: █████████
Dnt: 1
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

message=%7B%22actions%22%3A%5B%7B%22id%22%3A%2283%3Ba%22%2C%22descriptor%22%3A%22serviceComponent%3A%2F%2Fui.comm.runtime.components.aura.components.siteforce.controller.PubliclyCacheableAttributeLoaderController%2FACTION%24getComponentAttributes%22%2C%22callingDescriptor%22%3A%22markup%3A%2F%2Fsiteforce%3ApageLoader%22%2C%22params%22%3A%7B%22viewOrThemeLayoutId%22%3A%228c568ef8-3954-4997-930c-542a81f9e8eb%22%2C%22publishedChangelistNum%22%3A61%2C%22audienceKey%22%3A%22cp38y0onxM9f4QchAW2Mkg%22%7D%2C%22version%22%3A%2259.0%22%2C%22storable%22%3Atrue%7D%5D%7D&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%22Q0FGdjJNU2hrWnJiekVjWXdRVlJ4d08ySzBfZjVsY04wOG9fYlRpVWRXUEEyNDYuMTUuNS0zLjAuNA%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AcommunityApp%22%3A%22xUUH_isHmNQqCOJ9yNTV7A%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Afalse%7D&aura.pageURI=%2F████%2Fs%2F%3Ft%3D1703212778793&aura.token=█████..█████████
```

## Description

This HTTP POST request captures a legitimate Salesforce Aura interaction for loading component attributes, providing the baseline structure, token, and context needed for modification in exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| message | URL-encoded JSON with actions array for getComponentAttributes, including viewOrThemeLayoutId, publishedChangelistNum, audienceKey | Yes |
| aura.context | URL-encoded JSON for production mode, fwuid, app details | Yes |
| aura.pageURI | Encoded URI of the current page | Yes |
| aura.token | Session authentication token | Yes |

## Examples

### Basic Usage

Intercept via proxy tool like Burp Suite while performing a page load in the authenticated portal.

### Advanced Usage

Replay in Repeater after capturing to test token validity.

## Expected Output

200 OK response with JSON containing up to 2000 records, aura.token validation, and sequential Salesforce IDs in the data.

## Related

- [[commands/Exploit-getItems-for-Contact-Records]]
