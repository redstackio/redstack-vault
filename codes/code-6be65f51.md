---
id: 6be65f51-f4ca-4d8f-a7ac-90da1bb69581
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:17.585903+00:00'
updated_at: '2023-04-06T03:56:17.600128+00:00'
---

# Code Snippet 6be65f51

**Language**: Bash

```bash
# Run on password file containing hashes to be cracked
john passwd

# Use a specific wordlist
john --wordlist=<wordlist> passwd

# Use a specific wordlist with rules
john --wordlist=<wordlist> passwd --rules=Jumbo

# Show cracked passwords
john --show passwd

# Restore interrupted sessions
john --restore
```
