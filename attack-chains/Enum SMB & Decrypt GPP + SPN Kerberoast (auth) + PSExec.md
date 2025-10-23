---
id: eaa41e18-3fc0-4a6b-a66d-313968ebafae
name: Enum SMB & Decrypt GPP + SPN Kerberoast (auth) + PSExec
type: attack_chain
description: Windows, SMB, Group Password Policy, SYSVOL, SPN, Kerberoast, psexec
verified: false
submitted: false
step_count: 10
created_at: '2020-03-26T01:58:07.907746+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
- '[[Connect to Windows using PsExec (Authenticated)]]'
- '[[Decrypt a Group Policy Preferences (GPP) Password]]'
- '[[List All Active Directory Users]]'
- '[[Search SMB by Filename and Download Matches]]'
- '[[Basic Port Scan with Service Enumeration]]'
- '[[Query Domain for SPN and Attempt to Kerberoast (Authenticated)]]'
- '[[Brute Force Password Hashes (Hashcat)]]'
- '[[Browse an SMB Share]]'
- '[[Identify a Password Hash (Hashcat)]]'
- '[[List SMB Shares]]'
tags:
- Windows
- SMB
- Group Password Policy
- SYSVOL
- SPN
- Kerberoast
- psexec
---

# 🎯 Enum SMB & Decrypt GPP + SPN Kerberoast (auth) + PSExec

> **Enhanced Attack Chain Dashboard**

---

## 📊 Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| **Chain Status** | ⚠️ **UNVERIFIED** |
| **Total Steps** | `10` |
| **Execution Time** | ~4-8 hours |
| **Skill Level** | 🟢 Beginner-Intermediate |
| **Complexity** | Very High |
| **Impact Level** | 🟡 **MEDIUM** |

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

**Progress:** `█░░░░░░░░░` 10% | **Risk:** 🟢 Low

**Procedure:** [[Basic Port Scan with Service Enumeration]]

> 📝 **Objective:** Perform an Nmap port scan on a target and enumerate banners of ports 1-1024, as well as popular services (a full list can be found in /usr/share/nmap/nmap-services).

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 2]** List SMB Shares

**Progress:** `██░░░░░░░░` 20% | **Risk:** 🟢 Low

**Procedure:** [[List SMB Shares]]

> 📝 **Objective:** Query an SMB server and attempt to list available shares using a null session (no login).

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 3]** Browse an SMB Share

**Progress:** `███░░░░░░░` 30% | **Risk:** 🟡 Medium

**Procedure:** [[Browse an SMB Share]]

> 📝 **Objective:** Use smbclient to connect to an SMB share and browse with an interactive shell.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 4]** Search SMB by Filename and Download Matches

**Progress:** `████░░░░░░` 40% | **Risk:** 🟡 Medium

**Procedure:** [[Search SMB by Filename and Download Matches]]

> 📝 **Objective:** SMB shares often contain sensitive information, which can be easily enumerated. Tools such as smbmap can crawl a SMB share, looking for and downloading files which match certain name criteria.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 5]** Decrypt a Group Policy Preferences (GPP) Password

**Progress:** `█████░░░░░` 50% | **Risk:** 🟡 Medium

**Procedure:** [[Decrypt a Group Policy Preferences (GPP) Password]]

> 📝 **Objective:** Decrypt a Group Policy Preference Password using gpp-decrypt. While passwords contained in these GPP files are encrypted, Microsoft published the AES key, making decryption trivial. GPP files are often found on SYSVOL shares, as administrators use them to apply the same settings across multiple mac

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 6]** List All Active Directory Users

**Progress:** `██████░░░░` 60% | **Risk:** 🟡 Medium

**Procedure:** [[List All Active Directory Users]]

> 📝 **Objective:** Attackers with valid credentials to an Active Directory domain user can authenticate with a domain controller and list other users in the domain.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 7]** Query Domain for SPN and Attempt to Kerberoast (Authenticated)

**Progress:** `███████░░░` 70% | **Risk:** 🟡 Medium

**Procedure:** [[Query Domain for SPN and Attempt to Kerberoast (Authenticated)]]

> 📝 **Objective:** Sevrice principal names (SPN) are unique identifiers used by Kerberos authentication. Due to how Kerberos handles service tickets, attackers may be able to query a domain controller with valid credentials, make a request to the ticket granting service (TGT), and receive the hash of other accounts.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 8]** Identify a Password Hash (Hashcat)

**Progress:** `████████░░` 80% | **Risk:** 🟡 Medium

**Procedure:** [[Identify a Password Hash (Hashcat)]]

> 📝 **Objective:** Analyze a password hash to identify the type and Hashcat mode.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 9]** Brute Force Password Hashes (Hashcat)

**Progress:** `█████████░` 90% | **Risk:** 🔴 High

**Procedure:** [[Brute Force Password Hashes (Hashcat)]]

> 📝 **Objective:** Use Hashcat to brute force hashes with a dictionary. See Example Hashes for help identifying the mode.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

### **[Step 10]** Connect to Windows using PsExec (Authenticated)

**Progress:** `██████████` 100% | **Risk:** 🟡 Medium

**Procedure:** [[Connect to Windows using PsExec (Authenticated)]]

> 📝 **Objective:** Use PSExec to connect to a remote Windows system and spawn a Command shell  (cmd.exe). In order to use PSExec, the user must have full permissions to the "$ADMIN" share, which generally requires administrator credentials.

**Expected Output:**
- Refer to procedure documentation for details

**Success Indicators:** ✅ Objective achieved

---

## 🎯 Attack Chain Summary

### Key Achievements
- ✅ Connect to Windows using PsExec (Authenticated)
- ✅ Decrypt a Group Policy Preferences (GPP) Password
- ✅ List All Active Directory Users
- ✅ Search SMB by Filename and Download Matches
- ✅ Basic Port Scan with Service Enumeration
- ... and 5 more procedures

---

## 📈 Technique & Tactic Coverage

---

**Last Updated:** 2023-05-29T16:48:53.162677+00:00 | **Chain Version:** 2.0 Enhanced | **Status:** ⚠️ Draft
