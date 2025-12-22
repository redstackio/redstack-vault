---
id: 1420675d-0263-4f2f-9a8e-cdbd0407e5e0
name: Brute Force Virtual Host Domains (Wfuzz)
type: procedure
verified: true
submitted: true
created_at: '2019-10-17T21:12:56.080002+00:00'
updated_at: '2023-05-26T01:15:16.104150+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - brute-force
  - web-applications
commands:
  - '[[commands/wfuzz-brute-force-virtual-hosts]]'
platforms:
  - Web
tools:
  - '[[tools/Wfuzz]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Brute Force Virtual Hosts with Wfuzz

## Summary

This procedure uses the Wfuzz tool to brute force potential virtual host names on a target web server by fuzzing the HTTP Host header with entries from a wordlist. It helps discover hidden websites or subdomains served on the same IP address, expanding the attack surface during reconnaissance.

## Description

Many web servers use virtual hosting to serve multiple domains from a single IP address, differentiating based on the Host header in incoming HTTP requests. This procedure automates the enumeration of such virtual hosts by sending crafted requests where the Host header is replaced with guessed names (e.g., admin.example.com, api.example.com) from a wordlist. It filters out common 404 errors to focus on valid responses like 200 OK or 403 Forbidden, which may indicate discoverable hosts. This technique is useful in web penetration testing to map the full scope of a target's web presence without relying on DNS resolution alone.

## Requirements

1. A wordlist file containing potential virtual host or subdomain names (e.g., common.txt from SecLists or dirbuster lists).
2. Network connectivity to the target web server's IP address (typically over HTTP/HTTPS on port 80/443).
3. The base domain name of the target (e.g., example.com) to append to fuzzing payloads.
4. Wfuzz tool installed on the attacker's machine.
5. Basic understanding of HTTP headers and response codes.

## Defense

Defensive measures and detection strategies:

- Implement a Web Application Firewall (WAF) to detect and block rapid requests with varying Host headers, such as those from fuzzing tools.
- Enable rate limiting on the web server to throttle suspicious request volumes from a single IP.
- Monitor server logs for anomalous Host header values that do not match known domains and alert on patterns indicative of brute forcing (e.g., high-frequency unique hosts).
- Use certificate transparency logs or DNS monitoring to track legitimate virtual hosts and flag undiscovered ones.

## Objectives

1. Identify hidden virtual hosts served on the target IP to uncover additional web applications or entry points.
2. Gather intelligence on the target's web infrastructure without alerting DNS-based defenses.
3. Validate discovered hosts for further exploitation, such as directory brute forcing or vulnerability scanning.
4. Expected outcome: A list of valid virtual hosts that respond differently from 404 errors.

## Instructions

### Step 1: Prepare the Environment and Wordlist

**Context**: Ensure Wfuzz is installed and select an appropriate wordlist. This step sets up the necessary files and verifies tool availability to avoid runtime errors.

First, confirm Wfuzz is available by running a help command:

```bash
wfuzz -h
```

> This displays Wfuzz options; if not found, install via your package manager (see [[tools/Wfuzz]] for details). Choose a wordlist like /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt, which contains common subdomain names. If needed, customize the wordlist to include target-specific terms (e.g., add 'admin', 'dev', 'staging').

### Step 2: Execute the Virtual Host Brute Force

**Context**: Launch Wfuzz to send HTTP requests to the target IP, fuzzing the Host header with wordlist entries. This simulates legitimate requests to various subdomains while hiding noise from non-existent paths.

**Command** ([[commands/wfuzz-brute-force-virtual-hosts]]):

```bash
wfuzz --hc 404 -c -w $_WORDLIST -u http://$_TARGET_IP -H 'Host: FUZZ.$_DOMAIN'
```

> Replace $_WORDLIST with the path to your wordlist, $_TARGET_IP with the server's IP (e.g., 10.10.10.10), and $_DOMAIN with the base domain (e.g., example.com). The --hc 404 flag filters out 404 responses, -c enables counters for progress tracking, -u sets the base URL, and -H adds the custom Host header. Run this from a Kali Linux terminal or similar environment. If the target uses HTTPS, change http to https and consider adding --ss for SSL support if needed.

Decision point: If the target returns many false positives (e.g., due to custom error pages mimicking 200), adjust --hc to include additional status codes like --hc 404,403 or use --hh for header-based filtering.

### Step 3: Analyze and Verify Results

**Context**: Review Wfuzz output for valid responses and manually verify discovered hosts to confirm they are active virtual hosts rather than artifacts.

Parse the output for lines showing status codes other than 404 (e.g., C=200 or C=403). For each potential hit, test manually using curl:

```bash
curl -H 'Host: discovered-subdomain.$_DOMAIN' http://$_TARGET_IP
```

> This sends a simple request to the discovered host; look for unique content like different page titles or server responses. Document valid hosts in a file for further procedures, such as [[procedures/brute-force-directories-with-gobuster]]. If no hits, try a larger wordlist or check if the server requires specific paths (e.g., add / to the URL).

Expected outcome: A refined list of virtual hosts with their response details for mapping the target's web footprint.
