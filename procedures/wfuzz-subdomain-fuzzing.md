---
id: 90f10c29-a639-43a5-8768-cfab3b41324f
name: wfuzz-subdomain-fuzzing
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:40.389777+00:00'
updated_at: '2023-05-26T18:52:49.108344+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques: []
tags:
  - subdomain-enumeration
  - reconnaissance
  - fuzzing
  - dns
commands:
  - '[[commands/wfuzz-fuzz-subdomains]]'
platforms:
  - Linux
  - Web
tools:
  - '[[tools/Wfuzz]]'
validated: true
---

# wfuzz-subdomain-fuzzing

## Summary

This procedure uses the wfuzz tool to perform subdomain fuzzing on a target domain by sending HTTP requests with a wordlist of potential subdomain names in the Host header, identifying valid subdomains based on response differences.

## Description

Subdomain fuzzing is a reconnaissance technique to discover hidden or non-obvious subdomains of a target domain, which can expand the attack surface for further enumeration or exploitation. Wfuzz, a flexible web fuzzer, is used here to brute-force subdomain names by injecting them into the Host header of HTTP requests to the target domain's IP or main site. This method is useful when DNS enumeration tools are unavailable or when testing for virtual hosting configurations. The procedure filters responses to focus on those indicating successful subdomain resolution, such as different response sizes or codes. It maps to MITRE ATT&CK Reconnaissance tactic, specifically gathering victim host information through active scanning-like behavior.

## Requirements

1. Access to a Linux environment with wfuzz installed.
2. A wordlist containing common subdomain names, such as /SecLists/Discovery/DNS/subdomains-top1mil-5000.txt.
3. Network access to the target domain (no authentication required, but firewall rules may block fuzzing).
4. Basic knowledge of HTTP headers and response codes.

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAFs) to rate-limit or block requests with varying Host headers.
- Monitor server logs for unusual patterns of requests to the main domain with non-standard Host values.
- Use DNS logging to detect queries for uncommon subdomains.
- Deploy intrusion detection systems (IDS) to flag high-volume HTTP requests from a single source.

## Objectives

1. Identify valid subdomains that respond differently from invalid ones.
2. Expand the target's attack surface for subsequent reconnaissance.
3. Validate discovered subdomains for further testing.
4. Collect evidence of subdomain structure without direct DNS queries.

## Instructions

### Step 1: Prepare the Environment and Wordlist

**Context**: Ensure wfuzz is installed and the wordlist is available. This step sets up the tools needed for fuzzing, explaining why a quality wordlist is crucial for effective subdomain discovery.

Install wfuzz if not present using [[tools/Wfuzz]] installation instructions. Verify the wordlist path exists and contains relevant subdomain payloads.

### Step 2: Execute Subdomain Fuzzing

**Context**: Run wfuzz to inject subdomain names from the wordlist into the Host header, targeting the main domain's URL. This simulates requests to potential subdomains and identifies valid ones by excluding standard responses (e.g., 404 for invalid). The -c flag enables color output, -f re applies a regex filter if needed, and --hc 311 hides Moved Permanently responses which may indicate redirects.

**Command** ([[commands/wfuzz-fuzz-subdomains]]):
```bash
wfuzz -c -w /SecLists/Discovery/DNS/subdomains-top1mil-5000.txt -u "http://$_TARGET_DOMAIN" -H "Host: FUZZ.$_TARGET_DOMAIN" --hc 311
```

> This command sends requests to the target domain's root URL but overrides the Host header with fuzzing payloads (e.g., admin.target.com). Successful subdomains will return different response codes, sizes, or content compared to invalid ones. Monitor for variations in response length or status codes to identify hits. If the target uses HTTPS, replace http with https and add --ss to follow redirects if necessary.

### Step 3: Analyze and Validate Results

**Context**: Review wfuzz output to extract valid subdomains and verify them manually or with additional tools. This step ensures the results are actionable and filters false positives.

Parse the output for requests where the response differs (e.g., non-404 codes or varying lengths). Use tools like curl or httpx to probe discovered subdomains:

```bash
curl -H "Host: $_SUBDOMAIN.$_TARGET_DOMAIN" http://$_TARGET_IP
```

> Expected results include a list of subdomain payloads that triggered unique responses. Save hits to a file for further enumeration, such as service discovery on those subdomains.
