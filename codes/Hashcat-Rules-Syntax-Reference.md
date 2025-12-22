---
type: code
language: hashcat-rules
verified: true
platforms:
  - Linux
  - Windows
tags:
  - rules
  - syntax-reference
validated: true
---

# Hashcat-Rules-Syntax-Reference

## Code

```hashcat rules
:    | do nothing
l    | Lowercase all letters
u    | Uppercase all letters
c    | Capitalize the first letter and lower the rest
C    | Lowercase first found character, uppercase the rest
t    | Toggle the case of all characters in word.
TN   | Toggle the case of characters at position N
r    | Reverse the entire word
d    | Duplicate entire word
pN   | Append duplicated word N times
f    | Duplicate word reversed
{    | Rotates the word left.
}    | Rotates the word right
$X   | Append character X to end
^X   | Prepend character X to front
[    | Deletes first character
]    | Deletes last character
DN   | Deletes character at position N
xNM  | Extracts M characters, starting at position N
ONM  | Deletes M characters, starting at position N
iNX  | Inserts character X at position N
oNX  | Overwrites character at position N with X
'N   | Truncate word at position N
sXY  | Replace all instances of X with Y
@X   | Purge all instances of X
zN   | Duplicates first character N times
ZN   | Duplicates last character N times
q    | Duplicate every character
XNMI | Insert substring of length M starting from position N of word saved to memory at position I
4    | Append the word saved to memory to current word
6    | Prepend the word saved to memory to current word
M    | Memorize current word
```

## Description

This code snippet provides a reference list of common Hashcat rule syntaxes and their effects, used for creating custom rules files to mutate wordlists. It serves as a quick lookup for transformations like case changes, reversals, and insertions during password cracking preparation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N | Position or count for operations like toggle or duplicate | 1, 2 |
| X | Character to append, prepend, insert, or replace with | 1, $, a |
| M | Length or number for extraction/deletion | 3, 5 |
| Y | Replacement character in swaps | b, ! |
| I | Memory slot index for advanced insertions | 0, 1 |

## Usage

Copy relevant rules into a .rules file for use with Hashcat's -r option in wordlist mutation procedures, such as expanding dictionaries for brute-force attacks. Combine multiple rules (one per line) to generate diverse variations.

## Detection

No direct execution; rules are input files. Detect via file analysis for .rules files containing patterns like $X or ^X in forensic investigations of cracking tools.

## Related

- [[procedures/Mutate-Wordlist-with-Hashcat-Rules]]
- [[tools/Hashcat]]
