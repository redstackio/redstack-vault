---
id: 3d58787d-a4b6-424a-8a30-cf274b5188d6
name: Account-Takeover-Through-Password-Reset-Poisoning
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:53.789366+00:00'
updated_at: '2023-04-06T03:55:53.799003+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Phishing|T1566 - Phishing]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
  - >-
    [[sub-techniques/Spearphishing Attachment|T1566.001 - Spearphishing
    Attachment]]
  - '[[sub-techniques/Spearphishing Link|T1566.002 - Spearphishing Link]]'
  - >-
    [[sub-techniques/Spearphishing via Service|T1566.003 - Spearphishing via
    Service]]
tags:
  - '[[tags/Account Takeover]]'
  - '[[tags/Account Takeover Through Password Reset Poisoning]]'
  - '[[tags/Password Reset Feature]]'
  - phishing
  - host-header-injection
commands:
  - '[[commands/curl-modify-host-header]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Charles-Proxy]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Account-Takeover-Through-Password-Reset-Poisoning

## Summary

Account takeover through password reset poisoning involves manipulating the password reset feature of a web application via phishing and HTTP request interception. An attacker sends a phishing email to the victim with a link mimicking the legitimate reset page. Upon the victim submitting their email, the attacker intercepts the request, modifies the Host header to point to a controlled domain, and forwards it. This poisons the reset process, directing the victim to the attacker's fake page where they enter a new password, which is captured for account takeover.

## Description

This procedure targets web applications with vulnerable password reset mechanisms that rely on the Host header for redirecting reset links or pages. The attack begins with spearphishing to lure the victim into initiating a password reset on a proxied connection. By altering the Host header (e.g., from the legitimate domain to attacker.com), the application generates a reset token or link pointing to the attacker's server. The victim, believing it's legitimate, completes the reset on the attacker's page, revealing their new password. This grants the attacker valid credentials for the victim's account, enabling access to sensitive data, further phishing, or malware distribution. The technique exploits trust in password reset flows and is effective against applications without Host header validation. Prerequisites include the ability to phish the victim and position a proxy between the victim and the target server.

## Requirements

1. Access to send phishing emails to the target victim (e.g., via compromised email or social engineering tools).
2. A proxy tool like [[tools/Burp-Suite]] or [[tools/Charles-Proxy]] to intercept and modify HTTP requests.
3. Control over a domain and server to host the fake reset page (e.g., attacker.com/reset).
4. Knowledge of the target's password reset endpoint URL and expected request format.
5. Victim interaction: The victim must click the phishing link and proceed with the reset process.

## Defense

Defensive measures and detection strategies:

- Implement strict Host header validation on the server side to ensure redirects only use whitelisted domains.
- Use multi-factor authentication (MFA) for password resets to prevent takeover even if credentials are captured.
- Educate users on phishing recognition, such as verifying reset links match the official domain.
- Monitor for anomalous Host headers in password reset requests and log them for anomaly detection.
- Employ web application firewalls (WAFs) to block requests with mismatched Host headers.

## Objectives

1. Trick the victim into initiating a password reset via phishing.
2. Intercept and poison the reset request to redirect to attacker-controlled infrastructure.
3. Capture the victim's new password during the reset completion.
4. Achieve full account takeover for data access or further compromise.

## Instructions

### Step 1: Prepare Phishing Email and Fake Reset Page

**Context**: Set up the phishing lure and the malicious endpoint to capture credentials. Create a fake password reset page that mirrors the legitimate one, including form fields for email and new password submission. Host it on your controlled domain (e.g., attacker.com/reset). Craft a phishing email with a link to this page, disguised as coming from the legitimate service.

**Instructions**: Use an email tool or service to send the phishing email. Ensure the link points to your proxy setup (e.g., via Burp or Charles) rather than directly to the fake page, to enable interception.

> No specific command here; focus on social engineering setup. Verify the fake page logs submitted credentials (e.g., to a file or database).

### Step 2: Intercept Victim's Password Reset Initiation

**Context**: Position your proxy to capture the victim's request when they enter their email on the legitimate site (lured via phishing). The goal is to modify the request before it reaches the server.

**Instructions**: Configure [[tools/Burp-Suite]] or [[tools/Charles-Proxy]] to intercept traffic from the victim's browser. Have the victim directed to the real reset page through your proxied link. When they submit the email (e.g., POST to /reset), pause the request in the proxy.

> Expected: Intercepted POST request with victim's email in the body.

### Step 3: Modify Host Header and Forward Request

**Context**: Alter the Host header in the intercepted request to poison the reset flow, causing the server to generate a reset link or token for your domain. This exploits applications that use the Host header for reset URL construction.

**Command** ([[commands/curl-modify-host-header]]):

Use [[commands/curl-modify-host-header]] to simulate or test the modified request if not using a GUI proxy:

```bash
curl -X POST https://example.com/reset.php \
  -H "Accept: */*" \
  -H "Content-Type: application/json" \
  -H "Host: attacker.com" \
  -d '{"email": "victim@example.com"}'
```

> This command sends the POST with the modified Host header. In a live attack, modify directly in the proxy interface and forward. The server processes the request as if from attacker.com, generating a reset token emailed or displayed with a link to attacker.com/reset?token=abc.

**Expected Output**: Server response with a success message or reset initiation confirmation, but the underlying token now points to your domain.

### Step 4: Capture Victim's New Password

**Context**: Direct the victim to complete the reset on your fake page using the poisoned token. Log the submitted new password.

**Instructions**: Monitor your fake page logs. When the victim follows the poisoned reset link (from email or previous response) and submits the new password, capture it via server-side logging or form handler (e.g., PHP script writing to a file).

> Expected: Victim submits form on attacker.com, revealing plaintext new password.

### Step 5: Validate Takeover and Access Account

**Context**: Use the captured credentials to log in and confirm control.

**Instructions**: Navigate to the legitimate login page and enter the victim's email with the new password. If successful, explore the account for sensitive data.

> Expected: Successful login without errors, granting access to the victim's dashboard or resources.

**Success Indicators**:
- Phishing email opened and link clicked.
- Modified request forwarded without server rejection.
- Victim completes reset on fake page, password captured.
- Valid login with new credentials.
