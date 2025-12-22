---
type: procedure
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Search Open Technical Databases|T1596 - Search Open Technical
    Databases]]
sub_techniques:
  - '[[sub-techniques/DNS/Passive DNS|T1596.001 - DNS/Passive DNS]]'
  - '[[sub-techniques/Digital Certificates|T1596.003 - Digital Certificates]]'
tags:
  - '[[tags/Enumerate all subdomains (only if the scope is *.domain.ext)]]'
  - '[[tags/Subdomains Enumeration]]'
  - '[[tags/Using Aquatone - new version (Go)]]'
commands:
  - '[[commands/subfinder-enumerate-subdomains]]'
  - '[[commands/aquatone-scan-subdomains-from-file]]'
  - '[[commands/amass-active-brute-subdomains]]'
tools:
  - '[[tools/subfinder]]'
  - '[[tools/amass]]'
  - '[[tools/Aquatone]]'
platforms:
  - Linux
skill_level: beginner
impact_level: low
detection_risk: low
verified: true
validated: true
---

# Subdomain-Enumeration-and-Scan-with-Aquatone

## Summary

This procedure performs subdomain enumeration on a target domain using passive and active techniques with Subfinder and Amass, followed by scanning the discovered subdomains with Aquatone to identify open ports, HTTP/HTTPS services, and generate visual reports. It is useful for reconnaissance in penetration testing to map the attack surface of a target organization's infrastructure.

## Description

Subdomain enumeration reveals hidden or forgotten subdomains that may expose additional attack vectors, such as administrative interfaces or misconfigured services. Subfinder uses passive sources like search engines and public databases for quick, low-noise discovery, while Amass employs active brute-forcing for more comprehensive results. Aquatone, a Go-based tool, then actively scans these subdomains for common ports and web technologies, producing an interactive HTML report with screenshots and technology fingerprints. This approach is ideal for offensive security engagements where understanding the full domain footprint is critical, but it generates network traffic that could be detected. The procedure assumes a Linux environment with the tools pre-compiled and placed in specific directories like ./Subfinder, ./Amass, and ./Aquatone.

## Requirements

1. Network access to query public DNS resolvers (e.g., 8.8.8.8, 1.1.1.1) and the target domain.
2. Installed and executable binaries for Subfinder, Amass, and Aquatone in the specified paths (./Subfinder/subfinder, ./Amass/amass, ./Aquatone/aquatone).
3. Write permissions to /tmp for output files.
4. Basic knowledge of bash scripting and DNS concepts.

## Defense

- Implement strict access controls to restrict access to sensitive information.
- Regularly monitor and log network traffic to detect any suspicious activity.
- Use intrusion detection and prevention systems to detect and prevent attacks.

## Objectives

1. Identify all subdomains of a target domain using passive and active methods.
2. Scan the discovered subdomains for open ports and HTTP(S) servers.
3. Gather information about a target's infrastructure and architecture through generated reports.

## Instructions

### Step 1: Enumerate Subdomains with Subfinder

**Context**: Use Subfinder for passive subdomain discovery by querying multiple public sources via specified DNS resolvers. This step minimizes noise as it avoids direct interaction with the target nameservers. The results are saved to a temporary file for further processing.

**Command** ([[commands/subfinder-enumerate-subdomains]]):
```bash
./Subfinder/subfinder -d $_DOMAIN -r 8.8.8.8,1.1.1.1 -nW -o $_OUTPUT_FILE
```

> This command enumerates subdomains for the given domain using resolvers 8.8.8.8 and 1.1.1.1, disables wildcard handling with -nW, and outputs to a file. Expected output is a list of discovered subdomains written to $_OUTPUT_FILE, such as "sub1.target.com\nsub2.target.com". Verify by checking the file contents with cat $_OUTPUT_FILE; success if at least one subdomain is listed beyond the root domain.

### Step 2: Scan Subfinder Results with Aquatone

**Context**: Pipe the Subfinder output to Aquatone to perform active scanning on the discovered subdomains, focusing on a large set of common ports to identify live services and web technologies. This generates an HTML report with screenshots and details.

**Command** ([[commands/aquatone-scan-subdomains-from-file]]):
```bash
cat $_INPUT_FILE | ./Aquatone/aquatone -ports large -out $_OUTPUT_DIR
```

> This pipes the subdomain list to Aquatone, scanning large port ranges and outputting results to an HTML directory. Expected output is a directory $_OUTPUT_DIR containing index.html with a dashboard of scanned hosts, including screenshots, HTTP headers, and technology info. Success if the report shows live subdomains with open ports like 80/443.

### Step 3: Enumerate Subdomains with Amass Brute Force

**Context**: Use Amass for active brute-force enumeration to discover additional subdomains not found passively. This is more aggressive and may generate more detectable traffic but uncovers hidden assets.

**Command** ([[commands/amass-active-brute-subdomains]]):
```bash
./Amass/amass -active -brute -o $_OUTPUT_FILE -d $_DOMAIN
```

> This runs active enumeration with brute-forcing on the domain, saving unique subdomains to $_OUTPUT_FILE. Expected output is a file with subdomains like "admin.target.com\napi.target.com". Verify with wc -l $_OUTPUT_FILE; success if new subdomains are added compared to Subfinder results.

### Step 4: Scan Amass Results with Aquatone

**Context**: Repeat the Aquatone scan on Amass-discovered subdomains to consolidate findings from both enumeration methods into a unified report. This step ensures comprehensive coverage.

**Command** ([[commands/aquatone-scan-subdomains-from-file]]):
```bash
cat $_INPUT_FILE | ./Aquatone/aquatone -ports large -out $_OUTPUT_DIR
```

> Reuse the Aquatone command on the Amass output file. Expected output appends to or creates a new report in $_OUTPUT_DIR, potentially revealing more services. Success if the combined report covers all unique subdomains from both tools.
