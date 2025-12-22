---
id: 60c6803d-8835-41e0-9152-75ad84fb3b5f
name: patTemplate-Template-Definition-Example
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:40.417306+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - PHP
tags:
  - patTemplate
  - template
  - example
validated: true
---

# patTemplate-Template-Definition-Example

## Code

```xml
<patTemplate:tmpl name="page">
  This is the main page.
  <patTemplate:tmpl name="foo">
    It contains another template.
  </patTemplate:tmpl>
  <patTemplate:tmpl name="hello">
    Hello {NAME}.<br/>
  </patTemplate:tmpl>
</patTemplate:tmpl>
```

## Description

This XML snippet illustrates the basic structure of a patTemplate page template, including nested <patTemplate:tmpl> tags for sub-templates and {NAME} placeholders for dynamic content insertion. It demonstrates how patTemplate organizes reusable components but highlights potential injection points if user input populates these elements without validation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| name | Unique identifier for the template | "page" |
| {NAME} | Placeholder for dynamic substitution | User-supplied value, e.g., "World" |

## Usage

Embed this structure in PHP code using patTemplate::displayTemplate() to render dynamic pages. In an attack context, identify where user input replaces placeholders or is inserted as tag attributes, then inject <patTemplate:php> for SSTI. For example, if {NAME} is user-controlled, set it to a malicious value during form submission.

## Detection

- Web logs showing XML tags in request bodies.
- Server errors with 'patTemplate' in stack traces.
- Anomalous PHP execution in template rendering (monitor via PHP error logs or WAF rules for <patTemplate:php> patterns).

## Related

- [[procedures/Exploit-Server-Side-Template-Injection-in-patTemplate]]
