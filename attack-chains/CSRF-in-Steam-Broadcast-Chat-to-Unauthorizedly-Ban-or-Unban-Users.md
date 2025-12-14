---
id: ac-steam-csrf-ban-001
tags:
  - csrf
  - steam
  - web
  - ban
  - unban
  - broadcast
  - moderation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Start-Steam-Broadcast]]'
  - '[[procedures/Extract-Broadcast-Steam-ID]]'
  - '[[procedures/Craft-Malicious-CSRF-HTML-Page]]'
  - '[[procedures/Lure-Broadcast-Creator-to-Malicious-Page]]'
  - '[[procedures/Auto-Submit-CSRF-Form-for-Ban-Unban]]'
step_count: 5
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:35.523Z'
description: >-
  A multi-stage CSRF attack exploiting the Steam broadcast chat's mute update
  endpoint to silently ban or unban users by tricking the broadcast creator into
  visiting a malicious page.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# CSRF in Steam Broadcast Chat to Unauthorizedly Ban or Unban Users

Multi-stage attack chain demonstrating a complete CSRF workflow against Steam's broadcast chat feature, allowing an attacker to disrupt moderation by banning or unbanning users without the creator's consent.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Start Broadcast] --> B[Extract ID]
    B --> C[Craft Malicious Page]
    C --> D[Lure Victim]
    D --> E[Auto-Submit CSRF]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard web development tools like a text editor and web server)

### Target Environment

- Steam Community web platform
- Active Steam account for attacker
- Victim must be a broadcast creator with moderation privileges

### Initial Access Requirements

- No prior credentials needed for the target
- Attacker needs social engineering access to lure the victim
- Network access to host the malicious page

## Detailed Attack Procedures

### Step 1: Start a Broadcast on Steam Community
procedure: [[procedures/Start-Steam-Broadcast]]

**Objective**: Initiate a live broadcast to generate a target URL containing the Steam ID for exploitation.

**Instructions**: Log into Steam Community and start a live broadcast session via the broadcasting feature. This creates a shareable URL.

**Expected Output**: A broadcast URL like `https://steamcommunity.com/broadcast/watch/{STEAM ID}/`.

**Success Indicators**:
- Broadcast is live and URL is generated
- Steam ID is visible in the URL

### Step 2: Extract the Broadcast's Steam ID
procedure: [[procedures/Extract-Broadcast-Steam-ID]]

**Objective**: Parse the broadcast URL to obtain the Steam ID parameter required for crafting the CSRF payload.

**Instructions**: Manually inspect the broadcast URL or use browser developer tools to copy the `{STEAM ID}` value from the path.

**Expected Output**: The numeric Steam ID (e.g., 123456789).

**Success Indicators**:
- Steam ID extracted accurately
- ID can be used in subsequent form parameters

### Step 3: Craft a Malicious HTML Page for Ban or Unban
procedure: [[procedures/Craft-Malicious-CSRF-HTML-Page]]

**Objective**: Create an HTML page with a hidden form and JavaScript to auto-submit a POST request to the vulnerable endpoint.

**Instructions**: Use a text editor to build an HTML file with an iframe, hidden form targeting `https://steamcommunity.com/broadcast/ajaxupdateusermute/`, and inputs for `broadcaststeamid`, `issuersteamid`, `chattersteamid`, `bantype`, `duration`, and `perm`. Include JavaScript to submit on load. For unban: set `bantype=0`, `duration=0`, `perm=0`. For permanent ban: `bantype=1`, `duration=0`, `perm=1`. Host the page on an attacker-controlled server.

**Expected Output**: A functional HTML file that loads silently and submits the form.

**Success Indicators**:
- Page loads without visible elements
- Form submission triggers on page load

### Step 4: Trick the Broadcast Creator into Visiting the Malicious Page
procedure: [[procedures/Lure-Broadcast-Creator-to-Malicious-Page]]

**Objective**: Use social engineering to direct the victim (broadcast creator) to the attacker's hosted malicious page.

**Instructions**: Employ phishing emails, chat messages, or fake links pretending to be Steam-related content to lure the victim to the hosted HTML page.

**Expected Output**: Victim visits the page, triggering the auto-submit.

**Success Indicators**:
- Victim confirms visit (e.g., via logs)
- No user interaction required post-visit

### Step 5: The Form Submits Automatically, Exploiting the CSRF
procedure: [[procedures/Auto-Submit-CSRF-Form-for-Ban-Unban]]

**Objective**: Execute the CSRF payload to silently ban or unban a target user in the broadcast chat.

**Instructions**: Upon page load, the embedded JavaScript `document.getElementById("csrf-form").submit()` triggers the POST request in a hidden iframe, exploiting the lack of CSRF token validation.

**Expected Output**: Silent ban or unban action on the target user without alerting the victim.

**Success Indicators**:
- Target user is banned/unbanned in the broadcast chat
- No errors in browser console; action completes invisibly

## Attack Chain Summary

### Key Achievements

1. Generated and extracted broadcast Steam ID for targeting
2. Crafted and hosted a stealthy CSRF payload page
3. Lured victim to execute the attack without suspicion
4. Achieved unauthorized moderation control via CSRF
5. Disrupted broadcast community interaction silently

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
