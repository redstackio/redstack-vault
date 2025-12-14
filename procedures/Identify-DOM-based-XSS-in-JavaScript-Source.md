---
tags:
  - xss
  - dom-xss
  - source-analysis
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.348Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4ce87855-7532-4dee-aaae-1f8c92c007aa
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify-DOM-based-XSS-in-JavaScript-Source

## Summary

This procedure involves inspecting the client-side JavaScript source code of a web page to detect DOM-based XSS vulnerabilities, particularly those arising from unsafe DOM manipulations like innerHTML with unsanitized inputs such as document.URL.

## Description

In the context of the Informatica knowledge base portal, this procedure targets the infasearchltd.aspx page where JavaScript around line 1406 uses document.URL (including the hash) without proper sanitization in an innerHTML assignment. This allows attackers to analyze the code for sinks that can be exploited for arbitrary JavaScript execution. The procedure requires only a web browser and is non-intrusive, focusing on static analysis to uncover the vulnerability before exploitation. Expected outcomes include pinpointing the exact code path for payload injection, enabling subsequent testing without server interaction.

## Requirements

1. Web browser with Developer Tools (e.g., Chrome, Firefox)
2. Direct access to the target URL: https://kb.informatica.com/KBExternal/pages/infasearchltd.aspx
3. Basic knowledge of JavaScript and DOM manipulation

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict inline scripts and eval
- Use DOM APIs like textContent or createTextNode instead of innerHTML
- Sanitize all URL-derived inputs with libraries like DOMPurify
- Monitor client-side errors and unexpected script executions via browser logging

## Objectives

1. Locate vulnerable JavaScript code handling URL fragments
2. Confirm lack of input sanitization in DOM insertion
3. Prepare for payload crafting based on attribute context breakout

## Instructions

### Step 1: Navigate to Target Page

**Context**: Load the page to access its source code for inspection.

Open a web browser and navigate to `https://kb.informatica.com/KBExternal/pages/infasearchltd.aspx`.

> Ensure the page loads fully without errors to view the complete JavaScript.

### Step 2: Inspect Source Code

**Context**: Use Developer Tools to examine the JavaScript for vulnerable patterns.

Press F12 to open Developer Tools, go to the Sources or Elements tab, and search for 'DynamicBreadcrumb' or scroll to approximately line 1406 in the embedded scripts.

> Look for code like: `var li = document.createElement('li'); strChild = '<a href='+document.URL+' style=\'color:#fff !important;font-size:10px\'>Search Results</a>'; li.innerHTML = strChild; document.getElementById('DynamicBreadcrumb').appendChild(li);`. Note the unsanitized `document.URL` insertion.

### Step 3: Analyze for XSS Sink

**Context**: Identify how the URL hash can escape the href attribute.

Review the string construction: the hash after # can close the href quote and inject additional HTML attributes or tags.

> Confirm that no encoding (e.g., htmlentities) is applied to document.URL, making it vulnerable to DOM-based XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[dom-xss]]
- [[JavaScript]]
