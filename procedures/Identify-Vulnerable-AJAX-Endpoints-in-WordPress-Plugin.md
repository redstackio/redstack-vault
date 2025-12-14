---
id: proc-uuid-1
tags:
  - csrf
  - wordpress
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/Vulnerable-frs-save-PHP-Function]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:15.559Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable AJAX Endpoints in WordPress Plugin

## Summary

This procedure involves reviewing the source code of the Fluid Responsive Slideshow plugin to identify AJAX endpoints that lack CSRF protection, enabling subsequent exploitation.

## Description

In a WordPress environment, plugins like Fluid Responsive Slideshow (v2.2.0) often register AJAX actions without proper nonce validation. By examining ajax.php, attackers can spot handlers like 'frs_save' that directly process $_POST data for wp_update_post, allowing CSRF attacks. This step is reconnaissance-focused and requires access to plugin files, typically via download or server access.

## Requirements

1. Access to WordPress plugin files (e.g., via FTP or plugin repository)
2. Basic PHP and WordPress knowledge
3. Text editor for code review

## Defense

Defensive measures and detection strategies:

- Implement code reviews for all plugins before installation
- Use WordPress security plugins like Wordfence to scan for missing nonces
- Monitor file access logs for unauthorized plugin inspections

## Objectives

1. Locate vulnerable AJAX handlers
2. Understand input processing flaws
3. Prepare for CSRF testing

## Instructions

### Step 1: Download and Review Plugin Files

**Context**: Obtain the plugin and open ajax.php to search for wp_ajax actions.

**Command** ([[commands/Vulnerable-frs-save-PHP-Function]]):

Review the code snippet:

```php
function frs_save() {
 global $wpdb;
 unset($_POST['action']);
 $id = htmlspecialchars($_POST['post_id']);
 // ... (later)
 $slide_type = htmlspecialchars($_POST['slide_type']);
 $title = htmlspecialchars($_POST['title']);
 $content = $_POST['content'];
 $my_post = array(
  'post_title' => $title,
  'post_content' => $content,
  'ID'=>$id
 );
 wp_update_post( $my_post );
}
```

> This shows no CSRF check; content is raw and unsanitized for JS.

### Step 2: Confirm Lack of Nonces

**Context**: Search for wp_verify_nonce or similar; absence confirms vulnerability.

No specific command; manual grep or search in editor for 'nonce' in ajax.php.

> Expected: No validation found, direct $_POST usage.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

-

## Commands Used

- [[commands/Vulnerable-frs-save-PHP-Function]]

## Tools Used

-

## Tags

- csrf
- wordpress
- recon
