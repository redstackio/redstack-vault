---
id: 8a000891-ef7a-4676-903b-4b2316bd25f7
name: Generate DNS Sub-Domain Wordlist (seclists)
type: procedure
verified: true
submitted: true
created_at: '2020-06-30T04:41:15.237461+00:00'
updated_at: '2023-05-26T00:48:26.948250+00:00'
commands:
- '[[build dns subdomain wordlist with sed]]'
---

# Generate DNS Sub-Domain Wordlist (seclists)

**Status**: ✓ Verified

## Summary

You will find it useful to build your own subdomain wordlist to brute force with tools like massdns. Once you obtain SecLists wordlist from github and un-gzip / un-tar it, run this command against your target domain to build the wordlist into your local directory. 

## Description

# Description

You will find it useful to build your own subdomain wordlist to brute force with tools like massdns.

Once you obtain SecLists wordlist from github and un-gzip / un-tar it, run this command against your target domain to build the wordlist into your local directory.

**Command** ([[build dns subdomain wordlist with sed]]):

```bash
sed 's/$/.$_TARGET_DOMAIN/' $_SECLISTS_WORDLIST > $_OUTPUT_FILE
```

## Commands Used

- [[build dns subdomain wordlist with sed]]
