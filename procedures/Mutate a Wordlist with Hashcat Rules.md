---
id: cf7ea112-750b-467d-a340-2902086bf4c2
name: Mutate a Wordlist with Hashcat Rules
type: procedure
verified: true
submitted: true
created_at: '2019-10-18T00:15:53.265299+00:00'
updated_at: '2023-05-26T00:50:42.580511+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
platforms:
- Linux
- Windows
tags:
- '[[Cryptography]]'
- '[[password cracking]]'
commands:
- '[[Hashcat Mutate a Wordlist Using Rules]]'
---

# Mutate a Wordlist with Hashcat Rules

**Status**: ✓ Verified

## Summary

Hashcat not only can be used to brute force crack hashes, it can also take an initial wordlist, mutate it with rules, and output the result using the --stdout option. 

## Description

# Description

Hashcat not only can be used to brute force crack hashes, it can also take an initial wordlist, mutate it with rules, and output the result using the `--stdout` option. 



# Instructions

For this example, a wordlist will be built that includes:

- the original word

- the word backwards

- the word rotated left twice

- the word with '1985' appended

- the word with 123 prepended

- the word in all uppercase

words.txt will contain two words





**Code**: [[Davidson
password
]]





Use the following table to build the `rules.txt` file.



**Code**: [[:    | do nothing
l    | Lowercase all letters
u  ]]





Given the requirements, create a rules.txt file with the following contents:





**Code**: [[:
r
{{
$1$9$8$5
^1^2^3
u]]





Mutate the list and output the results to a new file





**Command** ([[Hashcat Mutate a Wordlist Using Rules]]):

```bash
hashcat -a 0 words.txt --stdout -r rules.txt > $_OUTPUT.txt
```





## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[Hashcat Mutate a Wordlist Using Rules]]

## Tags

- [[Cryptography]]
- [[password cracking]]


