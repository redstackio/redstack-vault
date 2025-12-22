---
id: e884f63a-2ed0-4287-9174-a25c497edaa0
name: linux-shadow-hash-type-identifiers
type: code
language: text
verified: true
created_at: '2020-01-20T20:42:02.725903+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - hash-identification
  - cryptography
validated: true
---

# linux-shadow-hash-type-identifiers

## Code

```text
$1$ – MD5
$2a$ – Blowfish
$2y$ – Eksblowfish
$5$ – SHA-256
$6$ – SHA-512
```

## Description

This reference list identifies common hashing algorithms used in Linux /etc/shadow files based on the prefix format. Each entry maps the identifier (e.g., $6$) to the algorithm name, helping determine the appropriate Hashcat mode for cracking.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | Static reference list; no variables | N/A |

## Usage

Consult this list when extracting hashes from /etc/shadow to quickly identify the type before using tools like Hashcat. Embed in documentation or scripts for automated hash parsing in red team tools.

## Detection

Not applicable as this is a reference, not executable code. Defenders should focus on access logs to /etc/shadow rather than this identifier list.

## Related

- [[procedures/Brute-Force-Shadow-Hashes]]
- [[tools/Hashcat]]
