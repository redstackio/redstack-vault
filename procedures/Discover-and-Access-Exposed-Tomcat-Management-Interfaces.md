---
tags:
  - tomcat
  - misconfiguration
  - authentication-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-tomcat-endpoints]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: a9eb929f-31c9-4615-89ca-530e06230079
created_at: '2025-12-14T17:31:19.725Z'
updated_at: '2025-12-14T17:31:19.725Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover-and-Access-Exposed-Tomcat-Management-Interfaces

## Summary

This procedure outlines how to identify and exploit a misconfiguration in Apache Tomcat where the /admin and /manager endpoints are accessible without authentication, enabling unauthorized control over server deployment, management, and configuration.

## Description

Apache Tomcat, a popular Java-based web server, includes built-in web applications for administration (/admin) and HTML manager (/manager). By default, these should be secured with authentication or removed in production. A common misconfiguration leaves them exposed to the public internet or internal networks without protections, allowing attackers to perform actions like deploying malicious WAR files, viewing server status, or modifying configurations. In this scenario, the vulnerability was found on a single host in a pilot environment, reported via HackerOne, and fixed by restricting access. The procedure assumes network reachability to the target and focuses on passive discovery followed by direct access.

## Requirements

1. Network access to the Tomcat host (e.g., via HTTP on port 8080)
2. Basic web reconnaissance tools like curl or a browser
3. Knowledge of common Tomcat paths (/admin, /manager)

## Defense

Defensive measures and detection strategies:

- Enable authentication (e.g., via tomcat-users.xml) or remove manager/admin apps entirely
- Use IP whitelisting or reverse proxies (e.g., Apache HTTPD with mod_proxy) to restrict access
- Monitor access logs for requests to /admin or /manager from unauthorized IPs
- Deploy WAF rules to block unauthenticated admin endpoint access

## Objectives

1. Confirm exposure of Tomcat management interfaces
2. Gain unauthorized entry to perform administrative actions
3. Demonstrate potential for server takeover or data exfiltration

## Instructions

### Step 1: Probe for Exposed Endpoints

**Context**: Use HTTP requests to check if /admin and /manager are accessible without authentication challenges.

**Command** ([[commands/curl-check-tomcat-endpoints]]):
```bash
curl -s -I http://target-host:8080/admin
```

> This HEAD request checks the response headers. A 200 OK without WWW-Authenticate indicates exposure. Expected output includes HTTP/1.1 200 OK and content-type related to HTML or Tomcat resources.

### Step 2: Access the Management Interface

**Context**: If exposed, directly interact with the endpoint to verify full access.

**Command** ([[commands/curl-check-tomcat-endpoints]]):
```bash
curl -s http://target-host:8080/manager/html
```

> Retrieves the HTML manager page. Successful output shows a dashboard for deploying apps or viewing sessions, confirming unauthorized access. Use a browser for interactive use, where no login is prompted.

### Step 3: Validate Administrative Capabilities

**Context**: Test basic admin functions to assess impact.

**Instructions**: In the browser, navigate to the endpoint and attempt to view server status or list applications. No further commands needed; observe if deployment options are available.

> Expected output: Interactive forms for WAR uploads or config changes without auth prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-tomcat-endpoints]]

## Tools Used


## Tags

- tomcat
- misconfiguration
- authentication-bypass
