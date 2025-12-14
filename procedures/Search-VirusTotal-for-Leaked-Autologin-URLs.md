---
id: proc-search-vt-leaked-urls
tags:
  - information-disclosure
  - credential-leak
  - virustotal
type: procedure
tools:
  - '[[tools/VirusTotal]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Search Open Websites-Domains]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:33:06.427Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Search Open Websites-Domains]]'
  - '[[Unsecured Credentials]]'
---
# Search-VirusTotal-for-Leaked-Autologin-URLs

## Summary

This procedure outlines how to use VirusTotal to search for and identify leaked autologin URLs containing sensitive credentials for web applications like Chaturbate, enabling attackers to extract usernames and hashed passwords for potential account takeover.

## Description

Attackers leverage VirusTotal's public URL indexing, which aggregates data from shared links, emails, and web crawls, to discover endpoints that inadvertently expose credentials. In the Chaturbate case, autologin URLs designed for email-based logins include usernames and SHA1-hashed passwords in query parameters. These URLs become publicly discoverable if users share email links or if they are indexed by scanners. The procedure involves domain searching on VirusTotal, reviewing associated URLs, and extracting the credentials. Prerequisites include a VirusTotal account for full access, though basic searches are free. Expected outcomes are lists of vulnerable URLs leading to offline hash cracking.

## Requirements

1. Internet access and a web browser
2. VirusTotal account (free tier sufficient for domain searches)
3. Basic understanding of URL query parameters and hashing (e.g., SHA1)

## Defense

Defensive measures and detection strategies:

- Implement URL parameter stripping or token-based auth instead of embedding credentials
- Use HTTPS and referer checks to prevent indexing
- Monitor VirusTotal and similar services for domain mentions
- Enforce strong hashing (e.g., bcrypt) and rate-limiting on logins

## Objectives

1. Discover indexed sensitive URLs for the target domain
2. Extract embedded credentials for further exploitation
3. Enable account takeover via hash cracking

## Instructions

### Step 1: Perform Domain Search on VirusTotal

**Context**: Initiate reconnaissance by querying VirusTotal for the target domain to retrieve associated URLs.

Navigate to https://www.virustotal.com and enter the domain (e.g., chaturbate.com) in the search bar. Select the "Domain" tab and review the "Relations" section for linked URLs.

> This step uncovers publicly shared or indexed endpoints without executing any code.

### Step 2: Identify and Extract Autologin URLs

**Context**: Filter and analyze the URL list for patterns indicating credential exposure.

Look for URLs matching patterns like /accounts/autologin/?username=...&password=.... Manually copy the full URL, including query parameters, to extract the username and hashed password.

Example extracted URL: https://chaturbate.com/accounts/autologin/?username=aman4aman&password=Sha1$f5b91$0d6c2c053145a088373344d6fa08e97ce31312c6&next=/accounts/stopemails/

> Parse the 'username' for the account name and 'password' for the SHA1 hash. Save for cracking with tools like Hashcat using common wordlists.

### Step 3: Validate Credential Usability

**Context**: Assess the extracted data for exploitability.

Verify the hash format (e.g., SHA1) and attempt offline cracking. If successful, test login on the target site.

> Success is indicated by a cracked plaintext password allowing account access.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Credential Access]] Credential Access

### Techniques

- [[Search Open Websites-Domains]] Search Open Technical Databases
- [[Unsecured Credentials]] Unprotected Credentials

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files

## Commands Used


## Tools Used

- [[tools/VirusTotal]]

## Tags

- [[information-disclosure]]
- [[credential-leak]]
- [[tools/VirusTotal]]
