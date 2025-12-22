---
id: e0e0534d-9f84-4fd5-abea-0829e874617e
name: generate-subdomain-permutations-with-altdns
type: command
executor: bash
data: >-
  WORDLIST_PERMUTATION="./altdns/words.txt"

  python ./altdns/altdns.py -i $_INPUT_FILE -o $_OUTPUT_FILE -w
  $WORDLIST_PERMUTATION
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - recon
  - subdomain-enum
verified: true
validated: true
---

# generate-subdomain-permutations-with-altdns

## Command

```bash
WORDLIST_PERMUTATION="./altdns/words.txt"
python ./altdns/altdns.py -i $_INPUT_FILE -o $_OUTPUT_FILE -w $WORDLIST_PERMUTATION
```

## Description

Generates permutations of subdomains by combining a wordlist with input domains. Run from the directory containing the altdns folder after installation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INPUT_FILE | Path to file with target domains (one per line, e.g., inputdomains.txt) | Yes |
| $_OUTPUT_FILE | Path to output file for generated permutations (e.g., output_permutations.txt) | Yes |
| -i | Input file flag | Built-in |
| -o | Output file flag | Built-in |
| -w | Wordlist file flag | Built-in |

## Examples

### Basic Usage

```bash
WORDLIST_PERMUTATION="./altdns/words.txt"
python ./altdns/altdns.py -i inputdomains.txt -o output_permutations.txt -w $WORDLIST_PERMUTATION
```

### Advanced Usage

For Python 2.7 compatibility: replace `python` with `python2.7`. Use absolute paths for files if running remotely.

## Expected Output

No console output during generation; check the output file:
$ head output_permutations.txt
www.target.com
target.com.www
admin.target.com
target.com.admin
...

File will contain 1000s of lines based on input sizes.

## Related

- [[procedures/Subdomain-Enumeration-using-AltDNS]]
- [[commands/install-altdns]]
