---
id: cf2c2de0-46a3-496b-8e59-d11fb9328e8e
name: Enum and brute force SMB using RID (auth), WinRM, w/ Remote Shell
type: attack_chain
description: Windows, smb, rid, winrm, shell, cisco type 7, brute force, CTF
verified: false
submitted: false
step_count: 11
created_at: '2020-03-31T04:28:39.042317+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
- '[[Brute Force SMB Users Using RID (Authenticated)]]'
- '[[Find Interesting Strings in a Raw Memory Dump]]'
- '[[Build a User List from a Public Webpage]]'
- '[[Basic Port Scan with Service Enumeration]]'
- '[[Dump a Process''s Memory (PowerShell)]]'
- '[[Brute Force Password Hashes (Hashcat)]]'
- '[[Spawn an Interactive Shell with WinRM (Linux)]]'
- '[[Decrypt a Cisco Type 7 Password]]'
- '[[Brute Force SMB Usernames and Passwords]]'
- '[[Identify a Password Hash (Hashcat)]]'
tags:
- Windows
- smb
- rid
- winrm
- shell
- cisco type 7
- brute force
- CTF
---

# 🎯 Enum and brute force SMB using RID (auth), WinRM, w/ Remote Shell

> **Enhanced Attack Chain Dashboard**

---

## 📊 Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| **Chain Status** | ⚠️ **UNVERIFIED** |
| **Total Steps** | `11` |
| **Execution Time** | ~4-8 hours |
| **Skill Level** | 🔴 Advanced |
| **Complexity** | Very High |
| **Impact Level** | 🟠 **HIGH** |

---

## 🎭 Attack Flow Visualization

```mermaid
graph TD
    A[🌐 Initial Recon]
    B[👥 Enumeration]
    C[🎫 Exploitation]
    D[🔑 Analysis]
    E[💥 Cracking]
    F[🔓 Initial Access]
    G[🩸 Deep Enumeration]
    H[📊 Analysis]
    I[⚙️ Privilege Escalation]
    J[🎯 Rights Escalation]
    K[💎 Credential Harvest]
    L[👑 Domain Compromise]
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> J
    J --> K
    K --> L
    
    style A fill:#4a90e2,stroke:#2e5c8a,stroke-width:3px,color:#fff
    style C fill:#e25555,stroke:#8a2e2e,stroke-width:3px,color:#fff
    style E fill:#e25555,stroke:#8a2e2e,stroke-width:3px,color:#fff
    style H fill:#9b59b6,stroke:#6c3483,stroke-width:3px,color:#fff
    style K fill:#e74c3c,stroke:#a93226,stroke-width:3px,color:#fff
    style L fill:#27ae60,stroke:#1e8449,stroke-width:3px,color:#fff
```

---

## 🛠️ Prerequisites & Requirements

### Required Tools
```bash path=null start=null
hashcat              # Password cracking
winrm                # WinRM shell
```

### Target Environment
- ✅ Windows target system
- ✅ Network connectivity to target

### Initial Access Requirements
- 🔓 Requirements based on first step of chain
- 🔓 See detailed procedures below

---

## 🔬 Detailed Attack Procedures

### **[Step 1]** Basic Port Scan with Service Enumeration

**Progress:** `░░░░░░░░░░` 9% | **Risk:** 🟢 Low

**Procedure:** [[Basic Port Scan with Service Enumeration]]

> 📝 **Objective:** Perform an Nmap port scan on a target and enumerate banners of ports 1-1024, as well as popular services (a full list can be found in /usr/share/nmap/nmap-services).

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 2]** Decrypt a Cisco Type 7 Password

**Progress:** `█░░░░░░░░░` 18% | **Risk:** 🟢 Low

**Procedure:** [[Decrypt a Cisco Type 7 Password]]

> 📝 **Objective:** Cisco router passwords encrypted using Type 7 are trivial to decrypt using open source tools, as the key is public.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 3]** Identify a Password Hash (Hashcat)

**Progress:** `██░░░░░░░░` 27% | **Risk:** 🟡 Medium

**Procedure:** [[Identify a Password Hash (Hashcat)]]

> 📝 **Objective:** Analyze a password hash to identify the type and Hashcat mode.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 4]** Brute Force Password Hashes (Hashcat)

**Progress:** `███░░░░░░░` 36% | **Risk:** 🔴 High

**Procedure:** [[Brute Force Password Hashes (Hashcat)]]

> 📝 **Objective:** Use Hashcat to brute force hashes with a dictionary. See Example Hashes for help identifying the mode.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 5]** Build a User List from a Public Webpage

**Progress:** `████░░░░░░` 45% | **Risk:** 🟡 Medium

**Procedure:** [[Build a User List from a Public Webpage]]

> 📝 **Objective:** Administrators will often create user names following predictable patterns, making it possible for attackers to guess at valid names. This procedure will go over popular naming schemes for building potential user lists from a public website, which can be then used to brute force logins.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 6]** Brute Force SMB Usernames and Passwords

**Progress:** `█████░░░░░` 54% | **Risk:** 🔴 High

**Procedure:** [[Brute Force SMB Usernames and Passwords]]

> 📝 **Objective:** Various tools can be used to brute force valid username and password combinations of exposed SMB shares, and is a common approach when attacking Active Directory environments. This attack is noisy, and should be avoided is stealth is a requirement.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 7]** Brute Force SMB Users Using RID (Authenticated)

**Progress:** `██████░░░░` 63% | **Risk:** 🔴 High

**Procedure:** [[Brute Force SMB Users Using RID (Authenticated)]]

> 📝 **Objective:** Various tools can be used to brute force valid SMB users using their relative identifier (RID). This allows attackers to easily enumerate additional users on a system with which they've already authenticated.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 8]** Spawn an Interactive Shell with WinRM (Linux)

**Progress:** `███████░░░` 72% | **Risk:** 🔴 High

**Procedure:** [[Spawn an Interactive Shell with WinRM (Linux)]]

> 📝 **Objective:** Spawn a PowerShell session  on a remote system using the WinRM service (usually port 5985).  See the Evil-WinRM tools page for installation instructions.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 9]** Dump a Process's Memory (PowerShell)

**Progress:** `████████░░` 81% | **Risk:** 🔴 High

**Procedure:** [[Dump a Process's Memory (PowerShell)]]

> 📝 **Objective:** Dump a process's memory  into a file using PowerSploit's Out-Minidump cmdlet.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 10]** Find Interesting Strings in a Raw Memory Dump

**Progress:** `█████████░` 90% | **Risk:** 🔴 High

**Procedure:** [[Find Interesting Strings in a Raw Memory Dump]]

> 📝 **Objective:** Basic enumeration of human readable strings can quickly provide information from a raw memory dump. Depending on the source, a dump may include usernames and passwords, encryption keys, cookies, library calls, etc, all of which can be easily identified without the need for more sophisticated analys

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 11]** Spawn an Interactive Shell with WinRM (Linux)

**Progress:** `██████████` 100% | **Risk:** 🔴 High

**Procedure:** [[Spawn an Interactive Shell with WinRM (Linux)]]

> 📝 **Objective:** Spawn a PowerShell session  on a remote system using the WinRM service (usually port 5985).  See the Evil-WinRM tools page for installation instructions.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

## 🎯 Attack Chain Summary

### Key Achievements
- ✅ Brute Force SMB Users Using RID (Authenticated)
- ✅ Find Interesting Strings in a Raw Memory Dump
- ✅ Build a User List from a Public Webpage
- ✅ Basic Port Scan with Service Enumeration
- ✅ Dump a Process's Memory (PowerShell)
- ... and 5 more procedures

---

## 📈 Technique & Tactic Coverage

---

**Last Updated:** 2023-05-29T16:48:53.162677+00:00 | **Chain Version:** 2.0 Enhanced | **Status:** ⚠️ Draft
