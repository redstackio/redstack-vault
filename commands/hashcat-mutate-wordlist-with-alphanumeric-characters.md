---
id: 66d0dee8-4b7d-4d06-83de-02c8fa448cd1
name: hashcat-mutate-wordlist-with-alphanumeric-characters
type: command
executor: bash
data: hashcat -a 6 --stdout $_WORDLIST ?a?a > $_MUTATED_LIST
output: |-
  root@kali:~# hashcat -a 6 --stdout words.txt ?a?a > mutated.txt
  (Generates mutated words like admin12)
created_at: '2019-10-09T18:38:08.468857+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - mutation
  - wordlist
verified: true
validated: true
---

# hashcat-mutate-wordlist-with-alphanumeric-characters

## Command

```bash
hashcat -a 6 --stdout $_WORDLIST ?a?a > $_MUTATED_LIST
```

## Description

Appends two alphanumeric chars to each word in list using combinator attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a 6 | Combinator mode | Yes |
| --stdout | Output to stdout | Yes |
| $_WORDLIST | Input list | Yes |
| ?a?a | Mask for two alphanum | Yes |
| > $_MUTATED_LIST | Output file | Yes |

## Examples

### Simple Mutation

```bash
hashcat -a 6 --stdout list.txt ?d?d > nums.txt
```

## Expected Output

Expanded wordlist with mutations.

## Related

- [[procedures/enumerate-web-cms-for-usernames-and-passwords]]
