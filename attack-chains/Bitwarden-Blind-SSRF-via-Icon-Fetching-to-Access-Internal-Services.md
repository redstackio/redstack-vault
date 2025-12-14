---
tags:
  - ssrf
  - bitwarden
  - internal-access
  - dns-bypass
  - cloud-metadata
type: attack_chain
tools:
  - '[[tools/FakeDns]]'
  - '[[tools/Nginx]]'
  - '[[tools/PHP]]'
  - '[[tools/Perl]]'
  - '[[tools/Docker]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Docker
  - Cloud
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Acquire-Domain-and-Setup-Public-Server]]'
  - '[[procedures/Install-and-Configure-Nginx-Webserver]]'
  - '[[procedures/Setup-FakeDns-with-Malicious-Records]]'
  - '[[procedures/Create-PHP-Redirect-Script]]'
  - '[[procedures/Install-Self-Hosted-Bitwarden-with-Docker]]'
  - '[[procedures/Setup-Perl-TCP-Listener-in-Container]]'
  - '[[procedures/Add-Credential-in-Bitwarden-to-Trigger-Fetch]]'
  - '[[procedures/Observe-SSRF-Request-on-Listener]]'
step_count: 8
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:08:55.276Z'
description: >-
  Demonstrates exploitation of a blind HTTP GET SSRF vulnerability in
  Bitwarden's icon fetching feature to access internal hosts like localhost and
  cloud metadata services.
skill_level: intermediate
impact_level: high
id: 2c13d394-461c-4d05-93dc-9a93429aad11
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Service Scanning]]'
---
# Bitwarden Blind SSRF via Icon Fetching to Access Internal Services

Multi-stage attack chain demonstrating exploitation of a blind HTTP GET SSRF in Bitwarden's website icon fetching feature, bypassing private IP checks to access internal services like localhost (via 0.0.0.0) and AWS metadata (169.254.0.0/16).

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 8 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Acquire Domain & Setup DNS] --> B[Configure Webserver Redirect]
    B --> C[Deploy Bitwarden Instance]
    C --> D[Setup Internal Listener]
    D --> E[Trigger Icon Fetch]
    E --> F[Observe Internal Request]
    F --> G[Scan Internal Network or Access Metadata]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/FakeDns]]
- [[tools/Nginx]]
- [[tools/PHP]]
- [[tools/Perl]]
- [[tools/Docker]]

### Target Environment

- Self-hosted Bitwarden instance (Docker-based)
- Required services/ports: Port 80 open internally
- Network access: Control over a public domain and DNS

### Initial Access Requirements

- No prior credentials needed; user adds a credential to trigger the fetch
- Attacker controls a domain for DNS manipulation
- Access to a server with public IP

## Detailed Attack Procedures

### Step 1: Acquire Domain and Setup Public Server
procedure: [[procedures/Acquire-Domain-and-Setup-Public-Server]]

**Objective**: Obtain a domain to control DNS resolutions and host a redirect server for initial icon fetch.

**Instructions**: Purchase a domain (e.g., yourdomain.com) from a registrar and configure its nameservers to point to your public server IP. Set up a basic server environment to host the webserver.

**Expected Output**: Domain resolves to your public IP (verify with `nslookup www.yourdomain.com`).

**Success Indicators**:
- Domain acquired and DNS pointed to public IP
- Server accessible via HTTP on port 80

### Step 2: Install and Configure Nginx Webserver
procedure: [[procedures/Install-and-Configure-Nginx-Webserver]]

**Objective**: Deploy a webserver to serve the initial icon request and redirect to internal targets.

**Instructions**: Install Nginx on the public server using package manager (e.g., `apt install nginx` on Ubuntu). Configure a virtual host for www.yourdomain.com to serve the PHP redirect script.

**Expected Output**: Nginx running and responding to HTTP requests on the public IP.

**Success Indicators**:
- Webserver logs show access to root path
- PHP scripts executable

### Step 3: Setup FakeDns with Malicious Records
procedure: [[procedures/Setup-FakeDns-with-Malicious-Records]]

**Objective**: Configure a fake DNS server to resolve public subdomain to external IP and internal subdomains to localhost (0.0.0.0).

**Instructions**: Install [[tools/FakeDns]] and add records using [[commands/fakedns-a-record-www]] and [[commands/fakedns-a-record-local]]:

```bash
A www.yourdomain.com YOUR.PUBLIC.IP
A *.local.yourdomain.com 0.0.0.0
```

**Expected Output**: DNS queries for www.yourdomain.com resolve to public IP; test.local.yourdomain.com resolves to 0.0.0.0.

**Success Indicators**:
- Resolutions confirmed via DNS tools
- No leakage of internal IPs

### Step 4: Create PHP Redirect Script
procedure: [[procedures/Create-PHP-Redirect-Script]]

**Objective**: Implement an HTTP redirect on the public server to chain to internal paths via subdomain resolution.

**Instructions**: Create index.php in the web root with [[commands/php-http-redirect]]:

```php
<?php header("Location: http://test.local.yourdomain.com/PATH_IS_KEPT"); exit(); ?>
```
Configure Nginx to process PHP files.

**Expected Output**: Accessing http://www.yourdomain.com returns 302 redirect to http://test.local.yourdomain.com/PATH_IS_KEPT.

**Success Indicators**:
- Curl test shows redirect header
- Path preserved in redirect URL

### Step 5: Install Self-Hosted Bitwarden with Docker
procedure: [[procedures/Install-Self-Hosted-Bitwarden-with-Docker]]

**Objective**: Deploy a vulnerable Bitwarden instance to test the icon fetching SSRF.

**Instructions**: Follow official docs at https://bitwarden.com/help/article/install-on-premise/. Use Docker Compose to spin up services, including the icons service (core 1.35.1, web 2.15.1).

**Expected Output**: Bitwarden web UI accessible and account creation/login functional.

**Success Indicators**:
- Services running without errors
- Icons service logs show no initial issues

### Step 6: Setup Perl TCP Listener in Container
procedure: [[procedures/Setup-Perl-TCP-Listener-in-Container]]

**Objective**: Create a listener inside the Bitwarden icons container to capture SSRF requests to localhost:80.

**Instructions**: Exec into the icons Docker container and run [[commands/perl-tcp-listener-port80]]:

```bash
perl -MIO::Socket::INET -ne 'BEGIN{$l=IO::Socket::INET->new( LocalPort=>80,Proto=>"tcp",Listen=>5,ReuseAddr=>1); my $l=$l->accept(); while(<$l>){ print $_; }; close($l);}'
```

**Expected Output**: Listener bound to port 80, waiting for connections.

**Success Indicators**:
- No bind errors
- Port 80 open internally

### Step 7: Add Credential in Bitwarden to Trigger Fetch
procedure: [[procedures/Add-Credential-in-Bitwarden-to-Trigger-Fetch]]

**Objective**: Add a login credential with the malicious URL to initiate the icon fetch and SSRF chain.

**Instructions**: Log into Bitwarden UI, navigate to add a new login item, and set URL to http://www.yourdomain.com. Enable icon fetching if not default.

**Expected Output**: Credential saved; icons service fetches from the URL, following redirect.

**Success Indicators**:
- No errors in UI
- Bitwarden logs show fetch attempt

### Step 8: Observe SSRF Request on Listener
procedure: [[procedures/Observe-SSRF-Request-on-Listener]]

**Objective**: Verify the SSRF by capturing the internal HTTP request on the listener.

**Instructions**: Monitor the Perl listener output after triggering the fetch.

**Expected Output**: Incoming GET /PATH_IS_KEPT HTTP/1.1 request with Bitwarden headers, targeted at localhost.

**Success Indicators**:
- Request received on internal listener
- Confirms bypass of private IP checks

## Attack Chain Summary

### Key Achievements

1. Bypassed incomplete private IP validation in Bitwarden's IsInternal check
2. Accessed localhost via 0.0.0.0 resolution and HTTP redirects
3. Demonstrated potential for internal network scanning or AWS metadata exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Service Scanning]] Network Service Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

*Last updated: 2023-10-01T00:00:00Z*
