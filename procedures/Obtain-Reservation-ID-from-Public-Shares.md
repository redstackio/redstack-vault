---
tags:
  - recon
  - idor
  - social-media
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:30:35.088Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a815c7be-1e32-4b7e-9e23-d465edc90e28
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Obtain-Reservation-ID-from-Public-Shares

## Summary

This procedure involves gathering reservation IDs from publicly shared Yelp reservation URLs on social media platforms, which expose sensitive identifiers without proper access controls.

## Description

In the context of Yelp's IDOR vulnerability, users often share reservation confirmation links on social media, embedding the reservation ID in the URL. Attackers can search for these shares to obtain valid IDs, setting the stage for unauthorized actions. This step requires no technical tools beyond a web browser and relies on open-source intelligence (OSINT) from public posts. Expected outcome is a list of harvestable IDs for further exploitation.

## Requirements

1. Access to social media search (e.g., Twitter, Facebook)
2. Web browser for URL inspection
3. Basic understanding of URL parameters

## Defense

Defensive measures and detection strategies:

- Educate users not to share reservation links publicly
- Monitor social media for leaked IDs and notify affected users
- Implement ID obfuscation or short-lived tokens in shared links

## Objectives

1. Collect valid reservation IDs for targeting
2. Identify exposed bookings for potential disruption
3. Enable follow-on IDOR exploitation

## Instructions

### Step 1: Search for Shared Reservations

**Context**: Use social media search to find posts containing Yelp reservation links.

Search queries like "Yelp reservation confirmation" or "booked at [restaurant] via Yelp" on platforms such as Twitter. Review results for URLs like https://yelp.com/reservations/confirm?id=12345.

### Step 2: Extract the ID

**Context**: Parse the URL to isolate the reservation ID parameter.

From the shared URL, copy the value after "id=" (e.g., 12345). Validate by noting if it's a sequential or predictable format, common in IDOR scenarios.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- osint
