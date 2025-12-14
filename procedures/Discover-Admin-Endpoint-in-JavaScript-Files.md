---
tags:
  - reconnaissance
  - javascript-analysis
  - endpoint-discovery
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
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:29:44.340Z'
sub_techniques: []
id: b85e59e1-bc76-4098-8348-1ae9fb2cf18e
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Discover-Admin-Endpoint-in-JavaScript-Files

## Summary

This procedure involves reviewing client-side JavaScript files on a target web application to identify hidden or admin-only endpoints, such as Zomato's restaurant menus handler, revealing potential access control weaknesses.

## Description

In web applications like Zomato, admin endpoints are often referenced in JavaScript for dynamic interactions. By inspecting source code, attackers can uncover these endpoints and their actions without server-side access. This is particularly effective for privilege escalation scenarios where endpoints lack proper authorization checks. Prerequisites include an authenticated session and browser access; expected outcomes include endpoint paths and actionable parameters for further testing.

## Requirements

1. Authenticated access to the target web application (e.g., Zomato user account)
2. Modern web browser with developer tools (e.g., Chrome DevTools)
3. Basic knowledge of JavaScript and HTTP requests

## Defense

Defensive measures and detection strategies:

- Obfuscate or minify JavaScript to hide endpoint references
- Implement Content Security Policy (CSP) to restrict script execution
- Monitor for unusual client-side code inspections via browser analytics

## Objectives

1. Identify admin endpoints exposed in client-side code
2. Extract actions and parameters for exploitation
3. Enable subsequent testing of access controls

## Instructions

### Step 1: Navigate to Target Page

**Context**: Access a relevant page where admin functionality might be referenced, such as a restaurant details page.

**Command** (Browser Navigation):
No specific command; manually navigate to https://www.zomato.com/[restaurant-slug] in the browser.

> Load the page and ensure an authenticated session is active. This positions the attacker to inspect dynamic content.

### Step 2: Inspect JavaScript Sources

**Context**: Use developer tools to search for endpoint references in loaded JS files.

**Command** (DevTools Search):
In Chrome DevTools (F12), go to Sources tab, search for "/php/restaurant_menus_handler.php" across all JS files.

> Expected output: Matches revealing the endpoint and actions like "toggle-res-menu-type", "clear_menu_tool". Note restaurant IDs (res_id) from page elements if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[web-discovery]]
