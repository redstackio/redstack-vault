---
id: 123e4567-e89b-12d3-a456-426614174001
tags:
  - api-token
  - information-disclosure
  - mapbox
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/get-mapbox-public-styles]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:10.138Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Retrieve-Public-Styles-with-Implicit-Token

## Summary

This procedure uses a Mapbox API token created with no explicit scopes to send a GET request to the /styles/v1/{username} endpoint, exploiting implicit public scopes to retrieve and disclose public map styles data without authorization.

## Description

The Mapbox API allows tokens with implicit public scopes to read styles, tiles, and fonts even if no scopes are selected during creation. By targeting the styles endpoint with such a token, an attacker can fetch JSON data containing public style configurations, including names, centers, zooms, and IDs, potentially exposing sensitive resource details. This targets web-based API interactions and requires only the token and target username. Prerequisites include the token from the creation procedure; outcomes include successful data retrieval confirming the vulnerability.

## Requirements

1. Mapbox public API token with implicit scopes
2. Target username (e.g., from public profiles)
3. curl or equivalent HTTP client
4. Network access to api.mapbox.com

## Defense

Defensive measures and detection strategies:

- Revoke or scope tokens properly to prevent implicit access
- Implement rate limiting on public read endpoints
- Log and alert on read requests from no-scope tokens
- Validate token scopes server-side before granting access

## Objectives

1. Exploit implicit scopes for unauthorized read access
2. Retrieve public styles data
3. Demonstrate information disclosure

## Instructions

### Step 1: Prepare the API Request

**Context**: Set up the GET request with the token and target endpoint to test implicit access.

**Instructions**: Identify the target username (e.g., 'katilthe') and construct the URL: https://api.mapbox.com/styles/v1/{username}?access_token={token}.

> No command; preparation step. Expected: Valid URL formed.

### Step 2: Execute the GET Request

**Context**: Send the request mimicking browser headers to retrieve styles data.

**Command** ([[commands/get-mapbox-public-styles]]):
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

> This command queries the endpoint; successful output is 200 OK with JSON array of styles, e.g., [{'version':8,'name':'test\'><svg/onload=alert(2)>-copy-copy','center':[-78.90145050000001,33.70101199999998],'zoom':12,'bearing':0,'pitch':0,'created':'2016-03-10T13:45:51.193Z','id':'cilmbusls00cvc6m23qpi69gg','modified':'2016-03-10T13:45:51.193Z','owner':'katilthe'}].

### Step 3: Analyze Response for Disclosure

**Context**: Review the JSON to confirm access and identify exposed data.

**Instructions**: Pipe the output to jq for parsing: curl ... | jq 'length' to count styles, or jq '.[0]' for details.

> Expected: Confirmation of data access, highlighting unintended exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/get-mapbox-public-styles]]

## Tools Used


## Tags

- api-token
- information-disclosure
