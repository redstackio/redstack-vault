---
id: eb691bf4-46b3-4bf3-a22a-cb50e90a8be0
name: Active Directory ASREPRoast to Kerberoast (have username)
type: attack_chain
description: With valid usernames attempt asreproast / kerberoast
verified: false
submitted: false
step_count: 4
created_at: '2023-01-11T20:54:04.613349+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
- '[[ASREPRoast SPN without pre-auth (have username)]]'
- '[[Query Domain for SPN and Attempt to Kerberoast (Authenticated)]]'
- '[[Crack asrep hash]]'
- '[[Brute Force Users with "Do Not Require Kerberos Preauth." Set]]'
tags:
- With valid usernames attempt asreproast / kerberoast
---

# 🎯 Active Directory ASREPRoast to Kerberoast (have username)

> **Enhanced Attack Chain Dashboard**

---

## 📊 Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| **Chain Status** | ⚠️ **UNVERIFIED** |
| **Total Steps** | `4` |
| **Execution Time** | ~1-2 hours |
| **Skill Level** | 🟢 Beginner-Intermediate |
| **Complexity** | Medium |
| **Impact Level** | 🟡 **MEDIUM** |

---

## 🎭 Attack Flow Visualization

```mermaid
graph TD
    A[🎯 Initial Access]
    B[🔓 Exploitation]
    C[📊 Post-Exploitation]
    D[👑 Objective Complete]
    A --> B
    B --> C
    C --> D
    
    style A fill:#4a90e2,stroke:#2e5c8a,stroke-width:3px,color:#fff
    style B fill:#e25555,stroke:#8a2e2e,stroke-width:3px,color:#fff
    style C fill:#9b59b6,stroke:#6c3483,stroke-width:3px,color:#fff
    style D fill:#27ae60,stroke:#1e8449,stroke-width:3px,color:#fff
```

---

## 🛠️ Prerequisites & Requirements

### Required Tools
```bash path=null start=null
kerberos             # AS-REP roasting
```

### Target Environment
- ✅ Network connectivity to target

### Initial Access Requirements
- 🔓 Requirements based on first step of chain
- 🔓 See detailed procedures below

---

## 🔬 Detailed Attack Procedures

### **[Step 1]** Brute Force Users with "Do Not Require Kerberos Preauth." Set

**Progress:** `██░░░░░░░░` 25% | **Risk:** 🟢 Low

**Procedure:** [[Brute Force Users with "Do Not Require Kerberos Preauth." Set]]

> 📝 **Objective:** Users with "Do not require Kerberos preauthentication" will disclose their TGT without authenticating with a valid password, as long as the username is correct. This allows attackers to build a wordlist and brute force valid users with GetNPUsers.py, also retreiving their TGT.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 2]** ASREPRoast SPN without pre-auth (have username)

**Progress:** `█████░░░░░` 50% | **Risk:** 🟢 Low

**Procedure:** [[ASREPRoast SPN without pre-auth (have username)]]

> 📝 **Objective:** Active Directory try to get hash from username. Looking user without pre-auth attribute on Kerberos. Send AS_REQ to DC to receive encrypted user key to crack. Can achieve without domain account, just a username.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 3]** Crack asrep hash

**Progress:** `███████░░░` 75% | **Risk:** 🔴 High

**Procedure:** [[Crack asrep hash]]

> 📝 **Objective:** Using hashcat to crack asrep hash obtained from impacket or rubeus tools on DC.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 4]** Query Domain for SPN and Attempt to Kerberoast (Authenticated)

**Progress:** `██████████` 100% | **Risk:** 🟡 Medium

**Procedure:** [[Query Domain for SPN and Attempt to Kerberoast (Authenticated)]]

> 📝 **Objective:** Sevrice principal names (SPN) are unique identifiers used by Kerberos authentication. Due to how Kerberos handles service tickets, attackers may be able to query a domain controller with valid credentials, make a request to the ticket granting service (TGT), and receive the hash of other accounts.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

## 🎯 Attack Chain Summary

### Key Achievements
- ✅ ASREPRoast SPN without pre-auth (have username)
- ✅ Query Domain for SPN and Attempt to Kerberoast (Authenticated)
- ✅ Crack asrep hash
- ✅ Brute Force Users with "Do Not Require Kerberos Preauth." Set

---

## 📈 Technique & Tactic Coverage

---

**Last Updated:** 2023-05-29T16:48:53.162677+00:00 | **Chain Version:** 2.0 Enhanced | **Status:** ⚠️ Draft
