---
url: null
tags:
  - demo
  - video
  - rce
type: tool
platforms:
  - Windows
description: Video showing remote code execution
id: 674808e9-79f0-4718-9b22-76191d902db2
created_at: '2025-12-11T06:10:22.804Z'
updated_at: '2025-12-11T06:10:22.804Z'
verified: false
validated: true
submitted: true
---
# ubiq_rce.mp4

**Status**: Unverified

## Overview

Video demonstrating RCE by launching calc.exe from a webpage.

## Description

Illustrates remote exploit using JavaScript payload.

## Features

- Visual RCE proof
- Step-by-step remote attack

## Installation

N/A (media file)

## Basic Usage

Play the video.

## Examples

N/A

## MITRE ATT&CK Mapping

N/A

## Detection

N/A

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/rce0923234.html]]

## References

- HackerOne report
