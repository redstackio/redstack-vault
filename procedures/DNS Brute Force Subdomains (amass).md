---
id: e36a27d8-7a78-4697-b41b-25d452eabd09
name: DNS Brute Force Subdomains (amass)
type: procedure
verified: false
submitted: false
created_at: '2020-07-02T15:08:27.021843+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[amass active dns brute force enumeration w/ DB]]'
- '[[amass dns brute force subdomains]]'
---

# DNS Brute Force Subdomains (amass)

## Summary

You can brute force subdomains with the built in brute force flag, or you can supply a wordlist. 

## Description

## Description

You can brute force subdomains with the built in brute force flag, or you can supply a wordlist.







**Command** ([[amass dns brute force subdomains]]):

```bash
amass enum -ip -brute -d $_TARGET_DOMAIN
```





This command attempts to resolve and verify the results because of the active flag. It specifies a wordlist included with Kali, and specifies both an output directory for the graph db and logs and an output results file containing just the results.







**Command** ([[amass active dns brute force enumeration w/ DB]]):

```bash
amass enum -active -d $_TARGET_DOMAIN -brute -w $_WORDLIST -src -ip -dir $_OUTPUT_DIR -o $_OUTPUT_RESULTS_FILE
```





## Commands Used

- [[amass active dns brute force enumeration w/ DB]]
- [[amass dns brute force subdomains]]


