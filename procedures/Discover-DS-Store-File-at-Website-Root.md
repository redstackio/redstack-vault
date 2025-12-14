---
tags:
  - information-disclosure
  - ds-store
  - reconnaissance
type: procedure
tools:
  - '[[tools/DS-Store-Parser]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[File and Directory Discovery]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0cec9720-b716-4762-8c2d-0e4e38347293
created_at: '2025-12-14T17:25:13.057Z'
updated_at: '2025-12-14T17:25:13.057Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Discover .DS_Store File at Website Root

## Summary

This procedure involves directly accessing a publicly exposed .DS_Store file at the root of a web server to discover internal directory structures and metadata, exploiting macOS file system artifacts left accessible due to server misconfiguration.

## Description

.DS_Store files are macOS system files that store folder metadata, including custom icons, positions, and file paths. When publicly accessible on a web server without authentication, attackers can download and parse them to map out internal directory trees, revealing sensitive organizational structures intended for internal use only. In this scenario, targeting Twitter's website, the root .DS_Store exposed initial folder attributes, aiding further reconnaissance for deeper disclosures.

## Requirements

1. Internet access to the target web server
2. Browser or download tool (e.g., wget or curl) to fetch the file
3. Optional: .DS_Store parsing tool for detailed analysis

## Defense

Defensive measures and detection strategies:

- Configure web servers (e.g., Apache, Nginx) to deny access to hidden files like .DS_Store using rules in .htaccess or server config (e.g., `RedirectMatch 404 /\.[^/]+$`)
- Implement web application firewalls (WAF) to block requests for system files
- Regularly scan for exposed sensitive files using tools like dirbuster or automated crawlers

## Objectives

1. Gain visibility into the target's file and directory structure
2. Identify paths for further exploration of sensitive areas
3. Collect metadata for potential misuse in targeted attacks

## Instructions

### Step 1: Access the Root .DS_Store File

**Context**: Directly request the .DS_Store file at the website root to check for public accessibility.

Use a browser or command-line tool to fetch `https://target.com/.DS_Store` (replace target.com with the actual domain, e.g., twitter.com).

> Download the binary file, which should be accessible without errors if misconfigured.

### Step 2: Parse the File for Metadata

**Context**: Analyze the downloaded .DS_Store to extract directory and file information.

Upload or process the file using the [[tools/DS-Store-Parser]] at https://digi.ninja/projects/fdb.php, or a local parser, to reveal folder attributes and paths (e.g., see parsed output showing internal directories).

> Expected output includes a tree-like structure of folders and files, such as images or text listings of metadata.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/DS-Store-Parser]]

## Tags

- [[information-disclosure]]
- [[ds-store]]
- [[Reconnaissance]]
