---
tags:
  - xxe
  - xml
  - semrush
  - file-read
  - directory-listing
type: attack_chain
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - Linux
complexity: medium
procedures:
  - '[[procedures/Create-Semrush-Project-with-Attacker-Domain]]'
  - '[[procedures/Configure-Site-Audit-with-Malicious-Sitemap]]'
  - '[[procedures/Trigger-XXE-in-Site-Audit]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of XXE vulnerability in Semrush Site Audit by providing a
  malicious sitemap.xml to read arbitrary server files and list directories.
skill_level: intermediate
impact_level: high
id: 317280e9-ab5e-4693-b2df-a9a94f3f8a50
created_at: '2025-12-13T09:00:33.792Z'
updated_at: '2025-12-13T09:00:33.792Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# XXE Injection via Malicious Sitemap in Semrush to Expose Server Files

Multi-stage attack chain demonstrating exploitation of an XXE vulnerability in Semrush's Site Audit function by crafting and submitting a malicious sitemap.xml file, allowing arbitrary file reading and directory listing on the server.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Project] --> B[Set Up Audit]
    B --> C[Configure Sitemap]
    C --> D[Start Audit]
    D --> E[Trigger XXE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#2c3e50
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox]]
- [[tools/Google-Chrome]]

### Target Environment

- Web-based platform (Semrush)
- Linux server with Java XML processor
- Network access to Semrush and attacker-controlled domain

### Initial Access Requirements

- Semrush account
- Control over a domain for hosting malicious sitemap.xml
- No prior server access needed

## Detailed Attack Procedures

### Step 1: Create Project with Attacker Domain
procedure: [[procedures/Create-Semrush-Project-with-Attacker-Domain]]

**Objective**: Set up a new project in Semrush using an attacker-controlled domain to host the malicious sitemap.

**Instructions**: Log into Semrush and create a new project. Set the domain to one controlled by the attacker, such as semrush.webhooks.pw.

**Expected Output**: A new project is created successfully.

**Success Indicators**:
- Project creation confirmed
- Domain associated with the project

### Step 2: Set Up New Site Audit
procedure: [[procedures/Configure-Site-Audit-with-Malicious-Sitemap]]

**Objective**: Initiate a new Site Audit for the project.

**Instructions**: Within the project, navigate to the Site Audit section and start a new audit.

**Expected Output**: Site Audit setup is initiated.

**Success Indicators**:
- Audit setup screen appears
- Ready to configure crawl source

### Step 3: Configure Audit with Malicious Sitemap
procedure: [[procedures/Configure-Site-Audit-with-Malicious-Sitemap]]

**Objective**: Change the crawl source to use the malicious sitemap URL.

**Instructions**: In Site Audit settings, select 'Enter sitemap URL' as the crawl source and provide the URL of the malicious sitemap.xml, e.g., http://static.webhooks.pw/files/semrush_sitemap.xml. This sitemap should be crafted to include external entities that resolve to server files like /etc/hostname or directories like /home.

**Expected Output**: Settings are saved with the malicious URL.

**Success Indicators**:
- Sitemap URL accepted
- No validation errors

### Step 4: Start the Site Audit
procedure: [[procedures/Trigger-XXE-in-Site-Audit]]

**Objective**: Initiate the audit process to download and process the sitemap.xml.

**Instructions**: Click to start the Site Audit, which will trigger the processing of the provided sitemap.

**Expected Output**: Audit begins processing.

**Success Indicators**:
- Audit status shows processing
- Server begins parsing the XML

### Step 5: Trigger XXE Vulnerability
procedure: [[procedures/Trigger-XXE-in-Site-Audit]]

**Objective**: The XML processor parses the malicious XML, resolving external entities to read files or list directories.

**Instructions**: Monitor the audit process or any exposed outputs where the resolved entities might appear, such as in error messages or audit reports, revealing contents of files like /etc/hostname or directory listings like /home.

**Expected Output**: Sensitive server information is exposed via the XXE injection.

**Success Indicators**:
- Arbitrary files read
- Directory contents listed
- Potential exposure of sensitive data

## Attack Chain Summary

### Key Achievements

1. Successful creation and configuration of a malicious sitemap in Semrush
2. Triggering of XXE vulnerability leading to file and directory exposure
3. Demonstration of arbitrary data access on the server

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

*Last updated: [TIMESTAMP]*
