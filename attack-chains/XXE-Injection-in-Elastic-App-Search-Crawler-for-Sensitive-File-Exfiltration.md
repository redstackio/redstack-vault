---
tags:
  - xxe
  - file-exfiltration
  - elastic
  - crawler
type: attack_chain
tools:
  - '[[tools/Sinatra]]'
  - '[[tools/Ruby]]'
  - '[[tools/openssl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/gem-install-sinatra]]'
  - '[[commands/ruby-server-rb]]'
  - '[[commands/puts-uri-unescape]]'
  - '[[commands/openssl-x509]]'
platforms:
  - Web
  - Cloud-AWS
  - Cloud-Azure
  - Linux
complexity: medium
procedures:
  - '[[procedures/Setup-Attacker-Server-for-XXE]]'
  - '[[procedures/Configure-Enterprise-Search-Crawler]]'
  - '[[procedures/Observe-Exfiltrated-Data]]'
  - '[[procedures/Update-Payload-for-Multi-Line-Exfiltration]]'
  - '[[procedures/Analyze-Leaked-Certificates]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Cloud Storage]]'
description: >-
  Multi-stage attack exploiting XXE in Elastic Enterprise Search's App Search
  web crawler to read and exfiltrate sensitive server files.
skill_level: intermediate
impact_level: high
id: 25f1c907-626a-4924-987a-1cea7499a4ed
created_at: '2025-12-13T09:00:27.307Z'
updated_at: '2025-12-13T09:00:27.307Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Cloud Storage]]'
---
# XXE Injection in Elastic App Search Crawler for Sensitive File Exfiltration

Multi-stage attack chain demonstrating exploitation of XXE vulnerability in Elastic Enterprise Search's App Search web crawler version 7.12.0, leading to arbitrary file reads and exfiltration of sensitive data such as credentials, private keys, and configuration files.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Attacker Server] --> B[Configure Crawler]
    B --> C[Observe Exfiltration]
    C --> D[Update Payload]
    D --> E[Analyze Leaked Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#8e44ad
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Sinatra]]
- [[tools/Ruby]]
- [[tools/openssl]]

### Target Environment

- Linux-based server running Elastic Enterprise Search 7.12.0
- Services: App Search Web Crawler, Elasticsearch, Enterprise Search
- Ports: 443, 9243
- Network access to the attacker's domain

### Initial Access Requirements

- Access to Enterprise Search UI for configuration
- Ability to host a public malicious server

## Detailed Attack Procedures

### Step 1: Setup Attacker Server
procedure: [[procedures/Setup-Attacker-Server-for-XXE]]

**Objective**: Create a malicious server to serve robots.txt and sitemap.xml files that trigger XXE.

**Instructions**: Install Sinatra using [[commands/gem-install-sinatra]]:

```bash
gem install sinatra
```

Then run the server script using [[commands/ruby-server-rb]]:

```bash
ruby server.rb
```

**Expected Output**: Server startup logs and routes for /robots.txt, /sitemap.xml, and /exfil.dtd.

**Success Indicators**:
- Server is running and accessible
- Malicious files are hosted

### Step 2: Configure Enterprise Search Crawler
procedure: [[procedures/Configure-Enterprise-Search-Crawler]]

**Objective**: Point the web crawler to the attacker's domain to initiate parsing of malicious sitemap.

**Instructions**: Log into Enterprise Search UI, create an engine, enable web crawler, enter the attacker's domain URL, and start the crawl.

**Expected Output**: Crawler begins processing the domain.

**Success Indicators**:
- Crawl starts successfully
- Requests hit the attacker server

### Step 3: Observe Exfiltrated Data
procedure: [[procedures/Observe-Exfiltrated-Data]]

**Objective**: Monitor server logs for exfiltrated file contents triggered by XXE.

**Instructions**: Check the attacker server's console for incoming requests to /exfil endpoint with query parameters containing file data like /etc/hostname.

**Expected Output**: Logs showing exfiltrated data as query strings.

**Success Indicators**:
- File contents appear in logs
- Successful XXE confirmation

### Step 4: Update Payload for Multi-Line Exfiltration
procedure: [[procedures/Update-Payload-for-Multi-Line-Exfiltration]]

**Objective**: Modify the payload to handle multi-line files and directory listings.

**Instructions**: Update sitemap.xml and add /pingback endpoint. Restart server with [[commands/ruby-server-rb]]:

```bash
ruby server.rb
```

Use [[commands/puts-uri-unescape]] in the script to print unescaped query strings.

**Expected Output**: Unescaped contents of files like /etc/passwd or directory listings.

**Success Indicators**:
- Multi-line data exfiltrated
- Directory structures revealed

### Step 5: Analyze Leaked Certificates
procedure: [[procedures/Analyze-Leaked-Certificates]]

**Objective**: Parse and examine leaked certificate files for further exploitation potential.

**Instructions**: Use [[commands/openssl-x509]] to analyze the certificate:

```bash
openssl x509 -in node.crt -text -noout
```

**Expected Output**: Certificate details including issuer, subject, and public key.

**Success Indicators**:
- Certificate information extracted
- Potential for MITM or further attacks identified

## Attack Chain Summary

### Key Achievements

1. Successful XXE injection via sitemap parsing
2. Exfiltration of sensitive files including credentials and keys
3. Potential for privilege escalation and data exposure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Cloud Storage]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

*Last updated: 2023-10-01*
