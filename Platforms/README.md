---
title: Platform Navigation
type: navigation
created: 2025-01-22
---

# 💻 Platform-Based Navigation

> **Browse procedures, techniques, and tools by target platform**  
> Filter content for Windows, Linux, macOS, Cloud, Web, Network, and Container environments

---

## 📊 Platform Coverage

```dataview
TABLE WITHOUT ID
  platforms as "Platform",
  length(rows) as "Procedures"
FROM "procedures"
WHERE platforms != null
FLATTEN platforms
GROUP BY platforms
SORT length(rows) DESC
```

### Quick Stats
- **Web Applications**: ~260 procedures (SQL injection, XSS, SSRF, etc.)
- **Windows**: ~126 procedures (AD attacks, PowerShell, registry, etc.)
- **Linux**: ~64 procedures (privilege escalation, persistence, etc.)
- **Cloud**: ~46 procedures (AWS, Azure, GCP)
- **Network**: Infrastructure and protocol attacks
- **Containers**: Docker, Kubernetes exploitation
- **macOS**: Apple system techniques

---

## 🗺️ Browse by Platform

### 🪟 [[Platforms/Windows|Windows]]
The most comprehensive platform coverage for enterprise environments.

**Top Categories:**
- Active Directory attacks
- PowerShell exploitation
- Registry manipulation
- Service abuse
- Credential dumping

```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics"
FROM "procedures"
WHERE contains(platforms, "Windows")
SORT file.name ASC
LIMIT 10
```

[View all Windows procedures →](Windows.md)

---

### 🐧 [[Platforms/Linux|Linux]]
Unix and Linux system exploitation techniques.

**Top Categories:**
- Privilege escalation
- SSH attacks
- Kernel exploits
- Container escapes
- Sudo abuse

```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics"
FROM "procedures"
WHERE contains(platforms, "Linux")
SORT file.name ASC
LIMIT 10
```

[View all Linux procedures →](Linux.md)

---

### 🍎 [[Platforms/macOS|macOS]]
Apple macOS and OS X specific techniques.

**Top Categories:**
- Keychain access
- LaunchAgents/Daemons
- SIP bypass
- Code signing abuse

```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics"
FROM "procedures"
WHERE contains(platforms, "Mac") OR contains(platforms, "macOS") OR contains(platforms, "OSx")
SORT file.name ASC
LIMIT 10
```

[View all macOS procedures →](macOS.md)

---

### ☁️ [[Platforms/Cloud|Cloud]]
Cloud platform attacks (AWS, Azure, GCP).

**Top Categories:**
- IAM exploitation
- Storage enumeration
- Lambda/Functions abuse
- Metadata service SSRF
- Resource hijacking

```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics"
FROM "procedures"
WHERE contains(platforms, "Cloud") OR contains(platforms, "AWS") OR contains(platforms, "Azure") OR contains(platforms, "GCP")
SORT file.name ASC
LIMIT 10
```

[View all Cloud procedures →](Cloud.md)

---

### 🌍 [[Platforms/Web|Web Applications]]
Web application vulnerabilities and exploitation.

**Top Categories:**
- SQL Injection
- Cross-Site Scripting (XSS)
- SSRF attacks
- XXE exploitation
- Authentication bypass
- CORS misconfiguration

```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics"
FROM "procedures"
WHERE contains(platforms, "Web")
SORT file.name ASC
LIMIT 10
```

[View all Web procedures →](Web.md)

---

### 🌐 [[Platforms/Network|Network]]
Network infrastructure and protocol attacks.

**Top Categories:**
- MITM attacks
- DNS poisoning
- LLMNR/NBT-NS poisoning
- SMB relay
- Network reconnaissance

```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics"
FROM "procedures"
WHERE contains(platforms, "Network")
SORT file.name ASC
LIMIT 10
```

[View all Network procedures →](Network.md)

---

### 📦 [[Platforms/Containers|Containers]]
Container and orchestration platform exploitation.

**Top Categories:**
- Docker escape
- Kubernetes abuse
- Container registry attacks
- Privilege escalation
- Secrets extraction

```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics"
FROM "procedures"
WHERE contains(platforms, "Container") OR contains(platforms, "Docker") OR contains(platforms, "Kubernetes")
SORT file.name ASC
LIMIT 10
```

[View all Container procedures →](Containers.md)

---

## 🔍 Cross-Platform Techniques

Some techniques work across multiple platforms:

```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  platforms as "Platforms",
  tactics as "Tactics"
FROM "procedures"
WHERE platforms != null AND length(platforms) > 1
SORT length(platforms) DESC, file.name ASC
LIMIT 15
```

---

## 🛠️ Tools by Platform

### Windows Tools
```dataview
TABLE WITHOUT ID
  file.link as "Tool",
  category as "Category"
FROM "tools"
WHERE contains(platforms, "Windows") OR contains(tags, "windows")
SORT file.name ASC
LIMIT 10
```

### Linux Tools
```dataview
TABLE WITHOUT ID
  file.link as "Tool",
  category as "Category"
FROM "tools"
WHERE contains(platforms, "Linux") OR contains(tags, "linux")
SORT file.name ASC
LIMIT 10
```

---

## 📈 Platform Statistics

### Procedures by Platform
```dataview
TABLE WITHOUT ID
  platforms as "Platform",
  length(rows.file.link) as "Total Procedures",
  length(filter(rows, (r) => r.verified = true)) as "Verified"
FROM "procedures"
WHERE platforms != null
FLATTEN platforms
GROUP BY platforms
SORT length(rows) DESC
```

### Most Documented Platform-Tactic Combinations
```dataview
TABLE WITHOUT ID
  platforms as "Platform",
  tactics as "Tactic",
  length(rows) as "Procedures"
FROM "procedures"
WHERE platforms != null AND tactics != null
FLATTEN platforms
FLATTEN tactics
GROUP BY platforms, tactics
SORT length(rows) DESC
LIMIT 20
```

---

## 🎯 Navigation Paths

### For Penetration Testing
1. Identify target platform
2. Browse relevant procedures
3. Check tools available for platform
4. Build attack chain with platform-specific techniques

### For Red Team Operations
1. Start with [[Platforms/Web]] for initial access
2. Pivot to [[Platforms/Windows]] for internal network
3. Use [[Platforms/Linux]] for server compromise
4. Leverage [[Platforms/Cloud]] for cloud resources

### For Security Research
1. Compare techniques across platforms
2. Identify cross-platform patterns
3. Study platform-specific mitigations
4. Contribute new procedures

---

## 🔗 Related Navigation

- [[Dashboard|← Back to Dashboard]]
- [[MITRE-Framework|Browse by MITRE ATT&CK →]]
- [[Tools-Index|Browse by Tools →]]
- [[Attack-Chains-Index|View Attack Chains →]]

---

## 💡 Usage Tips

### Finding Platform-Specific Techniques
1. Click on platform page (e.g., [[Platforms/Windows]])
2. Browse Dataview query results
3. Use Quick Search (`Cmd/Ctrl + O`) within platform folder
4. Filter by tactic using [[Queries/procedures-by-platform]]

### Comparing Platforms
- Use the Cross-Platform Techniques query above
- Check the Platform Statistics section
- Use Graph View to see relationships
- Compare tool availability across platforms

### Contributing
- Add platform metadata to procedures missing it
- Verify existing procedures on your platform
- Submit new platform-specific techniques
- Update tools with platform compatibility

---

*Last updated: 2025-01-22*  
*Platforms: 7 | Procedures: 2,198 | Tools: 820*
