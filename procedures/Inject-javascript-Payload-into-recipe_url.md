---
id: proc-uuid-instacart-xss-inject-001
tags:
  - xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.875Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-javascript-Payload-into-recipe_url

## Summary

This procedure involves crafting a URL for the Instacart partner recipe page by injecting a javascript: protocol payload into the recipe_url parameter, which is reflected unsanitized into an href attribute, setting up for XSS execution.

## Description

In the context of testing the Instacart web application, the recipe_url parameter accepts user input without validation and directly inserts it into an HTML href attribute on the partner recipe page. By supplying 'javascript:alert(1)' as the value, the attacker creates a link that, when clicked, executes JavaScript in the victim's browser. This is a classic reflected XSS scenario requiring no authentication and relying on social engineering for the click. Prerequisites include access to a web browser and knowledge of URL encoding for parameters.

## Requirements

1. Web browser for URL construction and testing
2. Public access to https://www.instacart.com/store/partner_recipe
3. Basic understanding of URL parameters and HTML attributes

## Defense

Defensive measures and detection strategies:

- Implement input validation and sanitization for URL parameters, stripping or encoding javascript: protocols
- Use Content Security Policy (CSP) to restrict inline JavaScript execution
- Monitor for anomalous href attributes in server logs or via WAF rules blocking javascript: schemes

## Objectives

1. Set up a reflected payload in the target page's HTML
2. Prepare for user interaction to trigger execution
3. Demonstrate vulnerability for reporting or exploitation

## Instructions

### Step 1: Construct the Malicious URL

**Context**: Build the base URL with the payload and supporting parameters to mimic a legitimate recipe submission, ensuring the page renders without errors.

No specific command; manually assemble in browser address bar or using a URL builder:

Example URL:
```url
https://www.instacart.com/store/partner_recipe?recipe_url=javascript:alert(1)&partner_name=&ingredients%5B%5D=apples&ingredients%5B%5D=butter&ingredients%5B%5D=Splenda+Brown+Sugar+Blend&ingredients%5B%5D=cinnamon&ingredients%5B%5D=nutmeg&title=Barb%27s+Fried+Apples+-Diabetic-Low+Fat&description=&image_url=%2Fassets%2Fimg%2Fno-recipe-image.jpg
```

> This constructs a valid-looking recipe page where recipe_url is reflected into the image href. Verify by inspecting the page source for the payload in the href.

### Step 2: Validate Reflection

**Context**: Load the URL and confirm the payload is present but not yet executed.

Open the URL in a browser and inspect the element (e.g., right-click the recipe image > Inspect).

> Look for href="javascript:alert(1)" in the <a> tag. If present, the injection succeeded.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
