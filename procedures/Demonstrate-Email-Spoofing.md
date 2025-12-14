---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - email-spoofing
  - phishing
  - smtp
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Email
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:30:59.004Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Demonstrate Email Spoofing

## Summary

This procedure simulates sending a spoofed email from a target domain to illustrate how missing DMARC allows impersonation without authentication failure enforcement.

## Description

Attackers exploit absent DMARC policies to forge From headers, making phishing emails appear from trusted sources like scott@paragonie.com. In this case, the demonstration targets external receivers (e.g., Gmail, Yahoo) where the email passes delivery but fails auth checks, yet isn't quarantined due to no DMARC policy. Prerequisites include an SMTP client; outcomes show potential for social engineering despite the company's GPG preference.

## Requirements

1. SMTP access (e.g., via Mailjet or local client like swaks)
2. Target domain with weak auth (e.g., no DMARC)
3. Receiver email address for testing (e.g., abcd@example.com)

## Defense

Defensive measures and detection strategies:

- Implement DMARC with strict policies
- Train users on GPG verification over headers
- Monitor email logs for anomalous From domains

## Objectives

1. Forge and send email with spoofed sender
2. Validate delivery and auth failure on receiver side
3. Demonstrate phishing enablement

## Instructions

### Step 1: Forge Email Headers

**Context**: Set up the email with a spoofed From address to bypass basic checks.

Use an SMTP tool or client to compose an email with From: scott@paragonie.com, subject, and body.

> No specific command; in tools like Thunderbird or Python's smtplib, override the From header. Ensure the sending server allows relaying.

### Step 2: Send and Verify

**Context**: Deliver the email and inspect receiver headers for auth results.

Send to abcd@example.com and check the received email's headers (e.g., in Gmail, show original).

> Expected: Authentication-Results show SPF/DKIM pass/fail, but no DMARC rejection, allowing display as legitimate.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- spoofing
- phishing-demo
- email-auth-bypass
