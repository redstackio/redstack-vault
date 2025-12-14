---
id: tool-gitsploit-927413
url: 'https://github.com/arthaudtz/gitsploit'
tags:
  - github
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.561Z'
validated: true
submitted: true
---
# gitSploit

**Status**: Unverified

## Overview

gitSploit finds and exploits GitHub repo vulns, scanning Zomato for 10 issues.

## Description

Ruby framework for GitHub vuln hunting.

## Features

- Feature 1: Pattern matching
- Feature 2: Exploit modules
- Feature 3: Repo search

## Installation

### Requirements

- Ruby

### Install Commands

```bash
gem install gitsploit
```

## Basic Usage

```bash
gitsploit --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `search` | Query repos |
| `--exploit` | Show exploits |

## Examples

### Example 1: Basic Usage

```bash
gitsploit search zomato
```

### Example 2: Advanced Usage

```bash
gitsploit search zomato --type xss
```

## MITRE ATT&CK Mapping

### Techniques

- [[Hardware]]

### Tactics

- [[Discovery]]

## Detection

- GitHub API abuse

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools


## References

- GitHub repo
