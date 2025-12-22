---
type: procedure
description: >-
  Locate a company's Autonomous System Number (ASN) using the asnlookup tool to
  identify associated IP ranges for further reconnaissance.
verified: true
submitted: false
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Network Information]]'
sub_techniques: []
tags:
  - reconnaissance
  - asn-lookup
  - network-enumeration
commands:
  - '[[commands/asnlookup-lookup-asn-for-organization]]'
platforms:
  - Linux
tools:
  - '[[tools/Asnlookup]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Find-Company-ASN-Using-Asnlookup

## Summary

This procedure uses the asnlookup tool to query an organization's name and retrieve its associated Autonomous System Number (ASN). The ASN provides critical network information, such as public IP CIDR ranges, which can be used for subsequent subdomain enumeration, IP scanning, and mapping the target's attack surface during reconnaissance phases of security assessments.

## Description

Autonomous System Numbers (ASNs) are unique identifiers assigned to networks or organizations by regional internet registries. By looking up an ASN via the organization's name, attackers or red teamers can enumerate the public IP blocks (CIDRs) allocated to that ASN. This information is valuable for discovering hosted domains, subdomains, and services without direct interaction with the target. The asnlookup tool automates queries to WHOIS databases and other sources to fetch this data. This technique is commonly used in passive reconnaissance to build a profile of the target's infrastructure before active scanning begins. It maps to MITRE ATT&CK under Reconnaissance, specifically gathering victim network information.

## Requirements

1. Python 3.x installed on a Linux system (e.g., Kali or Ubuntu).
2. Git for cloning the tool repository.
3. Internet access for querying public registries.
4. The asnlookup tool installed (see [[tools/Asnlookup]] for installation).
5. Basic knowledge of networking concepts like ASNs and CIDR notation.

## Defense

Defensive measures and detection strategies:

- Monitor for automated WHOIS queries or ASN lookups from unusual IP addresses using network traffic analysis tools like Zeek or Suricata.
- Implement rate limiting on public-facing WHOIS services if hosting any.
- Use threat intelligence feeds to track reconnaissance tools like asnlookup.
- Educate teams on OSINT risks and monitor for leaked ASN details in public reports.

## Objectives

1. Retrieve the target organization's ASN to identify network ownership.
2. Extract associated CIDR ranges for IP enumeration.
3. Enable follow-on reconnaissance activities like subdomain discovery.
4. Maintain low detection risk through passive querying.

## Instructions

### Step 1: Verify Tool Installation

**Context**: Ensure the asnlookup tool is available and functional before performing the lookup. This step confirms prerequisites are met and avoids runtime errors.

Run the help command to verify installation:

**Command** ([[commands/asnlookup-show-help]]):
```bash
python asnlookup.py --help
```

> This displays available options and confirms the tool is executable. If errors occur, refer to the [[tools/Asnlookup]] installation guide.

### Step 2: Perform ASN Lookup for Organization

**Context**: Query the tool with the target organization's name to retrieve the ASN and related network details. Replace the organization name with the actual target (e.g., 'google' or 'microsoft'). This step accomplishes the core reconnaissance objective.

**Command** ([[commands/asnlookup-lookup-asn-for-organization]]):
```bash
python asnlookup.py -o <Organization>
```

> The command queries public databases and outputs the ASN, owner details, and CIDR blocks. For example, inputting 'apple' might reveal AS714: Apple Inc., with associated IP ranges.

### Step 3: Parse and Document Output

**Context**: Review the results to extract actionable intelligence, such as ASN number and CIDR ranges. This step involves manual verification and preparation for next phases, like feeding CIDRs into IP scanners.

Save the output to a file for analysis:

**Command** ([[commands/asnlookup-lookup-asn-for-organization]]):
```bash
python asnlookup.py -o <Organization> > asn_results.txt
```

> Examine the file for key details: ASN ID, description, country, and IP prefixes. Verify accuracy against public WHOIS tools. If multiple ASNs appear, prioritize the primary one based on description.

## Expected Output

Successful execution produces output similar to:

```
Organization: Apple Inc.
ASN: 714
Description: APPLE-AUSTIN4 - Apple Inc.
Country: US
CIDR Ranges:
- 17.0.0.0/8
- 17.32.0.0/11
... (additional prefixes)
```

Look for the ASN number, organization match, and list of IPv4/IPv6 prefixes. Errors may indicate invalid organization names or network issues—retry with variations (e.g., full legal name).
