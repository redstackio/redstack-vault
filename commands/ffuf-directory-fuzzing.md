---
type: command
executor: bash
data: >
  ffuf -w /usr/share/wordlists/dirb/common.txt -u https://target.com/FUZZ -fs
  324
output: null
tags:
  - fuzzing
  - directory-enumeration
platforms:
  - Linux
  - Web
created_at: '2020-07-24T17:11:28.829249+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
verified: true
validated: true
---

# ffuf-directory-fuzzing

## Command

```bash
ffuf -w /usr/share/wordlists/dirb/common.txt -u https://target.com/FUZZ -fs 324
```

## Description

This command uses ffuf to brute-force common directory names on a target website, helping to discover hidden directories or files during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -w | Path to the wordlist file containing directory names | Yes |
| -u | Base URL with FUZZ placeholder for the directory path | Yes |
| -fs | Filter out responses of a specific size (e.g., default 404 page) | No |
| FUZZ | Placeholder in the URL for wordlist substitutions | Yes |

## Examples

### Basic Usage

```bash
ffuf -w /usr/share/wordlists/dirb/common.txt -u https://example.com/FUZZ
```

### Advanced Usage

```bash
ffuf -w custom_dirs.txt -u https://target.com/FUZZ/ -fs 324 -t 50
```

## Expected Output

```
        /'___\/___\
       /\      /\ 
      /  \    /  \      /'___\\      ___ \\    ___   ___    /\ \//
     / /\ \  / /\ \    /\  _ `\    / /   \\  / / `\ / / `\ \ \ \/
    / /  \`\/ / /  \ \  /\ \ \ \_ / /     \\ / /   / /   /  \_\ \
   / /   / /\/ /    \ \/ / `\\_\\\/ /   /\ \\/ /   / /   / /\____ \
  / /___/ /   /      \  / / /_ / /\ \_/  \ \/\ \_/ / /   /  \  _ \ \
  \(\____/   /        \/ / /\ \  \  \____/\/\  \___/ /   /\___/ / /
   \ \__/   /         \ \/ /  \ \  /      /  \ \__/  \___/  \/____/ 
    \_____/           \____/    \_\/       /   \_____/ 

admin                [Status: 200, Size: 1234, Words: 56]
backup               [Status: 403, Size: 567, Words: 12]
...
```

A table of discovered paths with status codes, sizes, and word counts. Valid directories often return 200 or 301/302.

## Related

- [[procedures/Directory-and-Parameter-Fuzzing-with-Ffuf]]
- [[tools/Ffuf]]
