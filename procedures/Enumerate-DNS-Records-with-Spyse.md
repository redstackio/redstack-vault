---
id: 849d2c89-3328-462f-b4d6-8e8922331fb7
name: Enumerate-DNS-Records-with-Spyse
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.178098+00:00'
updated_at: '2023-04-10T20:25:09.085434+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather Victim Network Information|T1590 - Gather Victim Network
    Information]]
sub_techniques: []
tags:
  - '[[tags/Getting all DNS records]]'
  - '[[tags/Network Discovery]]'
  - '[[tags/Spyse]]'
commands:
  - '[[commands/spyse-enumerate-dns-records]]'
platforms:
  - Linux
tools:
  - '[[tools/Spyse]]'
validated: true
---

# Enumerate-DNS-Records-with-Spyse

## Summary

This procedure uses the Spyse CLI tool to query the Spyse API and retrieve all DNS records (A, AAAA, CNAME, MX, NS, PTR, SOA, SRV, TXT) for a specified target domain. It supports reconnaissance efforts to map a target's network infrastructure, identify subdomains, mail servers, and other exposed services that could reveal potential entry points or vulnerabilities.

## Description

In offensive security operations, enumerating DNS records is a foundational reconnaissance step to understand the target's digital footprint. Spyse aggregates passive OSINT data from various sources to provide comprehensive DNS information without directly querying the target's authoritative servers, reducing detection risk. This technique is particularly useful in early-stage engagement to discover hidden assets like development subdomains or third-party integrations. The procedure assumes access to a Spyse API key and focuses on automated querying and basic analysis of results to identify actionable intelligence, such as unusual TXT records that might contain tokens or misconfigurations in MX records indicating email infrastructure weaknesses.

## Requirements

1. Valid Spyse API key (obtain from spyse.com dashboard)
2. Internet access for API queries
3. Spyse CLI tool installed (see [[tools/Spyse]] for installation)
4. Basic command-line proficiency

## Defense

Defensive measures and detection strategies:

- Configure DNS records to minimize exposure by removing unnecessary or sensitive information from TXT, MX, and NS entries.
- Implement DNS query logging and monitoring tools like BIND or PowerDNS to detect anomalous bulk queries from Spyse IP ranges.
- Use DNSSEC to validate record integrity and prevent passive reconnaissance from revealing structure.
- Regularly audit public DNS data using tools like DNSDumpster or SecurityTrails to identify and clean up unintended exposures.

## Objectives

1. Retrieve all available DNS records for the target domain to map network infrastructure.
2. Analyze records for potential vulnerabilities, such as exposed subdomains or misconfigured services.
3. Identify security risks like hardcoded secrets in TXT records or outdated NS servers for further targeting.

## Instructions

### Step 1: Verify Spyse Installation and API Key

**Context**: Ensure the Spyse tool is installed and configured with your API key to avoid authentication errors during enumeration. This step confirms prerequisites before querying.

Set the API key as an environment variable:

```bash
export SPYSE_API_KEY=your_api_key_here
```

> Run `spyse --version` to verify installation. Expected output includes the tool version (e.g., "Spyse CLI v1.0.0").

### Step 2: Enumerate DNS Records

**Context**: Use the Spyse CLI to query all DNS record types for the target domain. This retrieves passive intelligence on the domain's DNS footprint, helping identify hosts, services, and potential attack vectors.

**Command** ([[commands/spyse-enumerate-dns-records]]):

```bash
spyse -target $_TARGET_DOMAIN --dns-all
```

> Replace $_TARGET_DOMAIN with the target (e.g., example.com). The --dns-all flag fetches A, AAAA, CNAME, MX, NS, PTR, SOA, SRV, and TXT records. Expected output is a JSON-formatted list of records, such as {"records": [{"type": "A", "value": "192.0.2.1", "name": "www.example.com"}]}. Pipe to jq for parsing if needed: `spyse -target $_TARGET_DOMAIN --dns-all | jq '.records[] | select(.type == "MX")'`.

### Step 3: Analyze Results for Vulnerabilities

**Context**: Review the output to identify useful intelligence, such as subdomains for further probing or TXT records with SPF/DKIM details that might indicate email spoofing opportunities.

Save output to a file and grep for specific types:

```bash
spyse -target $_TARGET_DOMAIN --dns-all > dns_records.json
cat dns_records.json | jq '.records[] | .name + " " + .type + " " + .value'
```

> Expected output: A tabular or filtered list of records (e.g., "mail.example.com MX 10 mailserver.example.com"). Look for anomalies like wildcard records or unexpected CNAMEs pointing to cloud providers, which could guide subsequent enumeration.
