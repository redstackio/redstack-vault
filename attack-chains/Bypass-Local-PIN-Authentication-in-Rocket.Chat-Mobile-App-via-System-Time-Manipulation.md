---
tags:
  - authentication-bypass
  - pin-bypass
  - time-manipulation
  - rocket-chat
  - mobile-security
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Mobile
  - iOS
  - Android
submitted: true
complexity: low
created_at: '[TIMESTAMP]'
procedures:
  - '[[procedures/Enable-Screen-Lock-in-Rocket.Chat-App]]'
  - '[[procedures/Trigger-PIN-Lock-by-Inactivity]]'
  - '[[procedures/Verify-PIN-Lock-Activation]]'
  - '[[procedures/Manipulate-Device-System-Time-to-Bypass-Lock]]'
  - '[[procedures/Access-App-Without-PIN]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:11.295Z'
description: >-
  Multi-stage attack chain exploiting the Rocket.Chat mobile app's reliance on
  device system time for PIN lock timeouts, allowing bypass with physical access
  by adjusting the clock.
skill_level: low
impact_level: high
id: bbacc1e2-8d81-4621-9123-17f7c097446c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass Local PIN Authentication in Rocket.Chat Mobile App via System Time Manipulation

Multi-stage attack chain demonstrating a complete attack workflow to bypass the local PIN code in Rocket.Chat's mobile app by manipulating the device's system time. The app uses the system clock to enforce lock timeouts after inactivity, allowing an attacker with physical access to reset the time and evade the PIN prompt, gaining full access to the user's account and privileges.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~2 minutes |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enable Screen Lock] --> B[Trigger Lock by Inactivity]
    B --> C[Verify Lock Activation]
    C --> D[Manipulate System Time]
    D --> E[Access App Unlocked]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (requires physical access to the target device)

### Target Environment

- Rocket.Chat mobile app installed on iOS or Android device
- App screen lock feature enabled with a timeout period (e.g., 1 minute)
- No network access required; fully local

### Initial Access Requirements

- Physical possession of the unlocked device
- Ability to access device settings for time manipulation
- No prior credentials needed beyond physical access

## Detailed Attack Procedures

### Step 1: Enable Screen Lock
procedure: [[procedures/Enable-Screen-Lock-in-Rocket.Chat-App]]

**Objective**: Configure the app's security feature to establish a baseline for the lock timeout mechanism.

**Instructions**: Open the Rocket.Chat app and navigate to settings to enable the screen lock with a short timeout, such as 1 minute. This sets up the condition for the subsequent lock trigger.

**Expected Output**: Screen lock enabled confirmation in app settings.

**Success Indicators**:
- Lock timeout period visible in settings
- App prompts for PIN setup if not already configured

### Step 2: Trigger PIN Lock by Inactivity
procedure: [[procedures/Trigger-PIN-Lock-by-Inactivity]]

**Objective**: Initiate the inactivity period to activate the PIN lock based on the system time.

**Instructions**: Close the chat activity in the app, note the current system time (e.g., 00:02), and wait for the configured timeout to elapse without interacting with the app.

**Expected Output**: The app enters a locked state after the timeout period.

**Success Indicators**:
- Elapsed time matches or exceeds the lock timeout
- System clock shows time progression beyond the noted start time

### Step 3: Verify PIN Lock Activation
procedure: [[procedures/Verify-PIN-Lock-Activation]]

**Objective**: Confirm that the PIN prompt is active, validating the lock mechanism before bypass.

**Instructions**: Reopen the Rocket.Chat app to check for the PIN entry screen, then close the app again without entering the PIN.

**Expected Output**: PIN code prompt appears on app launch.

**Success Indicators**:
- App requires PIN input to proceed
- No access to chat interface without authentication

### Step 4: Manipulate Device System Time to Bypass Lock
procedure: [[procedures/Manipulate-Device-System-Time-to-Bypass-Lock]]

**Objective**: Alter the system clock to a time before the lock was triggered, tricking the app into believing the timeout has not occurred.

**Instructions**: Access the device's system settings, disable automatic time synchronization if needed, and set the clock back to a time prior to the lock trigger (e.g., 00:01).

**Expected Output**: Device clock updated to the manipulated time.

**Success Indicators**:
- System time reflects the backward adjustment
- No errors in time change (may require developer options on some devices)

### Step 5: Access App Without PIN
procedure: [[procedures/Access-App-Without-PIN]]

**Objective**: Reopen the app to gain unauthorized access, confirming the bypass success.

**Instructions**: Launch the Rocket.Chat app again; the PIN prompt should not appear due to the manipulated time indicating no inactivity timeout.

**Expected Output**: Full access to the user's account, chats, and privileges without PIN entry.

**Success Indicators**:
- App opens directly to the main interface
- All user data and features accessible

## Attack Chain Summary

### Key Achievements

1. Enabled and triggered the app's PIN lock mechanism
2. Confirmed the lock's activation via system time dependency
3. Bypassed authentication by manipulating the device clock
4. Gained full unauthorized access to the Rocket.Chat account

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: [TIMESTAMP]*

## References

- [Rocket.Chat | Report #1126414 - Bypass local authentication (PIN code) | HackerOne](https://hackerone.com/reports/1126414)
