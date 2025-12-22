---
type: code
language: bash
verified: true
tags:
  - reconnaissance
  - script
  - subdomain-enumeration
platforms:
  - Linux
validated: true
---

# subdomain-enumeration-script-subfinder-and-amass

## Code

```bash
# Subfinder version
./Subfinder/subfinder -d $1 -r 8.8.8.8,1.1.1.1 -nW -o /tmp/subresult$1
cat /tmp/subresult$1 | ./Aquatone/aquatone -ports large -out /tmp/aquatone$1

# Amass version
./Amass/amass -active -brute -o /tmp/hosts.txt -d $1
cat /tmp/hosts.txt | ./Aquatone/aquatone -ports large -out /tmp/aquatone$1
```

## Description

This bash script performs subdomain enumeration using both Subfinder (passive) and Amass (active brute-force) methods, then scans the results with Aquatone to generate HTML reports. It takes the target domain as a positional argument ($1) and outputs to /tmp directories. Useful as a quick one-liner automation for reconnaissance workflows.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $1 | Target domain to enumerate | example.com |

## Usage

Save as a .sh file, make executable (chmod +x script.sh), and run with ./script.sh example.com. It will create /tmp/subresultexample.com for Subfinder output and /tmp/aquatoneexample.com for reports. Use in red team ops for batch enumeration; combine outputs manually if needed for deduplication.

## Detection

- DNS query logs showing high volume to public resolvers (8.8.8.8, 1.1.1.1).
- Network traffic to target domain on non-standard ports during Aquatone scans.
- File artifacts in /tmp if executed on a monitored system.

## Related

- [[procedures/Subdomain-Enumeration-and-Scan-with-Aquatone]]
- [[tools/subfinder]]
- [[tools/amass]]
- [[tools/Aquatone]]
