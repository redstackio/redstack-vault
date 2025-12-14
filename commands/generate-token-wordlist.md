---
data: >-
  for i in {1..1000}; do printf '%020s' $(echo $i | tr '[:digit:]' 'a'); echo;
  done > token_wordlist.txt
tags:
  - brute-force
  - generation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.546Z'
id: d06769f3-1736-4857-93e5-87445eac4cdd
verified: false
validated: true
submitted: true
---
# generate-token-wordlist

## Command

```bash
for i in {1..1000}; do printf '%020s' $(echo $i | tr '[:digit:]' 'a'); echo; done > token_wordlist.txt
```

## Description

Generates a simple wordlist of 20-character strings for brute forcing reset tokens, simulating alphanumeric guesses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{1..1000}` | Number of guesses to generate | No (adjustable) |
| `printf '%020s'` | Pads to 20 characters | Yes |
| `> token_wordlist.txt` | Output file | Yes |

## Examples

### Basic Usage

```bash
for i in {1..1000}; do printf '%020s' $(echo $i | tr '[:digit:]' 'a'); echo; done > token_wordlist.txt
```

### Advanced Usage

```bash
# Use crunch for better: crunch 20 20 -t @@@@@@@@@@@@%%%% > tokens.txt
```

## Expected Output

File token_wordlist.txt with 1000 lines of 20-char strings.

## Related

- [[commands/curl-post-password-reset]]
