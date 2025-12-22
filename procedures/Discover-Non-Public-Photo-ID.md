---
tags:
  - idor
  - discovery
  - flickr
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
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:25:34.218Z'
sub_techniques: []
id: 203bf6bf-59a2-4089-9113-e478e980f451
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Discover-Non-Public-Photo-ID

## Summary

This procedure identifies the unique ID of a non-public photo on Flickr, enabling direct object referencing in subsequent exploitation steps. It leverages exposed IDs from public or semi-public sources without requiring authentication.

## Description

In the context of Flickr's IDOR vulnerability, photo IDs are globally unique identifiers that can be obtained from various sources like shared links, API endpoints, or even cached data. Attackers discover these IDs through reconnaissance on user profiles, groups, or external references where privacy is not enforced on the ID itself. Once obtained, the ID allows bypassing visibility checks in features like group uploads. Prerequisites include a Flickr account and basic web navigation skills; expected outcomes are a harvestable list of target photo IDs for non-public content.

## Requirements

1. Active Flickr account for browsing
2. Access to public Flickr searches or user feeds where IDs may leak
3. Web browser with network inspection capabilities

## Defense

Defensive measures and detection strategies:

- Implement ID obfuscation or randomization in public APIs
- Monitor for anomalous ID usage in logs
- Enforce strict privacy on all photo metadata exposure

## Objectives

1. Obtain valid photo IDs for private content
2. Validate IDs are for non-public photos
3. Prepare for direct reference in group operations

## Instructions

### Step 1: Reconnaissance for Photo Exposure

**Context**: Search for potential targets and inspect elements where photo IDs are referenced.

Navigate to Flickr's search or user profile pages. Use the browser's developer tools (F12) to inspect network requests or HTML elements containing photo links. Look for patterns like 'photo_id=1234567890' in URLs or JSON responses.

### Step 2: Extract and Verify ID

**Context**: Collect the ID and test basic accessibility to confirm it's non-public.

Copy the extracted ID. Attempt to access https://www.flickr.com/photos/[user]/ [ID] directly; if access is denied, it's likely private, confirming suitability for IDOR exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[Discovery]]
