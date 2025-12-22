---
type: code
language: hashcat-rules
verified: true
platforms:
  - Linux
  - Windows
tags:
  - rules
  - mutation-example
validated: true
---

# Sample-Rules-for-Wordlist-Mutation

## Code

```hashcat rules
:
r
{{
$1$9$8$5
^1^2^3
u
```

## Description

This code snippet defines a sample set of Hashcat rules for mutating wordlists: do nothing (:), reverse (r), rotate left twice ({{), append '1985' ($1$9$8$5), prepend '123' (^1^2^3), and uppercase (u). It demonstrates basic transformations to generate common password variations like birth years or reversals.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static ruleset; no runtime variables. Customize by editing lines for different appendages or operations. | N/A |

## Usage

Save as rules.txt and use with Hashcat's -r flag in mutation commands, e.g., to expand a wordlist with reversed and numbered variants for credential testing. Apply to base words like usernames or dictionary terms.

## Detection

Rules files are plain text; detect through keyword searches for patterns like $1$9$8$5 (year appends) in system files during incident response.

## Related

- [[procedures/Mutate-Wordlist-with-Hashcat-Rules]]
- [[commands/hashcat-mutate-wordlist-using-rules]]
