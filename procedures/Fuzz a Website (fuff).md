---
id: 9c118492-f825-4577-b932-f5f0d269dd0b
name: Fuzz a Website (fuff)
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:28.857057+00:00'
updated_at: '2023-05-26T18:35:23.816769+00:00'
commands:
- '[[fuff GET Parameter Fuzzing]]'
- '[[POST Data Fuzzing]]'
---

# Fuzz a Website (fuff)

**Status**: ✓ Verified

## Summary

Use this tool to find directories on a website. fuff 

## Description

# Description

Use this tool to find directories on a website.

[fuff](https://github.com/ffuf/ffuf)

##  Instructions

1. Fuzz the directories of a domain

Existing command

2. Fuzz the GET method

**Command** ([[fuff GET Parameter Fuzzing]]):

```bash
ffuf -w /path/to/paramnames.txt -u https://target/script.php?FUZZ=test_value -fs 4242

```

3. Fuzz the POST method

**Command** ([[POST Data Fuzzing]]):

```bash
ffuf -w /path/to/postdata.txt -X POST -d "username=admin\&password=FUZZ" -u https://target/login.php -fc 401

```

## Commands Used

- [[fuff GET Parameter Fuzzing]]
- [[POST Data Fuzzing]]
