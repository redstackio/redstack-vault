---
type: procedure
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[IP Addresses]]'
sub_techniques: []
tags:
  - reconnaissance
  - asn
  - osint
  - amass
commands:
  - '[[commands/amass-intel-enumerate-organization]]'
tools:
  - '[[tools/amass]]'
platforms:
  - Linux
skill_level: beginner
impact_level: low
detection_risk: low
verified: true
validated: true
---

# Find-Company-ASN-Using-Amass

## Summary

This procedure uses the Amass tool to enumerate Autonomous System Numbers (ASNs) associated with a target organization. It is a key step in passive reconnaissance to identify network infrastructure, IP ranges, and potential subdomains owned by the company, which can reveal subdivisions, mergers, or acquisitions.

## Description

In offensive security operations, understanding a target's network footprint is essential for mapping the attack surface. ASNs represent blocks of IP addresses controlled by an organization and are publicly available through WHOIS data. Amass's intel module queries passive data sources to retrieve ASNs linked to a company name. This technique falls under MITRE ATT&CK's Reconnaissance tactic, specifically gathering victim network information via IP addresses. It requires internet access but no direct interaction with the target, making it stealthy. Expected outcomes include a list of ASN IDs, descriptions, and owners, which can be used to enumerate IP ranges with tools like whois or further subdomain discovery.

## Requirements

1. Amass tool installed (see [[tools/amass]] for installation).
2. Internet access for querying passive intelligence sources.
3. Basic knowledge of command-line tools and networking concepts.
4. Target company name (exact or partial match for best results).

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous OSINT queries from internal networks, though this is external and hard to detect.
- Implement data leakage prevention by limiting public exposure of ASN-linked assets.
- Use threat intelligence platforms to track reconnaissance attempts on your organization's ASN.

## Objectives

1. Identify all ASNs associated with the target company.
2. Gather descriptive information on each ASN for context (e.g., regional networks).
3. Enable follow-on enumeration of IP blocks and subdomains.

## Instructions

### Step 1: Verify Amass Installation and Configuration

**Context**: Ensure Amass is installed and configured to access passive data sources. This step confirms the tool is ready and avoids runtime errors.

Run the help command to verify functionality.

**Command** ([[commands/amass-intel-enumerate-organization]]):
```bash
amass intel -org example --help
```

> This displays usage options. If Amass is not installed, follow the installation guide in [[tools/amass]]. Expected output includes the -org flag description, confirming the module is available.

### Step 2: Enumerate Organization ASNs

**Context**: Execute the core intelligence gathering to query for ASNs. Provide the exact company name to match against WHOIS and other sources. This retrieves ASN IDs and associated details.

**Command** ([[commands/amass-intel-enumerate-organization]]):
```bash
amass intel -org $_COMPANY_NAME
```

> Replace $_COMPANY_NAME with the target organization (e.g., "Google"). Amass aggregates data from multiple passive sources. If no results, try variations of the company name. Expected output is a comma-separated list of ASN IDs, names, and descriptions.

### Step 3: Parse and Verify Results

**Context**: Review the output to confirm relevant ASNs and note any for further use. This step includes basic validation and preparation for next actions, such as IP range enumeration.

Save the output to a file for analysis:

**Command** ([[commands/amass-intel-enumerate-organization]]):
```bash
amass intel -org $_COMPANY_NAME > asns.txt
```

> Open asns.txt in a text editor or use grep to filter (e.g., grep "Google" asns.txt). Success is indicated by at least one ASN matching the target. If empty, refine the company name or check Amass config for data sources.

### Step 4: Follow-Up Enumeration (Optional)

**Context**: Use discovered ASNs to expand reconnaissance, such as querying IP ranges. This bridges to additional procedures but verifies the initial find.

For each ASN, run a whois query (not part of Amass, but complementary):

```bash
whois -h whois.radb.net '!gASNNNNN' | grep route
```

> Replace NNNNN with the ASN (e.g., AS15169). Expected output: IP prefixes associated with the ASN. This confirms the ASN's validity and scope.
