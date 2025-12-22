---
tags:
  - injection
  - theme-modification
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/inject-shopify-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:18.206Z'
sub_techniques: []
id: 1eef396a-b0a0-495c-a082-2f4bae238711
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Script-into-Store-Theme

## Summary

Insert the crafted XSS payload into a Shopify store's theme using the admin editor, enabling persistent delivery to visitors.

## Description

Shopify allows theme customization via liquid files, which can be abused to embed malicious scripts. This step modifies theme.liquid or a section to include the payload, triggering on page load or click.

## Requirements

1. Shopify admin access with theme edit permissions
2. Prepared payload from prior procedure
3. Active store environment

## Defense

Defensive measures and detection strategies:

- Review theme changes for unauthorized scripts
- Enable script scanning in theme uploads
- Use version control for themes to detect modifications

## Objectives

1. Embed payload without breaking theme functionality
2. Ensure script executes in user context
3. Prepare for admin triggering

## Instructions

### Step 1: Access Theme Editor

**Context**: Navigate to theme modification interface.

Log in to Shopify admin > Online Store > Themes > Actions > Edit code on current theme.

> Expected output: Code editor open.

### Step 2: Insert Payload

**Context**: Add the script to a liquid file.

Open theme.liquid, insert the payload from [[commands/inject-shopify-xss-payload]] in the <head> or <body>.

```liquid
<!-- Insert in theme.liquid -->
{{ include the JS payload here }}
```

Save and preview.

> Expected output: Theme saves successfully, script visible in source.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/inject-shopify-xss-payload]]

## Tools Used


## Tags

- [[injection]]
- [[shopify]]
