---
type: procedure
description: >-
  Discover SSL/TLS certificates associated with a target domain or organization
  using the Spyse OSINT tool for reconnaissance.
verified: true
submitted: false
created_at: '2023-04-06T03:56:22Z'
updated_at: '2023-04-10T20:25:08Z'
tactics:
  - '[[Resource Development]]'
techniques:
  - '[[Acquire Infrastructure]]'
sub_techniques: []
tags:
  - network-discovery
  - ssl-certificates
  - osint
  - spyse
commands:
  - '[[commands/spyse-ssl-certificate-search-by-domain]]'
  - '[[commands/spyse-ssl-certificate-search-by-organization]]'
platforms:
  - Linux
  - macOS
tools:
  - '[[tools/Spyse]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# SSL-Certificate-Discovery-using-Spyse

## Summary

This procedure uses the Spyse CLI tool to query for SSL/TLS certificates associated with a target domain or organization, enabling attackers or security researchers to map out infrastructure, identify subdomains, and uncover potential phishing targets through certificate transparency data.

## Description

SSL certificate discovery is a reconnaissance technique that leverages public certificate transparency logs and OSINT databases to identify SSL/TLS certificates issued for a target domain or organization. Using Spyse, an OSINT search engine for internet-exposed assets, this procedure retrieves certificate details such as common names (CN), subject alternative names (SANs), issuers, and validity periods. This information provides insights into the target's infrastructure, including hidden subdomains and services that may not be directly discoverable via DNS enumeration. The technique is particularly useful in early-stage reconnaissance to build a comprehensive attack surface model and is mapped to MITRE ATT&CK technique T1583 (Acquire Infrastructure) under the Resource Development tactic.

## Requirements

1. Spyse API key (free tier available for basic queries; obtain from spyse.com)
2. Installed Spyse CLI tool (via pip or package manager)
3. Network access to the internet (no special privileges required)
4. Basic command-line proficiency

## Defense

- Implement certificate pinning and monitoring for unexpected issuances
- Use tools like Certificate Transparency monitors (e.g., Google's CT log monitors) to track and revoke rogue certificates
- Restrict API access to OSINT services like Spyse with rate limiting and authentication
- Employ web application firewalls (WAFs) to detect reconnaissance patterns

## Objectives

1. Retrieve a list of SSL/TLS certificates for a specified domain
2. Identify infrastructure details like subdomains and organizational assets from certificate data
3. Uncover potential vulnerabilities or phishing vectors through certificate analysis

## Instructions

### Step 1: Search SSL Certificates by Domain

**Context**: Begin by querying Spyse for certificates associated with a specific domain, such as a target's primary website. This step enumerates certificates to reveal associated hosts and services. Replace $_DOMAIN with the target domain (e.g., hotmail.com). Ensure your Spyse API key is configured via environment variable (export SPYSE_API_KEY=your_key).

**Command** ([[commands/spyse-ssl-certificate-search-by-domain]]):
```bash
spyse -target $_DOMAIN --ssl-certificates
```

> This command queries the Spyse database for SSL certificates matching the domain. It returns details like certificate IDs, issuers, and SANs. If no API key is set, the command will prompt for authentication.

### Step 2: Search SSL Certificates by Organization

**Context**: Extend the search to an entire organization to discover broader infrastructure, such as all certificates issued to Microsoft. Use the 'org:' prefix in the target. Replace $_ORGANIZATION with the target name (e.g., Microsoft). This helps in mapping corporate assets beyond single domains.

**Command** ([[commands/spyse-ssl-certificate-search-by-organization]]):
```bash
spyse -target "org: $_ORGANIZATION" --ssl-certificates
```

> This command fetches organization-wide certificate data, potentially revealing thousands of entries. Output includes certificate metadata useful for further enumeration. Pipe to jq for JSON parsing if needed (e.g., | jq '.data[] | .name').

### Step 3: Analyze Retrieved Certificates

**Context**: Review the output from previous steps to extract actionable intelligence, such as unique SANs for subdomain enumeration or weak issuers indicating misconfigurations. Save output to a file for offline analysis (e.g., > certs.json).

**Instructions**: Manually inspect the JSON response for fields like 'name', 'issuer', 'validity_not_after', and 'subjects'. Cross-reference with tools like crt.sh for validation. If vulnerabilities are suspected (e.g., expired certs), note them for follow-up procedures like subdomain takeover checks.

> Expected: A JSON array of certificate objects. Decision point: If results exceed 100, paginate using Spyse's --page flag.
