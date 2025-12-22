---
id: d2e73ae8-6c06-44ca-83de-3d9cb9cca0e1
type: tool
verified: true
created_at: '2019-08-28T21:17:43.026877+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - phishing
  - homograph
  - idn
  - generation
  - detection
url: 'https://github.com/securitygeneration/EvilURL'
category: Social Engineering
validated: true
---

# EvilURL

**Status**: Unverified

## Overview

EvilURL is a specialized tool for generating and detecting Unicode-based evil domains used in Internationalized Domain Name (IDN) homograph attacks. It helps red teams create realistic phishing domains that visually mimic legitimate ones and defenders identify suspicious domains by spotting non-Latin characters that resemble ASCII ones.

## Description

IDN homograph attacks exploit the similarity between Unicode characters from different scripts (e.g., Cyrillic 'а' looking like Latin 'a') to register domains that fool users into visiting malicious sites. EvilURL automates the generation of such domains by replacing characters in a target domain with visually similar Unicode variants. It also includes detection capabilities to analyze a domain and report if it's likely a homograph. Commonly used in phishing campaigns, social engineering tests, and domain security audits.

## Features

- Feature 1: Generate homograph domains by substituting characters with Unicode lookalikes from various scripts (Cyrillic, Greek, etc.).
- Feature 2: Detect and decode evil domains, highlighting malicious characters and suggesting legitimate equivalents.
- Feature 3: Output to files for batch processing and integration with other tools like DNS registrars or phishing kits.
- Feature 4: Support for partial homographs (e.g., only subdomain or TLD altered).

## Installation

### Requirements

- Perl 5 (pre-installed on most Linux distributions)
- Git

### Install Commands

```bash
# Clone the repository
git clone https://github.com/securitygeneration/EvilURL.git
cd EvilURL

# Make executable (if needed)
chmod +x evilurl.pl

# For Kali/Ubuntu: No additional packages needed if Perl is installed
# Verify: perl --version
```

On macOS, use Homebrew for Perl if not present: `brew install perl`.

## Basic Usage

```bash
perl evilurl.pl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -g, --generate | Generate evil domains from a base domain |
| -d, --detect | Detect if a domain is a homograph |
| -o, --output | Specify output file |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage (Generate)

```bash
perl evilurl.pl -g example.com
```

### Example 2: Advanced Usage (Detect)

```bash
perl evilurl.pl -d xn--xample-9ua.com -o detection_report.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1566.002]] Phishing: Spearphishing Link
- [[Drive-by Compromise]] Drive-by Compromise

### Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Perl script executions involving domain generation patterns (e.g., via process monitoring tools like Sysmon).
- Detection method 2: Network logs showing bulk DNS queries for Unicode domains during testing.
- Detection method 3: File system artifacts like evilurl.pl or generated domain lists in temp directories.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: DNSTwist]] (Alternative homograph generator)
- [[Related Tool: GoPhish]] (Phishing framework integration)

## References

- Official GitHub: https://github.com/securitygeneration/EvilURL
- IDN Homograph Attack Explanation: https://www.owasp.org/index.php/Internationalization_(I18N)_(OWASP-WS-009)
