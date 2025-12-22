---
type: procedure
description: >-
  Generate an expanded wordlist by applying mutation rules to an input wordlist
  using Hashcat's rule-based transformation capabilities.
verified: true
submitted: true
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - cryptography
  - password-cracking
commands:
  - '[[commands/hashcat-mutate-wordlist-using-rules]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Hashcat]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Mutate-Wordlist-with-Hashcat-Rules

## Summary

This procedure uses Hashcat to mutate an existing wordlist by applying a set of transformation rules, generating variations such as reversals, case changes, rotations, and appendages without performing actual hash cracking. This is useful for expanding wordlists prior to brute-force attacks on passwords, improving coverage of common user-generated passwords.

## Description

Hashcat's rule engine allows for efficient wordlist mutation using the --stdout option, which pipes transformed words to output instead of cracking hashes. This technique is particularly effective in credential access scenarios where initial wordlists (e.g., from dictionary attacks or leaked data) need augmentation with common patterns like appending years, reversing strings, or altering case. The process runs offline and is computationally lightweight compared to full brute-force, making it suitable for red team operations targeting weak passwords. It maps to MITRE ATT&CK's Brute Force technique under Credential Access, as it enhances password guessing efficiency.

## Requirements

1. Hashcat installed on a Linux or Windows system with sufficient CPU/GPU resources.
2. An input wordlist file (e.g., words.txt) containing base passwords or terms.
3. A rules file (e.g., rules.txt) defining mutation transformations.
4. Write permissions to output the mutated wordlist.
5. Basic familiarity with Hashcat syntax and rule formats.

## Defense

Defensive measures include enforcing strong password policies (length >12, no common patterns), rate-limiting login attempts, and monitoring for offline cracking tools via endpoint detection (e.g., process monitoring for hashcat.exe). Use multi-factor authentication to mitigate brute-force risks even if mutated wordlists are used.

## Objectives

1. Transform an input wordlist into a larger set of variations using predefined rules.
2. Output the mutated words to a new file for use in subsequent brute-force attempts.
3. Verify the mutations produce expected variations like case toggles and appendages.

## Instructions

### Step 1: Prepare the Input Wordlist

**Context**: Create or obtain a base wordlist with target passwords or terms. This step ensures you have a starting set of words to mutate, such as common usernames or dictionary terms.

For example, use a simple wordlist with entries like 'Davidson' and 'password':

```text
Davidson
password
```

Save this as `words.txt`. This provides the foundation for rule-based transformations.

### Step 2: Create the Mutation Rules File

**Context**: Define rules to apply transformations like reversing, rotating, appending numbers, and changing case. Reference Hashcat's rule syntax for accuracy.

First, review common Hashcat rules for guidance:

[[codes/Hashcat-Rules-Syntax-Reference]]

Then, create `rules.txt` with specific rules for the desired mutations (e.g., do nothing, reverse, rotate left twice, append '1985', prepend '123', uppercase):

[[codes/Sample-Rules-for-Wordlist-Mutation]]

Save the content as `rules.txt`. Each line represents one rule applied to every input word.

### Step 3: Execute Wordlist Mutation

**Context**: Run Hashcat in mutation mode to apply rules and generate the output wordlist. This step produces the expanded list ready for use in cracking or testing.

**Command** ([[commands/hashcat-mutate-wordlist-using-rules]]):
```bash
hashcat -a 0 $_INPUT_WORDLIST --stdout -r $_RULES_FILE > $_OUTPUT_FILE
```

Replace `$_INPUT_WORDLIST` with your input file (e.g., words.txt), `$_RULES_FILE` with rules.txt, and `$_OUTPUT_FILE` with the desired output (e.g., mutated_words.txt). This command reads the input, applies each rule, and redirects stdout to the output file.

> This generates variations for each input word based on the rules, such as 'Davidson' becoming 'DAVIDSON', 'nosdivaD', 'Davidson1985', etc. Verify by checking the output file size is larger than the input.
