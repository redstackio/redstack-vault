---
id: uuid-placeholder-proc2
tags:
  - shodan
  - scanning
  - kubernetes
  - recon
type: procedure
tools:
  - '[[tools/Shodan]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
  - Kubernetes
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:12.510Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
---

# Shodan Search for Exposed Kubernetes Endpoints

## Summary

This procedure uses Shodan, a search engine for internet-connected devices, to identify exposed Kubernetes-related endpoints, such as those serving sensitive JSON data on open ports.

## Description

Shodan indexes public internet services, allowing attackers to discover misconfigurations like open ports in Kubernetes clusters. In this scenario, searching for Kubernetes-specific terms or ports (e.g., 9001) reveals endpoints like http://104.154.232.252:9001/, which expose raw JSON with potential sensitive information. The procedure targets cloud-hosted Kubernetes services and assumes no prior access, focusing on passive reconnaissance to avoid direct interaction until verification.

## Requirements

1. Shodan account (free tier sufficient for basic searches)
2. Internet access
3. Basic understanding of search queries (e.g., port, service names)

## Defense

Defensive measures and detection strategies:

- Restrict services to private networks or use firewalls to block public exposure
- Monitor Shodan indexes and remove exposed assets via provider tools (e.g., GCP security)
- Implement rate limiting and logging on exposed ports to detect scans

## Objectives

1. Discover publicly indexed Kubernetes endpoints
2. Verify exposure of sensitive data like JSON configs
3. Expand reconnaissance beyond manual methods

## Instructions

### Step 1: Perform Shodan Search

**Context**: Log into Shodan and craft a query to find Kubernetes exposures, such as open ports or service banners.

**Command** (Shodan CLI or web search):
```bash
# Example Shodan CLI search (requires API key)
shodan search "port:9001 kubernetes"
```

> Use the web interface if no CLI: search for "port:9001 kubernetes json". Expected output: List of IPs and ports, e.g., 104.154.232.252:9001.

### Step 2: Verify Exposed Endpoint

**Context**: Access the discovered endpoint to confirm data exposure.

**Command** ([[commands/curl-access-url]]):
```bash
curl http://104.154.232.252:9001/
```

> This fetches the raw JSON. Expected output: JSON data related to Kubernetes, potentially containing sensitive details.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used

- [[tools/Shodan]]

## Tags

- [[tools/Shodan]]
- [[scanning]]
- [[kubernetes]]
- [[recon]]
