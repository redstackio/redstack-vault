---
id: 1fb3f3c2-a7d2-4008-be6a-e55b1fff2704
name: Hashcat-Mask-Character-Definitions
type: code
language: text
verified: true
created_at: '2020-03-17T05:51:53.413466+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - hashcat
  - mask
  - brute force
validated: true
---

# Hashcat-Mask-Character-Definitions

## Code

```
l | abcdefghijklmnopqrstuvwxyz
u | ABCDEFGHIJKLMNOPQRSTUVWXYZ
d | 0123456789
h | 0123456789abcdef
H | 0123456789ABCDEF
s | ! "#$%&'()*+,-./:;<=>?@[\]^_`{|}~
a | ?l?u?d?s
b | 0x00 - 0xff
```

## Description

This reference table defines Hashcat's built-in mask symbols for character sets used in brute-force attacks. Each symbol (?l, ?u, etc.) represents a specific set of characters, allowing precise control over password generation patterns without custom rules files.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | This is a static reference table; no runtime variables | N/A |

## Usage

Consult this table when constructing masks for wordlist generation or direct cracking. For instance, in a procedure like [[procedures/Generate-Wordlist-Using-Mask-Hashcat]], use ?d for the first position to limit to digits (0-9). Combine symbols like ?a for versatile alphanumeric positions. Save as a markdown note for quick lookup during engagements.

## Detection

N/A - This is a documentation snippet, not executable code. Detection applies to Hashcat usage itself (e.g., process monitoring for hashcat.exe, high GPU load during mask-based attacks).

## Related

- [[procedures/Generate-Wordlist-Using-Mask-Hashcat]]
- [[commands/hashcat-generate-wordlist-mask]]
