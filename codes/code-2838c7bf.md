---
id: 2838c7bf-3c26-4a39-8842-32ecc2214afb
type: code
language: Hashcat Rules
verified: false
created_at: '2020-03-16T08:02:51.110310+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 2838c7bf

**Language**: Hashcat Rules

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
