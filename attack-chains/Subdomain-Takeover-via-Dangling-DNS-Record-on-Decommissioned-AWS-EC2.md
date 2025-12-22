---
tags:
  - subdomain-takeover
  - dns
  - aws
  - ec2
  - elb
  - phishing
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-probe-http]]'
verified: false
platforms:
  - AWS
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Monitor-Subdomain-Responses-Over-Time]]'
  - '[[procedures/Probe-Subdomain-Accessibility]]'
  - '[[procedures/Confirm-AWS-ELB-Takeover]]'
step_count: 3
techniques:
  - '[[Hardware]]'
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T05:32:23.962Z'
description: >-
  Attack chain demonstrating discovery and confirmation of a subdomain takeover
  vulnerability where a dangling DNS record points to a repurposed AWS resource,
  enabling potential phishing or reputation damage.
skill_level: intermediate
impact_level: high
id: 713f4f6f-5d56-4869-9c20-65ba916900a6
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
  - '[[Vulnerability Scanning]]'
---
# Subdomain Takeover via Dangling DNS Record on Decommissioned AWS EC2

Multi-stage attack chain demonstrating a complete attack workflow for identifying and confirming a subdomain takeover vulnerability on a decommissioned AWS EC2 instance.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Monitor Subdomain Changes] --> B[Probe Accessibility]
    B --> C[Confirm ELB Takeover]
    C --> D[Potential Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Basic HTTP client like curl or web browser

### Target Environment

- AWS cloud platform
- DNS resolution for target subdomains
- Ports: 80, 443

### Initial Access Requirements

- Public internet access
- No credentials required
- Ability to monitor DNS over time

## Detailed Attack Procedures

### Step 1: Monitor Subdomain Changes
procedure: [[procedures/Monitor-Subdomain-Responses-Over-Time]]

**Objective**: Track changes in subdomain responses to identify potential decommissioning and repurposing of resources.

**Instructions**: Periodically query the subdomain using [[commands/curl-probe-http]] to record headers and body responses:

```bash
curl -i https://mk.prd.vine.co/
```

Compare responses over days, noting if port 443 transitions from closed to open.

**Expected Output**: Initial no-response or timeout, later HTTP responses with new server headers.

**Success Indicators**:
- Port 443 closed initially (no response)
- Subsequent open port with unexpected server headers

### Step 2: Probe Subdomain Accessibility
procedure: [[procedures/Probe-Subdomain-Accessibility]]

**Objective**: Verify if the subdomain is now resolving and responding to HTTP requests.

**Instructions**: Access the subdomain directly via HTTP using [[commands/curl-probe-http]]:

```bash
curl -i http://mk.prd.vine.co/
```

Observe the response status and headers.

**Expected Output**: HTTP/1.1 426 Upgrade Required with Server: awselb/2.0 header.

**Success Indicators**:
- HTTP response received
- Presence of AWS-specific server header

### Step 3: Confirm AWS ELB Takeover
procedure: [[procedures/Confirm-AWS-ELB-Takeover]]

**Objective**: Test for confirmation of AWS Elastic Load Balancer control by triggering error pages.

**Instructions**: Append a null byte or invalid path to the URL and query using [[commands/curl-probe-http]]:

```bash
curl -i http://mk.prd.vine.co/%00
```

Analyze the error response for AWS ELB indicators.

**Expected Output**: HTTP/1.1 400 Bad Request with AWS ELB error page content.

**Success Indicators**:
- Bad Request response
- AWS ELB-specific error messaging

## Attack Chain Summary

### Key Achievements

1. Identified dangling DNS record on decommissioned EC2
2. Confirmed resource repurposing to third-party AWS ELB
3. Demonstrated potential for subdomain takeover exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]] Gather Victim Host Information: Domains and Subdomains
- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
