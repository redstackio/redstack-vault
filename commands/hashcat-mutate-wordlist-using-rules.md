---
type: command
executor: bash
data: hashcat -a 0 $_INPUT_WORDLIST --stdout -r $_RULES_FILE > $_OUTPUT_FILE
output: |
  root@kali:~# hashcat -a 0 words.txt --stdout -r rules.txt 
  Davidson
  nosdivaD
  vidsonDa
  Davidson1985
  321Davidson
  DAVIDSON
  password
  drowssap
  sswordpa
  password1985
  321password
  PASSWORD
platforms:
  - Linux
  - Windows
tags:
  - password-cracking
  - wordlist-mutation
verified: true
validated: true
---

# hashcat-mutate-wordlist-using-rules

## Command

```bash
hashcat -a 0 $_INPUT_WORDLIST --stdout -r $_RULES_FILE > $_OUTPUT_FILE
```

## Description

This command uses Hashcat in straight attack mode (-a 0) with rules to mutate words from an input wordlist, outputting the transformations via --stdout instead of cracking hashes. It is ideal for generating password variations offline for later use in brute-force attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a 0 | Specifies straight dictionary attack mode (no mask or hybrid) | Yes |
| $_INPUT_WORDLIST | Path to the input wordlist file (e.g., words.txt) | Yes |
| --stdout | Outputs mutated words to stdout instead of performing cracking | Yes |
| -r | Specifies the rules file for mutations (e.g., rules.txt) | Yes |
| $_RULES_FILE | Path to the rules file containing transformation rules | Yes |
| > $_OUTPUT_FILE | Redirects stdout to an output file (e.g., mutated_words.txt) | Yes |

## Examples

### Basic Usage

```bash
hashcat -a 0 words.txt --stdout -r rules.txt > mutated_words.txt
```

This applies all rules in rules.txt to words.txt and saves results to mutated_words.txt.

### Advanced Usage

```bash
hashcat -a 0 passwords.txt --stdout -r best64.rules --remove-rules > expanded_passwords.txt
```

Uses a larger ruleset and removes duplicate rules for cleaner output.

## Expected Output

The command produces a list of mutated words, one per line, in the output file. For sample input 'Davidson' and 'password' with rules for reverse, rotate, append/prepend numbers, and uppercase:

```
Davidson
nosdivaD
vidsonDa
Davidson1985
321Davidson
DAVIDSON
password
drowssap
sswordpa
password1985
321password
PASSWORD
```

Success is indicated by a larger output file with varied word forms.

## Related

- [[procedures/Mutate-Wordlist-with-Hashcat-Rules]]
- [[tools/Hashcat]]
