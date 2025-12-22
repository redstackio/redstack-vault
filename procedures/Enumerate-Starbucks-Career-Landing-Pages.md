---
tags:
  - reconnaissance
  - web-enumeration
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:52:33.765Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 94f4304d-e342-46ed-b107-2eed23340125
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Enumerate-Starbucks-Career-Landing-Pages

## Summary

This procedure involves manually browsing and enumerating the career landing pages on the Starbucks Singapore website to identify pages with comment sections that show signs of prior compromise, such as spam redirects, indicating potential XSS vulnerabilities.

## Description

In a web vulnerability assessment, start by exploring the target's public-facing pages to map the attack surface. For Starbucks Singapore, focus on the careers section where user comments are allowed. Visiting pages like career-landing-1 to career-landing-6 reveals existing spam comments redirecting to external WordPress sites, confirming inadequate input validation. This step sets the stage for targeted exploitation without requiring automated tools.

## Requirements

1. Web browser with internet access
2. Knowledge of the target URL structure (e.g., https://www.starbucks.com.sg/careers/career-center/)
3. No authentication or special permissions needed

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to monitor unusual page visits
- Regularly audit comment sections for spam or anomalous content
- Use content security policy (CSP) to restrict script execution

## Objectives

1. Discover pages with interactive comment features
2. Identify indicators of weak sanitization (e.g., existing redirects)
3. Prepare for payload injection on confirmed targets

## Instructions

### Step 1: Navigate to Career Section

**Context**: Access the base careers directory to understand the page structure.

Open a web browser and visit https://www.starbucks.com.sg/careers/career-center/.

> This loads the career center overview; note any links to individual landing pages.

### Step 2: Browse Specific Landing Pages

**Context**: Systematically visit enumerated pages to check for comment sections.

Manually append page numbers: visit https://www.starbucks.com.sg/careers/career-center/career-landing-1, then -2, up to -6.

> Observe page content; look for 'Leave a Comment' sections and scan existing comments for redirects to external sites like WordPress blogs.

### Step 3: Document Findings

**Context**: Record vulnerable pages for follow-up exploitation.

Note URLs with active comment forms and any pre-existing spam.

> Successful enumeration yields a list of 6 pages, all showing vulnerability signs.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[web-enumeration]]
