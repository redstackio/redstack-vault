---
tags:
  - information-disclosure
  - path-disclosure
  - php
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-14T17:26:12.330Z'
sub_techniques: []
id: a0bca895-42eb-4894-aa94-da9f67cb27a1
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Trigger-Path-Disclosure-via-Malformed-URL-Parameter

## Summary

This procedure exploits a lack of input validation in PHP array parameters by submitting a malformed query string to index.php, triggering a PHP notice or error that reveals the full server path to the webroot or files.

## Description

In the context of the basic-google-maps-placemarks plugin, navigating to an endpoint like http://www.foxyform.com/index.php?step[]=4' causes PHP to misparse the array due to the trailing single quote, resulting in an undefined index notice. Without error suppression (e.g., via display_errors=On in php.ini), the error message includes the absolute file path, such as the location of index.php. This disclosure maps the target's filesystem, potentially aiding in local file inclusion or other path-based attacks. The procedure requires only browser access and is effective against PHP applications handling user-supplied arrays insecurely.

## Requirements

1. Web browser like Firefox for direct URL access
2. Publicly accessible target endpoint (e.g., index.php in the plugin)
3. PHP configuration with error reporting enabled (common in development or misconfigured production)

## Defense

Defensive measures and detection strategies:

- Disable display_errors in php.ini and log errors to secure files only
- Implement input sanitization to reject malformed arrays (e.g., validate parameter types with is_array() and filter_var())
- Use error handling wrappers like try-catch or set_error_handler() to suppress path leaks
- Monitor server logs for unusual PHP notices related to array indices

## Objectives

1. Induce a PHP error via malformed parameter to disclose server paths
2. Map the target's filesystem structure for reconnaissance
3. Identify potential escalation paths like vulnerable file inclusions

## Instructions

### Step 1: Prepare and Access the Endpoint

**Context**: Identify the vulnerable index.php endpoint, typically part of form-handling in the plugin, and craft the malformed parameter.

No specific command; use browser navigation.

> Open Firefox and enter the URL: http://target.com/index.php?step[]=4'. The single quote disrupts PHP's array parsing, triggering an error.

### Step 2: Observe and Extract Path Information

**Context**: Review the error output for disclosed paths and document them for further analysis.

No specific command; inspect browser response.

> The page will display a PHP notice like: "Notice: Undefined index: 4' in /full/server/path/to/index.php on line 123". Extract the path from the message.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- information-disclosure
- path-disclosure
- php
