---
id: ac-udemy-info-disclosure-001
tags:
  - information-disclosure
  - wordpress
  - readme-exposure
  - reconnaissance
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-WordPress-Application-Readme]]'
  - '[[procedures/Access-WordPress-Plugin-Readme]]'
step_count: 2
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:24:56.082Z'
description: >-
  A reconnaissance attack exploiting exposed readme files on a WordPress
  subdomain to disclose application and plugin version information, aiding in
  vulnerability identification.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Information Disclosure via Exposed WordPress Readme Files

Multi-stage reconnaissance chain demonstrating information disclosure through publicly accessible readme files on a WordPress-based subdomain, revealing software versions for potential exploitation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Access Application Readme] --> B[Reconnaissance: Access Plugin Readme]
    B --> C[Objective: Version Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[curl]]

### Target Environment

- WordPress installation on a web subdomain
- Publicly accessible HTTP endpoints
- No authentication required

### Initial Access Requirements

- Internet access to the target subdomain
- No credentials needed
- Direct URL knowledge or subdomain enumeration

## Detailed Attack Procedures

### Step 1: Access Application Readme
procedure: [[procedures/Access-WordPress-Application-Readme]]

**Objective**: Retrieve the application's version information from the exposed readme file to identify the WordPress core version.

**Instructions**: Use a web browser or [[commands/curl-access-url]] to navigate to the readme endpoint:

```bash
curl http://about.udemy.com/readme.html
```

This fetches the content directly. Review the output for version details in the HTML.

**Expected Output**: HTML content containing the WordPress version, such as "WordPress 3.9.1".

**Success Indicators**:
- Version string visible in response
- No 404 or access denied errors

### Step 2: Access Plugin Readme
procedure: [[procedures/Access-WordPress-Plugin-Readme]]

**Objective**: Retrieve the plugin's version information from the exposed readme file to identify vulnerabilities in the All-in-One SEO Pack plugin.

**Instructions**: Use a web browser or [[commands/curl-access-url]] to navigate to the plugin's readme endpoint:

```bash
curl http://about.udemy.com/wp-content/plugins/all-in-one-seo-pack/readme.txt
```

Parse the text output for version and changelog details.

**Expected Output**: Plain text file with plugin metadata, including lines like "Stable tag: 2.6.15".

**Success Indicators**:
- Plugin version and details exposed
- File content retrievable without errors

## Attack Chain Summary

### Key Achievements

1. Disclosed WordPress application version for targeted exploit research
2. Exposed All-in-One SEO Pack plugin version, enabling known vulnerability identification
3. Demonstrated low-effort reconnaissance on misconfigured web installations

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Software]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
