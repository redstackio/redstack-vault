---
id: 9b5efbf6-8e16-43ec-ba11-3d0238792b54
name: Brute-Force-Firefox-Master-Password-with-Wordlist
type: code
language: bash
verified: true
created_at: '2020-03-16T08:31:22.043770+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - brute-force
  - credential-access
validated: true
---

# Brute-Force-Firefox-Master-Password-with-Wordlist

## Code

```bash
for guess in $(cat $_WORDLIST); do echo $guess | python firefox_decrypt/firefox_decrypt.py .mozilla/firefox  2>&1 | grep 'Username:' -A 1; done
```

## Description

This Bash script automates brute-forcing the Firefox master password by iterating through a wordlist, piping each guess to the firefox_decrypt tool, and checking for successful decryption via grep on username output. It is used when the master password is unknown but a wordlist of potential passwords is available.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_WORDLIST | Path to the wordlist file containing password guesses | /usr/share/wordlists/rockyou.txt |

## Usage

Run this script in a terminal after installing firefox_decrypt and navigating to the directory with the target profile (e.g., cd ~). It processes each wordlist entry sequentially, stopping implicitly on success when credentials are output. Suitable for offline cracking in post-exploitation where profile files have been exfiltrated.

## Detection

- Monitor for repeated executions of python processes invoking firefox_decrypt.py, especially with piped input from wordlists.
- File access logs showing multiple reads of logins.json or key4.db in profile directories.
- High CPU usage from grep and loop iterations on compromised hosts.

## Related

- [[procedures/Extract-Firefox-and-Thunderbird-Passwords-from-Profiles]]
- [[tools/firefox-decrypt]]
