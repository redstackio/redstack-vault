---
id: 650475bd-c92f-4d7d-a718-1b41c22f7544
name: Enumerate-Domains-from-CIDR-IP-Range-Using-Amass
type: procedure
verified: true
submitted: false
created_at: '2020-06-29T16:32:10.923635+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Network Information]]'
sub_techniques:
  - '[[IP Addresses]]'
tags:
  - reconnaissance
  - domain-enumeration
  - passive-intel
commands:
  - '[[commands/amass-intel-ip-cidr-enumeration]]'
platforms:
  - Linux
tools:
  - '[[tools/amass]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Enumerate-Domains-from-CIDR-IP-Range-Using-Amass

## Summary

This procedure uses the Amass tool to perform passive intelligence gathering, enumerating domain names associated with a specified CIDR IP range. It is particularly effective against organizations hosted by Managed Service Providers (MSPs) or in dedicated data centers, where IP ranges are more static and tied to specific entities. In cloud environments like AWS or Azure, results may be limited due to dynamic elastic IPs assigned by the provider rather than the organization.

## Description

Amass leverages open-source intelligence (OSINT) sources such as certificate transparency logs, DNS records, and public databases to reverse-map IP addresses within a CIDR block to their corresponding domain names. This technique is non-intrusive and does not directly interact with the target network, making it suitable for early reconnaissance phases. The procedure identifies potential attack surfaces by revealing subdomains or hostnames that resolve to the given IP range, which can inform further enumeration or targeting. It maps to MITRE ATT&CK under Reconnaissance, focusing on gathering victim network information via IP addresses. Prerequisites include a valid CIDR notation (e.g., 13.224.8.0/21) and access to Amass, which performs all queries passively to avoid detection.

## Requirements

1. Amass tool installed and configured ([[tools/amass]]).
2. A target CIDR IP range in valid notation (e.g., x.x.x.x/yy).
3. Internet connectivity for querying OSINT sources.
4. Basic command-line proficiency; no target credentials or direct network access needed.

## Defense

Defensive measures and detection strategies:

- Monitor for passive DNS queries or OSINT scraping via tools like DNS firewall rules or threat intelligence feeds.
- Implement certificate transparency monitoring to detect unusual domain registrations tied to IP ranges.
- Use network segmentation to limit exposure of static IP blocks in data centers.
- Employ SIEM rules to alert on reconnaissance patterns from known OSINT tools like Amass.

## Objectives

1. Identify all domains and subdomains resolving to the specified CIDR IP range.
2. Build a list of potential targets for further reconnaissance or exploitation.
3. Validate the hosting environment (e.g., MSP vs. cloud) to refine attack strategy.
4. Output a mappable dataset of IP-domain associations for visualization or integration with other tools.

## Instructions

### Step 1: Verify Amass Installation and Configuration

**Context**: Ensure Amass is installed and ready to use, as this procedure relies on its intel module for passive enumeration. This step confirms the tool's availability and tests basic functionality to avoid runtime errors.

**Command** ([[commands/amass-intel-ip-cidr-enumeration]]):

Run a dry test with a small or known CIDR to verify output format.

```bash
amass intel -ip -cidr 8.8.8.0/24
```

> This command queries public sources for domains in the test range. If no errors occur and output appears (even if empty), proceed. Expected: List of domains or empty if no matches; confirms tool is operational.

### Step 2: Prepare the Target CIDR Range

**Context**: Select and validate the CIDR range based on prior intelligence (e.g., from ASN lookup or organization profiling). This ensures the input is accurate and scoped appropriately to avoid overwhelming queries or irrelevant results.

No specific command here; manually define the CIDR (e.g., from Shodan or WHOIS data). If the range is too broad (e.g., /16), narrow it to /21 or smaller for efficiency. Decision point: If targeting a cloud provider's range, cross-reference with ASN to filter; otherwise, proceed directly.

Expected: A validated CIDR string ready for input, e.g., "13.224.8.0/21".

### Step 3: Execute Domain Enumeration

**Context**: Run the core Amass intel command to gather domain names passively. This step performs the actual reverse IP-to-domain mapping using multiple OSINT feeds, producing a list of discovered assets.

**Command** ([[commands/amass-intel-ip-cidr-enumeration]]):

```bash
amass intel -ip -cidr $_CIDR_RANGE -o output.txt
```

> Replace $_CIDR_RANGE with your prepared CIDR (e.g., 13.224.8.0/21). The -o flag saves results to a file for further processing. Amass will query sources like Reverse DNS, Certificate Transparency, and public APIs. This may take several minutes depending on range size. Expected: A file with lines of "domain IP" pairs.

### Step 4: Review and Parse Results

**Context**: Analyze the output to identify relevant domains, filtering out noise (e.g., provider-owned domains). This step verifies success and prepares data for next phases like subdomain brute-forcing.

Use standard Linux tools to inspect:

```bash
cat output.txt | sort -u
```

> This deduplicates and sorts the list. Decision point: If results are sparse, expand to related ASNs; if abundant, prioritize by relevance (e.g., grep for target organization keywords). Expected: Clean list of unique domain-IP mappings.

### Step 5: Integrate with Further Reconnaissance

**Context**: Feed discovered domains into complementary tools for deeper enumeration, ensuring the procedure contributes to a broader attack chain.

For example, pipe to httpx for live host checking (assuming another procedure):

```bash
cut -d' ' -f1 output.txt | httpx -silent -o live_domains.txt
```

> This verifies which domains are active. Expected: Reduced list of responsive domains, indicating viable targets.
