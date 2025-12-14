---
url: null
tags:
  - email
  - smtp
type: tool
platforms:
  - Linux
description: Command-line tool for sending emails directly from files.
id: 9198f083-3c0f-4664-ba57-228aa84ebfaf
created_at: '2025-12-14T00:11:16.807Z'
updated_at: '2025-12-14T00:11:16.807Z'
verified: false
validated: true
submitted: true
---
# sendmail

**Status**: Unverified

## Overview

Sendmail is a mail transfer agent used for sending emails from the command line, particularly useful for delivering raw formatted messages in security testing scenarios like bypassing email sanitizers.

## Description

It reads email content from stdin or files and sends it via SMTP. In offensive security, it's employed to send crafted emails without client-side alterations, as seen in exploits targeting webmail services.

## Features

- Feature 1: Sends raw email content
- Feature 2: Extracts recipients from headers
- Feature 3: Supports custom sender addresses

## Installation

### Requirements

- Linux system
- Sendmail package installed (usually pre-installed)

### Install Commands

```bash
sudo apt install sendmail
```

## Basic Usage

```bash
sendmail --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-t` | Read recipients from message |
| `-f` | Set sender address |

## Examples

### Example 1: Basic Usage

```bash
/usr/sbin/sendmail -t < email.txt
```

### Example 2: Advanced Usage

```bash
/usr/sbin/sendmail -t -f attacker@example.com < email.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for sendmail process execution
- Detection method 2: Log unusual email sending patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation
- Related resources
