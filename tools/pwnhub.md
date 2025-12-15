---
id: tool-uuid-456
url: 'https://github.com/nikitastupin/pwnhub'
tags:
  - github-actions
  - exploitation
  - learning-resource
type: tool
verified: false
platforms:
  - Cloud
  - GitHub
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.558Z'
validated: true
submitted: true
---
---

# pwnhub

**Status**: Unverified

## Overview

Pwnhub is a GitHub repository serving as an educational resource for understanding and exploiting vulnerabilities in GitHub Actions and related CI/CD pipelines. It includes examples, write-ups, and code snippets for common misconfigurations like improper access controls, making it useful for security researchers testing supply chain attacks.

## Description

Developed by Nikita Stupin, pwnhub aggregates real-world exploits and defensive guidance for GitHub's automation features. It's particularly relevant for scenarios involving unauthorized workflow executions, secret exfiltration, and package tampering, as seen in projects like Hyperledger Iroha. Users can clone the repo to study PoCs, adapt them for pentesting, or contribute new findings. No installation required beyond Git; it's a static resource for offensive security learning.

## Features

- Feature 1: Curated collection of GitHub Actions vulnerability PoCs and explanations
- Feature 2: Guides on workflow permissions, token handling, and fork/PR attacks
- Feature 3: References to HackerOne reports and bounty programs for real-world context

## Installation

### Requirements

- Git installed
- GitHub account for cloning

### Install Commands

```bash
# Clone the repository
git clone https://github.com/nikitastupin/pwnhub.git
cd pwnhub
```

## Basic Usage

```bash
ls pwnhub/
cat pwnhub/examples/actions-exfil.md
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | As a resource repo, no CLI options; browse Markdown files |

## Examples

### Example 1: Basic Usage

```bash
cd pwnhub
open README.md  # Or use cat/grep to search for specific vulns
```

### Example 2: Advanced Usage

```bash
grep -r "secrets exfiltration" pwnhub/
# Review matching files for exploit patterns
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Compromise Hardware Supply Chain]]
- [[Credentials In Files]]

### Tactics

- [[Initial Access]]
- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Git clone activity to the pwnhub repo in logs
- References to pwnhub examples in attack workflows or PR descriptions
- Anomalous GitHub Actions runs matching pwnhub PoCs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- GitHub CLI (gh)
- Semgrep for static analysis

## References

- Official repository: https://github.com/nikitastupin/pwnhub
- Related resources: GitHub Docs on Actions security

---
