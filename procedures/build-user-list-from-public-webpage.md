---
id: fa6098c3-25f1-437b-8c52-2310e3416a59
name: build-user-list-from-public-webpage
type: procedure
verified: true
submitted: false
created_at: '2020-03-16T04:10:19.986818+00:00'
updated_at: '2023-05-25T19:58:31.804768+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather Victim Identity Information|T1589 - Gather Victim
    Identity Information]]
sub_techniques: []
tags:
  - enumeration
  - osint
commands:
  - '[[commands/cewl-generate-wordlist-from-webpage]]'
platforms:
  - Web
tools:
  - '[[tools/CeWL]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# build-user-list-from-public-webpage

## Summary

This procedure scrapes public websites for employee names and generates common username patterns (e.g., firstlast, initials) to build a list for brute-force attacks against services like SMB.

## Description

Organizations often expose staff on 'About Us' pages, enabling OSINT-based username guessing. Common AD patterns include lowercase, capitalized, or concatenated names. This feeds into tools like CrackMapExec for validation.

## Requirements

1. Target company website URL
2. Browser or scraping tool like CeWL
3. Text editor for variations

## Defense

- Minimize employee name exposure on public sites
- Implement account lockouts after failed logins
- Use non-predictable username schemes

## Objectives

1. Collect names from public sources
2. Generate 100+ username variants
3. Prepare list for brute-force

## Instructions

### Step 1: Scrape Names

**Context**: Crawl the site for text containing potential names.

**Command** ([[commands/cewl-generate-wordlist-from-webpage]]):
```bash
cewl -d 2 -m 5 -w names.txt $_TARGET_URL
```

> -d depth, -m min length; manually curate names from output.

### Step 2: Generate Variations

**Context**: Apply patterns to each name.

No command; script or manual: for "Mary Washington" → marywashington, mwashington.

> Save to users.txt; aim for 10 variants per name.

### Step 3: Validate List

**Context**: Check for duplicates and format.

sort -u users.txt | wc -l

> Success if list is clean and diverse.
