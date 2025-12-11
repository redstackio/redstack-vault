---
url: 'https://docs.gitlab.com/ee/user/project/wiki/'
tags:
  - gitlab
  - wiki
type: tool
platforms:
  - Web
  - GitLab
description: Wiki feature in GitLab for documentation
id: 458815e4-f41a-4803-8cb2-b30b62bb6e21
created_at: '2025-12-11T06:10:29.091Z'
updated_at: '2025-12-11T06:10:29.091Z'
verified: false
validated: true
submitted: true
---
# GitLab Wiki

**Status**: Unverified

## Overview

GitLab Wiki allows creating pages with commit messages, exploited here to control content for injections.

## Description

Integrated wiki system backed by Git, vulnerable when combined with API flaws.

## Features

- Feature 1: Page creation
- Feature 2: Version history
- Feature 3: Markdown support

## Installation

### Requirements

- GitLab instance

### Install Commands

N/A (built-in)

## Basic Usage

Access via GitLab UI.

### Common Options

N/A

## Examples

### Example 1: Basic Usage

Create page via web interface.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Wiki edit logs
- Detection method 2: Suspicious commit messages

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Confluence]]

## References

- Official documentation: https://docs.gitlab.com/ee/user/project/wiki/
