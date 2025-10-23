---
title: Windows Platform
type: platform
platform: Windows
created: 2025-01-22
---

# 🪟 Windows Platform

> **Enterprise Windows environments - Active Directory, PowerShell, and more**  
> ~126 documented procedures for Windows exploitation

---

## 📊 Overview

Windows is the most targeted platform in enterprise environments, with extensive coverage of:
- Active Directory attacks
- PowerShell-based techniques
- Registry manipulation
- Service and DLL abuse
- Credential harvesting
- Privilege escalation

```dataview
TABLE WITHOUT ID
  choice(verified = true, "✅", "⚠️") as "✓",
  file.link as "Procedure",
  tactics as "Tactics"
FROM "procedures"
WHERE contains(platforms, "Windows")
SORT verified DESC, file.name ASC
```

---

## 🎯 By MITRE Tactic

### Initial Access
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Windows") 
AND contains(tactics, "[[Initial Access")
SORT file.name ASC
```

### Execution
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Windows") 
AND contains(tactics, "[[Execution")
SORT file.name ASC
```

### Persistence
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Windows") 
AND contains(tactics, "[[Persistence")
SORT file.name ASC
```

### Privilege Escalation
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Windows") 
AND contains(tactics, "[[Privilege Escalation")
SORT file.name ASC
```

### Defense Evasion
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Windows") 
AND contains(tactics, "[[Defense Evasion")
SORT file.name ASC
```

### Credential Access
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Windows") 
AND contains(tactics, "[[Credential Access")
SORT file.name ASC
```

### Discovery
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Windows") 
AND contains(tactics, "[[Discovery")
SORT file.name ASC
```

### Lateral Movement
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Windows") 
AND contains(tactics, "[[Lateral Movement")
SORT file.name ASC
```

---

## 🔑 Key Technique Categories

### Active Directory Attacks
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics",
  choice(verified = true, "✅", "⚠️") as "✓"
FROM "procedures"
WHERE contains(platforms, "Windows")
AND (
  contains(file.name, "Active Directory") OR
  contains(file.name, "AD ") OR
  contains(file.name, "Kerberos") OR
  contains(file.name, "Domain") OR
  contains(tags, "active-directory")
)
SORT file.name ASC
```

### PowerShell Exploitation
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics",
  choice(verified = true, "✅", "⚠️") as "✓"
FROM "procedures"
WHERE contains(platforms, "Windows")
AND (
  contains(file.name, "PowerShell") OR
  contains(tags, "powershell")
)
SORT file.name ASC
```

### Credential Dumping
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics",
  choice(verified = true, "✅", "⚠️") as "✓"
FROM "procedures"
WHERE contains(platforms, "Windows")
AND (
  contains(file.name, "Credential") OR
  contains(file.name, "LSASS") OR
  contains(file.name, "Mimikatz") OR
  contains(file.name, "Password")
)
SORT file.name ASC
```

### Registry Manipulation
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics",
  choice(verified = true, "✅", "⚠️") as "✓"
FROM "procedures"
WHERE contains(platforms, "Windows")
AND (
  contains(file.name, "Registry") OR
  contains(tags, "registry")
)
SORT file.name ASC
```

### Service & DLL Abuse
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics",
  choice(verified = true, "✅", "⚠️") as "✓"
FROM "procedures"
WHERE contains(platforms, "Windows")
AND (
  contains(file.name, "Service") OR
  contains(file.name, "DLL") OR
  contains(tags, "service") OR
  contains(tags, "dll")
)
SORT file.name ASC
```

---

## 🛠️ Windows-Specific Tools

```dataview
TABLE WITHOUT ID
  file.link as "Tool",
  category as "Category",
  description as "Description"
FROM "tools"
WHERE contains(platforms, "Windows") OR contains(tags, "windows")
SORT file.name ASC
```

---

## 📈 Statistics

### Verification Status
```dataview
TABLE WITHOUT ID
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status",
  length(rows) as "Count"
FROM "procedures"
WHERE contains(platforms, "Windows")
GROUP BY verified
```

### Top Tactics
```dataview
TABLE WITHOUT ID
  tactics as "Tactic",
  length(rows) as "Procedures"
FROM "procedures"
WHERE contains(platforms, "Windows") AND tactics != null
FLATTEN tactics
GROUP BY tactics
SORT length(rows) DESC
```

---

## 🎯 Common Attack Paths

### Domain Compromise Path
1. **Initial Access** → Phishing, exposed RDP
2. **Execution** → PowerShell, WMI
3. **Discovery** → AD enumeration (BloodHound, PowerView)
4. **Credential Access** → LSASS dump, Kerberoasting
5. **Lateral Movement** → Pass-the-Hash, WinRM
6. **Privilege Escalation** → Token manipulation, Group Policy
7. **Domain Admin** → DCSync, Golden Ticket

### Local Privilege Escalation Path
1. **Execution** → Initial foothold
2. **Discovery** → System enumeration (WinPEAS, PowerUp)
3. **Find Weakness** → Unquoted service paths, weak permissions
4. **Exploit** → Service abuse, DLL hijacking
5. **Escalate** → SYSTEM access

---

## 🔗 Related Resources

### Internal Links
- [[Platforms/README|← All Platforms]]
- [[MITRE-Framework|Browse by Tactic]]
- [[Tools-Index|Windows Tools]]
- [[Queries/windows-specific|Windows Query Library]]

### Cross-References
- [[Cross-References/Windows-Persistence|All Windows Persistence Techniques]]
- [[Cross-References/Windows-PrivEsc|Windows Privilege Escalation]]
- [[Cross-References/AD-Enumeration|Active Directory Enumeration]]

### External Resources
- [Windows Security Documentation](https://docs.microsoft.com/en-us/windows/security/)
- [Active Directory Security](https://adsecurity.org/)
- [LOLBAS Project](https://lolbas-project.github.io/)
- [PayloadsAllTheThings - Windows](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources)

---

*Last updated: 2025-01-22*  
*Windows Procedures: ~126 | Tools: Check query above*
