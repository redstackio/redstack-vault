---
id: 94290888-4810-436c-9805-6288d3fee4e7
name: Extract-Firefox-and-Thunderbird-Passwords-from-Profiles
type: procedure
verified: true
submitted: false
created_at: '2019-10-23T21:39:44.833818+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credentials from Web Browsers]]'
sub_techniques: []
tags:
  - brute-force
  - cryptography
  - data-exposure
  - credential-access
commands:
  - '[[commands/firefox-decrypt-extract-passwords-from-profile]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/firefox-decrypt]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Extract-Firefox-and-Thunderbird-Passwords-from-Profiles

## Summary

This procedure extracts saved passwords from Firefox and Thunderbird user profiles by using the firefox_decrypt tool to decrypt credentials protected by a master password. It is useful in post-exploitation scenarios where an attacker has access to a victim's user directory and needs to recover stored website logins, assuming the master password is known or can be brute-forced.

## Description

Firefox and Thunderbird store saved passwords in their user profiles, encrypted with a master password for protection. If the attacker has local access to the victim's machine or profile directory (e.g., via file exfiltration), tools like firefox_decrypt can decrypt these credentials by providing the master password. The procedure involves cloning the tool, running the decryption script on the profile directory, and optionally brute-forcing the master password using a wordlist if unknown. This targets the typical profile locations on Linux (~/.mozilla/firefox or ~/.thunderbird) and can be adapted for Windows. Success yields plaintext usernames and passwords for websites, enabling further lateral movement or impersonation.

## Requirements

1. Local access to the victim's user profile directory (e.g., /home/user/.mozilla/firefox on Linux or %APPDATA%\Mozilla\Firefox\Profiles on Windows).
2. Python 3 installed on the attacker's machine.
3. Optional: A wordlist for brute-forcing the master password if unknown.
4. The firefox_decrypt tool installed.

## Defense

- Enforce strong, unique master passwords for browser credential storage and enable multi-factor authentication where possible.
- Use full-disk encryption (e.g., BitLocker on Windows, LUKS on Linux) to protect profile files at rest.
- Monitor for unauthorized access to user directories via file integrity monitoring tools like OSSEC or auditd.
- Disable password saving in browsers and use a dedicated password manager with better encryption.

## Objectives

1. Decrypt and extract saved credentials from Firefox/Thunderbird profiles.
2. Recover plaintext usernames and passwords for targeted websites.
3. Enable credential reuse for further attacks if the master password is compromised.

## Instructions

### Step 1: Install Firefox Decrypt Tool

**Context**: Clone the firefox_decrypt repository to obtain the decryption script. This step sets up the necessary tool for processing profile files.

Embed the installation inline:

```bash
git clone https://github.com/unode/firefox_decrypt.git
```

> This downloads the tool to a local directory. Navigate to the cloned folder for subsequent steps. Expected output includes confirmation of the clone operation, such as "Cloning into 'firefox_decrypt'...".

### Step 2: Extract Passwords from Profile

**Context**: Run the decryption script on the target profile directory, providing the master password via stdin if prompted. This step decrypts and lists all saved credentials.

**Command** ([[commands/firefox-decrypt-extract-passwords-from-profile]]):
```bash
python firefox_decrypt.py $PROFILE_DIRECTORY
```

> Replace $PROFILE_DIRECTORY with the path to the profiles.ini location (e.g., ~/.mozilla/firefox). If a master password is set, enter it when prompted. The script processes logins.json and key4.db files to output site details. Expected output includes a list of websites, usernames, and decrypted passwords if the master password is correct.

### Step 3: Brute-Force Master Password if Unknown

**Context**: If the master password is not known, use a scripted loop to attempt guesses from a wordlist. This automates trial-and-error decryption until success.

**Code** ([[codes/Brute-Force-Firefox-Master-Password-with-Wordlist]]):
```bash
for guess in $(cat $_WORDLIST); do echo $guess | python firefox_decrypt/firefox_decrypt.py .mozilla/firefox  2>&1 | grep 'Username:' -A 1; done
```

> Replace $_WORDLIST with the path to your password list (e.g., rockyou.txt). The script pipes each guess as the master password and greps for username output to indicate success. Run this in the directory containing the profile. Expected output shows successful decryptions with usernames and passwords upon hitting the correct guess; failures produce no grep matches.
