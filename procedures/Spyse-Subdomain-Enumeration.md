---
id: acac489e-2e4c-4867-94ce-3075a4afe142
name: Spyse-Subdomain-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.100069+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather Victim Network Information|T1590 - Gather Victim Network
    Information]]
sub_techniques: []
tags:
  - '[[tags/Network Discovery]]'
  - '[[tags/Searching for subdomains]]'
  - '[[tags/Spyse]]'
commands:
  - '[[commands/spyse-enumerate-subdomains]]'
platforms:
  - Linux
  - macOS
tools:
  - '[[tools/Spyse]]'
validated: true
---

# Spyse-Subdomain-Enumeration

## Summary

Spyse Subdomain Enumeration is a reconnaissance procedure that leverages the Spyse platform's CLI tool to discover subdomains associated with a target domain. This helps identify hidden attack surfaces, such as forgotten or misconfigured subdomains, by querying Spyse's database of internet assets gathered from DNS lookups, zone transfers, and web crawling.

## Description

This procedure uses the Spyse tool to perform passive subdomain enumeration without directly interacting with the target's DNS infrastructure, reducing detection risk. It is particularly useful in early-stage reconnaissance to map the target's digital footprint. The Spyse platform aggregates data from multiple sources to provide comprehensive subdomain lists, including associated IP addresses, SSL certificates, and open ports. In an attack scenario, this information can reveal entry points for further exploitation, such as vulnerable web applications on subdomains. Prerequisites include an active Spyse account with API access. The procedure assumes a Linux or macOS environment where the Spyse CLI is installed.

## Requirements

1. Active Spyse account with API key (free tier available for limited queries).
2. Spyse CLI tool installed on a Linux or macOS system.
3. Network access to the internet (no direct target access needed).
4. Basic command-line proficiency.

## Defense

Defensive measures and detection strategies:

- Monitor for subdomain enumeration attempts via DNS query logs or external intelligence services.
- Implement DNS sinkholing and rate limiting on authoritative DNS servers.
- Use services like Spyse defensively to proactively discover and secure exposed subdomains.
- Regularly audit and remove unused subdomains to shrink the attack surface.

## Objectives

1. Discover all subdomains associated with the target domain.
2. Identify potential attack surfaces from enumerated subdomains.
3. Gather additional metadata like IPs and ports for further reconnaissance.

## Instructions

### Step 1: Verify Spyse CLI Installation and Authentication

**Context**: Ensure the Spyse tool is installed and authenticated with your API key to avoid runtime errors. This step confirms the tool is ready for enumeration.

Install or verify Spyse using [[tools/Spyse]] documentation, then authenticate:

```bash
spyse auth --api-key $_API_KEY
```

> Replace $_API_KEY with your actual Spyse API key. Expected output: Confirmation message like "Authentication successful" if the key is valid.

### Step 2: Enumerate Subdomains for the Target Domain

**Context**: Run the core enumeration command to query Spyse's database for subdomains. This retrieves a list based on passive data collection, providing a broad view of the target's subdomain landscape.

**Command** ([[commands/spyse-enumerate-subdomains]]):

```bash
spyse -target $_TARGET_DOMAIN --subdomains
```

> Use $_TARGET_DOMAIN as a placeholder for the target (e.g., example.com). This command searches Spyse's index for subdomains. Expected output: A JSON or tabular list of subdomains, such as "sub1.example.com", "sub2.example.com", along with metadata like IPs if available.

### Step 3: Parse and Export Results for Analysis

**Context**: Process the output to save subdomains to a file for further use, such as feeding into other tools like httpx for liveliness checks. This step verifies success and prepares data for chaining with other procedures.

Save output to a file:

```bash
spyse -target $_TARGET_DOMAIN --subdomains > subdomains.txt
```

> Review subdomains.txt for the list. If no subdomains are found, verify your API quota or try a well-known domain for testing. Expected output: File containing subdomain entries, e.g., one per line or in JSON format.

### Step 4: Validate and Cross-Reference Results

**Context**: Check the enumerated subdomains against known sources to ensure completeness and identify any high-value targets. This adds context to the results.

Use grep or similar to filter:

```bash
cat subdomains.txt | grep -v "www"
```

> This excludes common subdomains like www. Expected output: Filtered list excluding noise. Cross-reference with tools like [[commands/dig-dns-lookup]] for verification.
