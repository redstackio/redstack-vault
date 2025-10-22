---
id: fcf61d0f-1909-4871-8dd0-6a78930a51c9
name: Brute Force Sub-Domains (gobuster)
type: procedure
verified: false
submitted: false
created_at: '2020-07-24T17:11:23.994367+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[gobuster brute force DNS from wordlist]]'
---

# Brute Force Sub-Domains (gobuster)

## Summary

You can use this tool to brute force a list of sub-domains from a master wordlist. This wordlist can be found from jhaddix gist master wordlist 

## Description

# Description

You can use this tool to brute force a list of sub-domains from a master wordlist.

This wordlist can be found from jhaddix gist

[master wordlist](https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056)

##  Instructions

1. Using gobuster to brute force a list of sub-domains from a wordlist

**Command** ([[gobuster brute force DNS from wordlist]]):

```bash
gobuster dns -d $TARGET_DOMAIN -w $WORDLIST

```

## Commands Used

- [[gobuster brute force DNS from wordlist]]
