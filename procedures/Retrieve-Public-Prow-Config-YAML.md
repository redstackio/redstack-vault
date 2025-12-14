---
id: proc-uuid-placeholder
tags:
  - information-disclosure
  - kubernetes
  - prow
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-prow-config]]'
verified: false
platforms:
  - Kubernetes
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:12.551Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
---

# Retrieve Public Prow Config YAML

## Summary

This procedure accesses the publicly exposed configuration endpoint of the Kubernetes Prow system to retrieve a YAML file containing internal details, enabling reconnaissance of infrastructure, credential paths, and build configurations without any authentication.

## Description

The Kubernetes Prow system, used for continuous integration in Kubernetes projects, exposes its full configuration at https://prow.k8s.io/config. This endpoint returns a large YAML file with non-sensitive build information but includes potentially useful details for attackers, such as paths to credentials (e.g., Google, Jenkins, AWS), secret names, GitHub team IDs, node specifications (CPU, memory, disk sizes), cron jobs, and network configurations. Discovered via direct URL access, this lack of access controls allows anyone to download the config, which could inform targeted attacks on the infrastructure. The Kubernetes team deems the data non-sensitive, but it still aids in mapping the environment.

## Requirements

1. Internet connectivity to access public HTTPS endpoints
2. A tool or browser capable of HTTP GET requests (e.g., curl)
3. No credentials or special permissions required

## Defense

Defensive measures and detection strategies:

- Implement authentication or IP whitelisting on configuration endpoints
- Use robots.txt or access controls to restrict public YAML files
- Monitor access logs for repeated fetches of /config endpoints
- Regularly audit public endpoints for sensitive data exposure

## Objectives

1. Gather internal configuration details from the Prow system
2. Identify potential entry points or weak spots in the Kubernetes infrastructure
3. Expose details like credential paths and system specs for further reconnaissance

## Instructions

### Step 1: Fetch the Configuration File

**Context**: Directly request the YAML configuration from the public endpoint to disclose internal details.

**Command** ([[commands/curl-fetch-prow-config]]):
```bash
curl https://prow.k8s.io/config
```

> This command performs a GET request to the endpoint and outputs the raw YAML. Successful execution returns a multi-section YAML with keys like 'plank', 'deck', 'hook', detailing components, presubmits, postsubmits, periods, and tide configurations. Look for sections revealing paths (e.g., /secrets/gcp/sa.json), hidden repos, and resource specs.

### Step 2: Parse and Analyze Output

**Context**: Review the retrieved YAML for actionable intelligence.

**Command** (No specific command; use text editor or YAML parser):

> Pipe the output to a file for analysis: `curl https://prow.k8s.io/config > prow-config.yaml`. Search for keywords like 'secret', 'credential', 'aws', 'github' to identify exposures.

> Expected output includes mappings to services like GitHub, Jenkins, AWS, and Google, with details on mounting points, usernames, and hashing algorithms.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-prow-config]]

## Tools Used


## Tags

- information-disclosure
- kubernetes
- prow
- yaml
- reconnaissance

---
