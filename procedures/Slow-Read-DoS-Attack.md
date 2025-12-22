---
id: 5304dfa5-7882-428a-88ae-93b02d919e05
name: Slow-Read-DoS-Attack
type: procedure
verified: true
submitted: true
created_at: '2020-09-06T18:43:30.724513+00:00'
updated_at: '2023-05-26T18:22:09.037338+00:00'
tactics:
  - '[[Impact]]'
techniques:
  - '[[Network Denial of Service]]'
sub_techniques: []
tags:
  - DoS
  - Web Applications
commands:
  - '[[commands/install-slowhttptest-on-ubuntu]]'
  - '[[commands/slowhttptest-slow-read-dos]]'
platforms:
  - Web
tools:
  - '[[tools/slowhttptest]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Slow-Read-DoS-Attack

## Summary

The Slow Read DoS Attack is a denial-of-service technique that overwhelms a web server by establishing multiple connections and reading HTTP responses extremely slowly. Unlike Slowloris, which delays requests, this method sends legitimate requests but throttles the reading of responses, forcing the server to keep connections open and exhaust resources like sockets and memory. This procedure uses the slowhttptest tool to simulate the attack and verify vulnerability on a target web application.

## Description

Slow Read DoS exploits servers that do not properly manage connection timeouts or resource limits during response transmission. By slowly consuming response data, the attacker ties up server threads, preventing legitimate users from accessing the service. This is particularly effective against Apache or similar servers without protections like mod_reqtimeout or rate limiting. The attack requires network access to the target URL and can be detected through unusual connection patterns. Prerequisites include a Linux environment for running the tool and ethical testing permissions to avoid real disruptions.

## Requirements

1. Linux system (e.g., Ubuntu or Kali) with sudo access for installation.
2. Network connectivity to the target web server.
3. Installed slowhttptest tool ([[tools/slowhttptest]]).
4. Basic understanding of HTTP and DoS concepts; no special credentials needed beyond network reachability.

## Defense

Defensive measures include implementing connection timeouts, rate limiting at the application or proxy level (e.g., using NGINX limit_req or Apache mod_evasive), and monitoring for slow response consumption via tools like fail2ban or intrusion detection systems. Enable TCP keep-alives and resource quotas to mitigate resource exhaustion.

## Objectives

1. Establish multiple connections to the target server while slowly reading responses to exhaust server resources.
2. Verify the attack's effectiveness by observing service degradation.
3. Simulate real-world DoS conditions for vulnerability assessment and training.

## Instructions

### Step 1: Install SlowHTTPTest Tool

**Context**: Begin by installing the slowhttptest tool, which is essential for executing Slow Read DoS attacks. This ensures you have the necessary software to probe the target without relying on pre-installed tools.

**Command** ([[commands/install-slowhttptest-on-ubuntu]]):
```bash
sudo apt-get install slowhttptest
```

> This command fetches and installs slowhttptest from the package repository. Run it on a Debian-based system like Ubuntu. Expected output includes package download progress and a success message like "slowhttptest is already the newest version" or installation completion without errors.

### Step 2: Execute Slow Read DoS Test

**Context**: With the tool installed, launch the Slow Read mode against the target URL. This step opens numerous connections, sends valid GET requests, and reads responses at a throttled pace (e.g., 24 bytes per interval), aiming to hang the server if unprotected.

**Command** ([[commands/slowhttptest-slow-read-dos]]):
```bash
slowhttptest -c $_CONNECTIONS -H -g -o $_OUTPUT_FILE -i $_INTERVAL -r $_RATE -t $_VERB -u $_URL -x $_READ_INTERVAL -p $_PROBE_TIMEOUT
```

> Customize parameters based on the target: for example, use 500 connections (-c 500), GET verb (-t GET), and the target URL (-u http://example.com). The -x flag enables Slow Read mode. Monitor the output for connection status updates. If successful, the server will show signs of unavailability, such as timeouts for new requests.

### Step 3: Verify Attack Impact

**Context**: Confirm the DoS effect by attempting to access the target application in a browser or via curl. This step validates that the slow reading has indeed degraded service availability.

**Instructions**: Open a web browser and navigate to the target URL (e.g., http://yourwebsite-or-server-ip.com). Alternatively, use a simple curl command:
```bash
curl -I $_URL
```

> Expected behavior: The request hangs, times out, or returns errors like 503 Service Unavailable. If the site loads normally, increase connections (-c) or adjust intervals (-i, -x) and retry. Success is indicated by consistent delays or denials for legitimate requests.
