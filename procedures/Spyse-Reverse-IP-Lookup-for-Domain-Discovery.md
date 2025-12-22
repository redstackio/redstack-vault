---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
  - '[[Gather Victim Network Information]]'
sub_techniques: []
tags:
  - network-discovery
  - reverse-ip-lookup
  - spyse
  - reconnaissance
commands:
  - '[[commands/spyse-domains-on-ip-lookup]]'
tools:
  - '[[tools/Spyse]]'
platforms:
  - Linux
  - macOS
validated: true
---

# Spyse-Reverse-IP-Lookup-for-Domain-Discovery

## Summary

This procedure uses the Spyse CLI tool to perform a reverse IP lookup, identifying all domains and subdomains hosted on a target IP address. It is a key reconnaissance technique for mapping the attack surface by discovering co-hosted sites, which may reveal additional entry points, shared vulnerabilities, or related infrastructure in offensive security operations.

## Description

Network discovery through reverse IP lookup helps attackers understand the target's hosting environment by querying DNS records and IP mappings. Spyse aggregates public data sources to provide details on domains sharing the same server, including hosting providers, SSL certificates, and DNS records. This can uncover hidden assets, such as development sites or misconfigurations on the same infrastructure. The procedure targets IP addresses obtained from prior enumeration (e.g., via WHOIS or DNS resolution) and outputs a list of associated domains for further investigation. It is particularly useful in early reconnaissance phases to expand the scope beyond the initial target domain.

## Requirements

1. Access to a Spyse account with API credentials (free tier available for basic queries).
2. The Spyse CLI tool installed on a Linux or macOS system.
3. Target IP address (e.g., resolved from a domain via nslookup or dig).
4. Network connectivity to query Spyse's API endpoints.

## Defense

- Implement network segmentation to isolate critical servers from shared hosting environments.
- Regularly audit DNS records and monitor for unexpected domain associations using tools like DNSDumpster or internal logging.
- Use dedicated IP addresses for sensitive applications and enable SSL/TLS pinning to limit exposure from co-hosted sites.
- Deploy web application firewalls (WAFs) to detect and block reconnaissance queries targeting infrastructure details.

## Objectives

1. Identify all domains and subdomains hosted on the target IP to expand the attack surface.
2. Gather metadata on co-hosted sites, such as hosting providers and certificates, for targeted follow-up attacks.
3. Refine reconnaissance by prioritizing vulnerable or related assets discovered through the lookup.

## Instructions

### Step 1: Configure Spyse API Access

**Context**: Before running lookups, set up your Spyse API key to authenticate queries. This ensures access to the platform's database without rate limits on free tiers.

**Command** (Manual setup, no specific command):

First, obtain your API key from the Spyse dashboard and export it as an environment variable:

```bash
export SPYSE_API_KEY=your_api_key_here
```

> This step prepares the environment for authenticated API calls. Verify by running `spyse --help`; successful authentication will show available options without errors.

### Step 2: Resolve Target Domain to IP (If Needed)

**Context**: If starting from a domain, resolve it to an IP address using standard DNS tools. This provides the input for the reverse lookup.

Use a basic DNS resolution command (not Spyse-specific):

```bash
dig +short target-domain.com
```

> Expected output: The IP address (e.g., 52.14.144.171). If the domain resolves to multiple IPs, select the primary one or iterate over them. This step ensures the target IP is accurate for the lookup.

### Step 3: Perform Reverse IP Lookup

**Context**: Execute the Spyse command to query domains associated with the target IP. This retrieves a comprehensive list of co-hosted domains, enabling broader reconnaissance.

**Command** ([[commands/spyse-domains-on-ip-lookup]]):

```bash
spyse -target $_TARGET_IP --domains-on-ip
```

> Replace $_TARGET_IP with the resolved IP (e.g., 52.14.144.171). The command queries Spyse's database and returns domains sharing the IP. If no API key is set, it will prompt for authentication. For large results, pipe to a file: `spyse -target $_TARGET_IP --domains-on-ip > domains.txt`. This step accomplishes the core objective of domain discovery.

### Step 4: Analyze and Verify Results

**Context**: Review the output for relevant domains and verify their status (e.g., alive, vulnerable) to prioritize next steps.

Use grep or manual inspection:

```bash
grep -i "target-related" domains.txt
```

> Expected: Filtered list of potentially related domains. Cross-reference with tools like httpx for liveness: `cat domains.txt | httpx -silent`. Success is confirmed by identifying at least one additional domain, indicating expanded scope.
