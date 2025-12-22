---
id: ba99d31a-2f1f-49f2-88d2-58307d7660af
type: tool
verified: true
created_at: '2019-08-28T21:17:38.147060+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Unix
tags:
  - dns
  - reconnaissance
  - zone-transfer
url: 'https://sourceforge.net/projects/dnswalk/'
commands:
  - '[[commands/dnswalk-basic-zone-transfer]]'
  - '[[commands/dnswalk-fast-mode-transfer]]'
  - '[[commands/dnswalk-check-consistency]]'
validated: true
---

# dnswalk

**Status**: Unverified

## Overview

Dnswalk is a DNS debugging and enumeration tool primarily used for performing zone transfers on specified domains. It walks the DNS namespace, retrieves records via AXFR if permitted, and performs checks for internal consistency and accuracy. Commonly used in reconnaissance phases of security assessments to map DNS infrastructure.

## Description

Dnswalk, written in Perl, attempts to transfer the entire zone from authoritative name servers and validates the data against various rules, such as proper NS record glue, consistent TTLs, and absence of loops. It's particularly useful for identifying misconfigurations in DNS setups that could lead to information disclosure. While older, it remains relevant for legacy systems or environments where zone transfers are not properly restricted.

## Features

- Feature 1: Zone transfer via AXFR to enumerate all DNS records (A, MX, NS, CNAME, etc.)
- Feature 2: Consistency checks for DNS database integrity, including loop detection and missing records
- Feature 3: Fast mode for quicker scans and check-only mode for validation without full walks
- Feature 4: Reporting of errors, warnings, and OK statuses for each checked element

## Installation

### Requirements

- Perl 5 (with standard libraries)
- Network access to DNS servers (UDP/TCP port 53)

### Install Commands

```bash
# On Ubuntu/Debian (may require building from source as it's not in standard repos)
git clone https://github.com/dnswalk/dnswalk.git  # Or download from SourceForge
cd dnswalk
perl Makefile.PL
make
make install

# Alternative: If available in repos (older versions)
# apt-get install dnswalk
```

For Kali Linux, it may be available via apt or can be installed from source as above.

## Basic Usage

```bash
dnswalk --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -f | Fast mode: Skip some checks for speed |
| -c | Check mode: Validate consistency without full transfer |
| -a | All checks: Perform comprehensive validation |
| -d level | Set debug level (1-3) |

## Examples

### Example 1: Basic Usage

```bash
dnswalk example.com
```

This performs a standard zone walk and basic checks.

### Example 2: Advanced Usage

```bash
dnswalk -f -c example.com
```

Fast check mode for quick consistency validation.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Search Open Websites-Domains]] Search Open Technical Databases (DNS enumeration via zone transfers)
- [[Network Service Scanning]] Network Service Scanning (probing DNS services)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual AXFR requests to authoritative DNS servers (log DNS queries for large transfers)
- Detection method 2: Perl process spawning with network connections to port 53
- Detection method 3: Failed zone transfer attempts in DNS server logs (e.g., BIND's query log showing REFUSED responses)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[dig]]
- [[nslookup]]
- [[tools/dnsenum]]

## References

- Official SourceForge project: https://sourceforge.net/projects/dnswalk/
- GitHub mirror: https://github.com/fabrice-lear/monthly-dnswalk
- DNS Zone Transfer Security: https://www.isc.org/bind/ (for defense context)
