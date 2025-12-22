---
id: 90af0264-cf90-462c-9a68-fa67700ecd38
name: Probe-Domains-for-Active-HTTP-HTTPS-Servers-Using-HTTProbe
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:22.899720+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - reconnaissance
  - web-probing
  - http-https
commands:
  - '[[commands/httprobe-probe-domains-for-http-https]]'
  - '[[commands/httprobe-probe-domains-for-http-https-on-custom-ports]]'
platforms:
  - Linux
  - macOS
tools:
  - '[[tools/httprobe]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Probe-Domains-for-Active-HTTP-HTTPS-Servers-Using-HTTProbe

## Summary

This procedure uses the httprobe tool to scan a list of domains and identify which ones are actively serving HTTP or HTTPS content. It is a key step in web reconnaissance to filter out inactive domains and focus on live web servers for further enumeration or testing.

## Description

httprobe performs parallel HTTP and HTTPS probes against a list of domains to determine which ones respond successfully. This helps in narrowing down the attack surface during reconnaissance phases of security assessments. The tool is efficient for large lists and supports custom ports for non-standard configurations. It outputs only the live URLs, making it easy to pipe into other tools like directory busters or vulnerability scanners. This technique aligns with active scanning for victim host information, commonly used in external reconnaissance to map web presence without relying on DNS resolution alone.

## Requirements

1. A text file containing a list of domains (one per line, e.g., example.com, sub.example.com).
2. httprobe tool installed on a Linux or macOS system.
3. Network access to the target domains (no firewall blocks on ports 80/443 or custom ports).
4. Basic command-line knowledge for piping inputs.

## Defense

Defensive measures and detection strategies:

- Monitor for unusual HTTP/HTTPS traffic patterns from scanning tools, such as rapid connections to port 80/443 from a single IP.
- Implement web application firewalls (WAFs) to rate-limit or block probe-like requests.
- Use network intrusion detection systems (NIDS) to flag high-volume probing on web ports.
- Log and analyze access logs for non-browser user agents or sequential domain requests.

## Objectives

1. Identify live HTTP/HTTPS endpoints from a domain list to prioritize reconnaissance targets.
2. Support custom port probing for environments with non-standard web configurations.
3. Generate a filtered list of active web servers for subsequent tool chaining.
4. Ensure efficient scanning with minimal false positives by verifying actual server responses.

## Instructions

### Step 1: Prepare Domain List

**Context**: Create or obtain a file with target domains to probe. This step ensures input is clean and ready for httprobe, avoiding errors from invalid formats.

Use a text editor or previous reconnaissance tools to generate the list. For example, if you have a file from subdomain enumeration:

```bash
# Assume domains.txt exists with one domain per line
cat domains.txt
```

Expected output: A list like:

```
example.com
sub.example.com
api.example.com
```

### Step 2: Probe Standard HTTP/HTTPS Ports

**Context**: Run httprobe on the domain list to check for active servers on default ports (80 for HTTP, 443 for HTTPS). This identifies basic web presence and outputs live URLs.

**Command** ([[commands/httprobe-probe-domains-for-http-https]]):

```bash
cat domains.txt | httprobe
```

> This command reads domains from stdin, probes each for HTTP/HTTPS, and prints only responding URLs (e.g., http://example.com or https://sub.example.com). It performs concurrent checks for efficiency.

### Step 3: Probe Custom Ports if Needed

**Context**: If the target environment uses non-standard ports for web services, specify them explicitly. This step extends the scan to cover variations like HTTP on port 81 or HTTPS on 8443, common in internal or misconfigured setups.

**Command** ([[commands/httprobe-probe-domains-for-http-https-on-custom-ports]]):

```bash
cat domains.txt | httprobe -p http:81 -p https:8443
```

> The -p flag defines protocols and ports. Output will include scheme://domain:port for responders, such as http://example.com:81. Use this when standard probes yield no results but web services are suspected on alternate ports.

### Step 4: Save and Verify Results

**Context**: Redirect output to a file for further use and manually verify a sample to ensure accuracy. This confirms the procedure's success and prepares data for next steps like service enumeration.

```bash
cat domains.txt | httprobe > live_servers.txt
echo "Sample check:"
head -5 live_servers.txt
```

Expected output: A file with live URLs, e.g.,

```
https://example.com
http://sub.example.com
```

If no output, check domain list validity or network connectivity.
