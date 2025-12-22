---
type: procedure
description: >-
  This procedure demonstrates a multi-step clickjacking attack using two overlay
  div elements to trick a user into performing a sensitive action, such as
  deleting their account, by aligning invisible iframe elements with enticing
  clickable divs.
verified: true
submitted: true
created_at: '2020-08-30T19:03:28.331412+00:00'
updated_at: '2023-05-26T15:58:46.530261+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - '[[tags/Clickjacking]]'
  - '[[tags/Web Applications]]'
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Multi-Step-Clickjacking-for-Account-Deletion

## Summary

This procedure outlines a sophisticated clickjacking attack where an attacker creates an HTML page with an invisible iframe overlaying the target's account management page. Two visible div elements are positioned to align with sensitive buttons (e.g., 'Delete Account' and its confirmation). When the victim clicks the divs, they unknowingly trigger the actions in the iframe, leading to account deletion without direct visibility of the consequences.

## Description

Clickjacking, also known as a UI redress attack, exploits the user's inability to see the underlying iframe content by setting its opacity to near-zero. In this multi-step variant, the attack requires sequential clicks: the first div triggers the initial action (e.g., initiating account deletion), and the second confirms it. This is particularly effective against web applications lacking frame-busting protections like X-Frame-Options or Content-Security-Policy (CSP) frame-ancestors directives. The attack targets user interactions on public-facing web apps, such as account portals, to perform unauthorized actions like data deletion. Prerequisites include knowledge of the target's page layout to precisely position the overlays. Success relies on social engineering to lure the victim to the attacker's page.

## Requirements

1. Access to the target's web application (e.g., valid session or public page).
2. Burp Suite or similar proxy tool to intercept and analyze requests.
3. A web server to host the malicious HTML page (e.g., local Python server or Apache).
4. Knowledge of the target's page structure, including button positions for alignment.
5. Victim interaction via phishing or drive-by delivery.

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers to prevent framing.
- Use CSP with frame-ancestors 'none' or specific domains to block unauthorized iframes.
- Monitor for unusual user actions, such as rapid successive clicks or account deletions from unfamiliar IPs.
- Educate users on recognizing suspicious overlays or prompts.
- Employ client-side JavaScript to detect framing and alert users.

## Objectives

1. Trick the victim into initiating a sensitive action (e.g., account deletion request) via the first click.
2. Capture and confirm the action through the second click without alerting the user to the iframe.
3. Achieve unauthorized account modification or deletion as the primary outcome.

## Instructions

### Step 1: Authenticate and Analyze Target Page

**Context**: Log in to the target application to access the account management section and identify the sensitive action endpoint. This step ensures you understand the page layout for precise overlay positioning.

Use [[tools/Burp-Suite]] to proxy traffic and inspect the page.

1. Configure your browser to route traffic through Burp Suite proxy (default: 127.0.0.1:8080).
2. Navigate to the login page and authenticate with provided credentials.
3. Proceed to the account actions section (e.g., settings or profile).

**Expected Output**: Successful login and visibility of the account page with buttons like 'Delete Account'.

### Step 2: Intercept and Extract Delete Endpoint

**Context**: Capture the HTTP request for the delete action to understand parameters and confirm the confirmation flow. This helps in verifying the attack path without executing it prematurely.

Use [[tools/Burp-Suite]] to intercept requests.

1. In Burp's Proxy tab, enable interception.
2. Trigger the 'Delete Account' action in the target application (do not confirm yet).
3. Copy the intercepted POST request URL and any required parameters (e.g., session tokens).
4. Note the positions of the 'Delete Account' button and the subsequent confirmation button using browser developer tools (e.g., inspect element to get coordinates).

**Expected Output**: Intercepted request showing the delete endpoint URL (e.g., /account/delete) and confirmation dialog trigger.

### Step 3: Craft and Position Clickjacking Exploit

**Context**: Create the malicious HTML page using the provided code snippet, adjusting positions to align divs with target buttons. This step assembles the invisible iframe and overlay elements.

Reference the exploit code: [[codes/Clickjacking-Exploit-HTML-with-Two-Overlay-Divs]]

1. Save the code as an HTML file (e.g., exploit.html).
2. Replace the iframe src attribute with the target's account URL (extracted from Step 2).
3. Adjust CSS positions (top, left) for .firstClick and .secondClick to match button coordinates (e.g., top: 380px; left: 50px for first, left: 200px for second).
4. Ensure iframe dimensions cover the necessary page area (width: 500px; height: 700px).
5. Set opacity to 0.0001 to render the iframe invisible while keeping divs prominent.

**Expected Output**: A functional HTML page where clicking 'Test me first' and 'Test me next' would trigger the aligned actions if framed correctly.

### Step 4: Deploy and Deliver to Victim

**Context**: Host the exploit page and deliver it to the victim via phishing email, malicious link, or social engineering to entice clicks on the divs.

1. Serve the HTML file using a simple web server (e.g., python -m http.server 8000).
2. Send the link to the victim, perhaps disguised as a game or test (e.g., 'Click these buttons to win!').
3. Monitor for victim interaction; the first click initiates deletion, the second confirms it.
4. Verify success by checking the target's application for account deletion.

**Expected Output**: Victim's account deleted upon sequential clicks, confirmed via application logs or direct check.

### Step 5: Verify and Clean Up

**Context**: Confirm the attack's success and mitigate traces to avoid detection.

1. Access the target's application to verify the account is deleted.
2. Clear any proxy logs in Burp Suite.
3. If testing, restore the account or note for reporting.

**Expected Output**: Deleted account status or error on login attempt.
