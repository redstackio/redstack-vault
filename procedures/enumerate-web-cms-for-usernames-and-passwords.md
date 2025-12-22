---
id: 6e9efe16-04dc-4b3a-ae5e-970fff6b7a4d
name: enumerate-web-cms-for-usernames-and-passwords
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T18:38:08.566896+00:00'
updated_at: '2023-05-26T18:35:53.258433+00:00'
tactics:
  - '[[tactics/Discovery|TA0007]]'
  - '[[tactics/Credential Access|TA0006]]'
techniques:
  - '[[techniques/Brute Force|T1110.001]]'
  - '[[techniques/Account Discovery|T1087.001]]'
sub_techniques: []
tags:
  - authentication
  - brute-force
  - cms
  - wordpress
commands:
  - '[[commands/wget-crawl-web-app-recursively]]'
  - '[[commands/grep-search-files-for-keywords]]'
  - '[[commands/cewl-generate-password-list-from-website-content]]'
  - '[[commands/hashcat-mutate-wordlist-with-alphanumeric-characters]]'
  - '[[commands/wpscan-enumerate-wordpress-plugins-users-themes-timthumb]]'
platforms:
  - Web
tools:
  - '[[tools/WPScan]]'
  - '[[tools/CeWL]]'
validated: true
---

# enumerate-web-cms-for-usernames-and-passwords

## Summary

This procedure crawls a web CMS like WordPress to extract usernames, generate custom password lists from content, and identify vulnerabilities for brute-force attacks.

## Description

CMS sites often leak info in source code, comments, or configs. Crawling downloads content for keyword searches, CEWL builds wordlists from page text, mutation adds variations, and WPScan enumerates users/plugins. Combined with stego-extracted creds, this yields login pairs.

## Requirements

- Target CMS URL
- Tools: wget, grep, cewl, hashcat, wpscan
- Wordlist for mutations

## Defense

- Remove author names from posts/comments
- Use strong, unique passwords; enable CAPTCHA/2FA
- Regularly update CMS/plugins to patch enum vulns

## Objectives

- Gather usernames from CMS
- Create targeted password lists
- Identify brute-force opportunities

## Instructions

### Step 1: Recursively Crawl the Site

**Context**: Download all accessible pages/files to local dir for offline analysis.

**Command** ([[commands/wget-crawl-web-app-recursively]]):
```bash
wget --recursive --html-extension --convert-links --restrict-file-names=windows --no-parent http://$_TARGET_IP
```

> Creates local mirror; review for hidden files.

### Step 2: Search for Keywords

**Context**: Grep downloaded files for credential hints like 'password' or 'admin'.

**Command** ([[commands/grep-search-files-for-keywords]]):
```bash
grep -C 5 -iR 'password|secret|admin' *
```

> Shows context around matches.

### Step 3: Generate Custom Wordlist

**Context**: Use site content to create relevant passwords.

**Command** ([[commands/cewl-generate-password-list-from-website-content]]):
```bash
cewl $_TARGET_IP -d 2 -m 5 -w passwords.txt
```

> Depth 2 crawls links; min word size 5.

### Step 4: Mutate Wordlist

**Context**: Append common suffixes/prefixes for variations.

**Command** ([[commands/hashcat-mutate-wordlist-with-alphanumeric-characters]]):
```bash
hashcat -a 6 --stdout passwords.txt ?a?a > mutated_passwords.txt
```

> ?a?a adds two alphanumeric chars.

### Step 5: Enumerate CMS Users and Plugins

**Context**: Target WordPress specifically for users/themes.

**Command** ([[commands/wpscan-enumerate-wordpress-plugins-users-themes-timthumb]]):
```bash
wpscan --url http://$_TARGET_IP --enumerate p,t,u,tt
```

> Lists users like 'admin'; check for vulns.
