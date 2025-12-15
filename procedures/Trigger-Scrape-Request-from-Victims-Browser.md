---
id: proc-trigger-scrape-request-187520
tags:
  - csrf
  - scrape
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/monitor-wordpress-scrape]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.706Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Scrape-Request-from-Victims-Browser

## Summary

This procedure describes how the CSRF request causes the WordPress server to fetch (scrape) content from the attacker's domain, setting the stage for the SSRF redirect.

## Description

Once the forged request hits wp-admin/press-this.php, WordPress processes it under the victim's session and issues an HTTP GET to the u= parameter URL (attacker.com). This lacks proper validation, allowing the attacker to control the response. The scrape is internal to the server, bypassing client-side restrictions. Expected outcome: Server contacts attacker domain, ready for redirect injection.

## Requirements

1. Successful CSRF delivery from previous step
2. Access to WordPress access logs or network monitoring
3. Attacker domain resolving publicly

## Defense

Defensive measures and detection strategies:

- Rate-limit Press This requests per session
- Log and alert on scrapes to external domains
- Disable Press This if unused

## Objectives

1. Force server-side HTTP request to attacker-controlled URL
2. Confirm CSRF success via scrape initiation
3. Prepare for SSRF payload delivery

## Instructions

### Step 1: Observe CSRF Processing

**Context**: Monitor for the incoming CSRF and subsequent scrape.

**Command** ([[commands/monitor-wordpress-scrape]]):
```bash
tail -f /var/log/apache2/access.log | grep "press-this.php"
```

> Watches for the CSRF hit; follow with grep for outgoing to attacker.com. Expected output: Log entries showing GET to press-this.php and then to u= URL.

### Step 2: Verify Scrape Request

**Context**: Ensure the server fetches from attacker domain.

**Command** ([[commands/log-external-fetch]]):
```bash
# On attacker server: tcpdump -i any port 80 -w scrape.pcap
# Or use access.log on attacker side
grep "GET / HTTP/1.1" /var/log/attacker/access.log
```

> Captures the incoming scrape. Expected output: Request from WordPress IP with User-Agent: Press This.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/monitor-wordpress-scrape]]
- [[commands/log-external-fetch]]

## Tools Used

- None

## Tags

- [[csrf]]
- [[scrape]]
