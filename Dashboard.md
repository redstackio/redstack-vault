---
title: Redstack TTP Vault Dashboard
type: dashboard
created: 2025-01-22
---

# 🎯 Redstack TTP Vault Dashboard

> **Your comprehensive offensive security knowledge base**  
> Navigate by MITRE ATT&CK tactics, platforms, tools, or dive directly into procedures and commands.

---

## 📊 Quick Statistics

```dataview
TABLE WITHOUT ID
  ("**" + rows.file.name + "**") as "Category",
  length(rows) as "Count"
FROM ""
WHERE file.folder != "" AND file.folder != "_assets"
GROUP BY file.folder
SORT length(rows) DESC
LIMIT 10
```

### By Entity Type
- **Procedures**: 2,198 (126 with embedded images)
- **Commands**: 4,877
- **Techniques**: 337
- **Tools**: 820 (6 with embedded images)
- **Attack Chains**: 21
- **Cheatsheets**: 171
- **Payloads**: 10
- **Code Snippets**: 3,609
- **Tags**: 1,944

**Total Files**: 13,518 markdown documents

---

## 🗺️ Navigation Hubs

### 🎭 By MITRE ATT&CK Framework
Start with tactics and drill down to techniques and procedures.

**📋 [[MITRE-Framework|MITRE ATT&CK Framework Overview]]**

**Tactics** (Click to explore):
- 🔴 [[tactics/Initial Access|Initial Access]] - Entry points into target systems
- 🟠 [[tactics/Execution|Execution]] - Running malicious code
- 🟡 [[tactics/Persistence|Persistence]] - Maintaining access
- 🟢 [[tactics/Privilege Escalation|Privilege Escalation]] - Gaining higher permissions
- 🔵 [[tactics/Defense Evasion|Defense Evasion]] - Avoiding detection
- 🟣 [[tactics/Credential Access|Credential Access]] - Stealing credentials
- 🟤 [[tactics/Discovery|Discovery]] - Network and system reconnaissance
- ⚫ [[tactics/Lateral Movement|Lateral Movement]] - Moving through the network
- 🔴 [[tactics/Collection|Collection]] - Gathering target data
- 🟠 [[tactics/Command and Control|Command and Control]] - C2 communications
- 🟡 [[tactics/Exfiltration|Exfiltration]] - Data extraction
- 🟢 [[tactics/Impact|Impact]] - Destructive actions
- 🔵 [[tactics/Reconnaissance|Reconnaissance]] - Pre-attack intel gathering
- 🟣 [[tactics/Resource Development|Resource Development]] - Building attack infrastructure

---

### 💻 By Platform
Browse procedures and tools by target platform.

**[[Platforms/README|Platform Index]]**

- 🪟 [[Platforms/Windows|Windows]] - Most comprehensive coverage
- 🐧 [[Platforms/Linux|Linux]] - Unix/Linux systems
- 🍎 [[Platforms/macOS|macOS]] - Apple systems
- ☁️ [[Platforms/Cloud|Cloud]] - AWS, Azure, GCP
- 🌐 [[Platforms/Network|Network]] - Network infrastructure
- 📦 [[Platforms/Containers|Containers]] - Docker, Kubernetes
- 🌍 [[Platforms/Web|Web Applications]] - Web vulnerabilities

---

### 🛠️ By Tools & Frameworks
Find procedures that use specific tools.

**[[Tools-Index|Tools & Frameworks Index]]**

Popular Categories:
- C2 Frameworks (Metasploit, Cobalt Strike, Empire)
- Enumeration Tools (BloodHound, PowerView, ADRecon)
- Exploitation Frameworks
- Credential Dumping Tools
- Post-Exploitation Utilities

---

### ⛓️ Attack Chains
Pre-built attack sequences from initial access to objective.

**[[Attack-Chains-Index|Attack Chains Library]]** - 21 documented chains

Examples:
- [[attack-chains/Phishing to Domain Admin|Phishing → Domain Admin]]
- [[attack-chains/Web Shell to Internal Network|Web Shell → Internal Network]]
- [[attack-chains/Cloud Compromise Path|Cloud Infrastructure Compromise]]

---

## 🔍 Dynamic Queries

### Recently Updated Content
```dataview
TABLE file.mtime as "Last Modified", type as "Type"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
AND file.folder != "_assets"
SORT file.mtime DESC
LIMIT 20
```

### Verified Procedures
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics",
  platforms as "Platforms"
FROM "procedures"
WHERE verified = true
SORT file.name ASC
LIMIT 10
```

### Unverified High-Value Content
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  tactics as "Tactics",
  file.ctime as "Created"
FROM "procedures"
WHERE verified = false
AND (contains(tags, "high-impact") OR contains(tags, "critical"))
SORT file.ctime DESC
LIMIT 10
```

### Commands by Executor
```dataview
TABLE WITHOUT ID
  executor as "Executor",
  length(rows) as "Count"
FROM "commands"
GROUP BY executor
SORT length(rows) DESC
```

---

## 🔎 Advanced Search & Queries

### Search Tools
- **Quick Search**: `Cmd/Ctrl + O` - Search all files
- **Global Search**: `Cmd/Ctrl + Shift + F` - Full-text search
- **Graph View**: `Cmd/Ctrl + G` - Visualize relationships
- **Tag Browser**: Browse by #tags in right sidebar

### Pre-built Query Library
Explore the **[[Queries/README|Queries Folder]]** for advanced filters:
- [[Queries/verified-procedures|All Verified Procedures]]
- [[Queries/procedures-by-tactic|Procedures by Tactic]]
- [[Queries/procedures-by-platform|Procedures by Platform]]
- [[Queries/commands-by-executor|Commands by Executor]]
- [[Queries/tools-by-category|Tools by Category]]
- [[Queries/orphaned-content|Orphaned Content (needs links)]]

---

## 📚 Cross-Reference Pages

Quick access to filtered content:
- [[Cross-References/Windows-Persistence|All Windows Persistence Techniques]]
- [[Cross-References/Credential-Dumping|All Credential Dumping Methods]]
- [[Cross-References/AD-Enumeration|All Active Directory Enumeration]]
- [[Cross-References/Privilege-Escalation-Windows|Windows Privilege Escalation]]
- [[Cross-References/Lateral-Movement|Lateral Movement Techniques]]

---

## 📝 Templates & Workflows

### Adding New Content
- [[Templates/New-Procedure|Create New Procedure]]
- [[Templates/New-Tool|Add New Tool]]
- [[Templates/New-Attack-Chain|Build Attack Chain]]
- [[Templates/Verify-Procedure|Procedure Verification Checklist]]

### Testing & Engagement Tracking
- [[Testing/README|Testing Tracker]] - Track what you've tested
- [[Testing/Engagement-Template|Engagement Template]]
- Use Kanban boards for procedure testing status

---

## 🎓 Usage Tips

### For Red Team Operations
1. Start with **[[MITRE-Framework]]** to plan attack phases
2. Browse **[[Platforms/Windows]]** for target-specific procedures
3. Use **[[Tools-Index]]** to find alternatives for blocked tools
4. Build attack chains with **[[Attack-Chains-Index]]**

### For Blue Team / Detection
1. Review **[[Tactics]]** to understand attack progression
2. Check **verified** procedures for accurate detection patterns
3. Use graph view to see technique relationships
4. Cross-reference with your SIEM/EDR detections

### For Research & Learning
1. Browse by **[[Platforms]]** for platform-specific techniques
2. Use **Tags** to find related content
3. Explore **[[Attack-Chains-Index]]** for end-to-end scenarios
4. Check unverified content and contribute verifications

---

## 🤖 AI / RAG Integration

### AnythingLLM Queries
Query the vault semantically:
- "Find Windows privilege escalation techniques"
- "Show me alternatives to mimikatz"
- "Build an attack chain from phishing to domain admin"
- "What commands can enumerate Active Directory?"

### Setup Guide
See [[RAG-Guide]] for AnythingLLM and LangChain integration.

---

## 📈 Quality Metrics

### Content Verification Status
```dataview
TABLE WITHOUT ID
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status",
  length(rows) as "Count"
FROM "procedures"
GROUP BY verified
```

### Coverage by Platform
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

**[[Quality-Metrics|Full Quality Dashboard →]]**

---

## 🔗 Quick Links

### Documentation
- [[IMPLEMENTATION_ROADMAP|Implementation Roadmap]]
- [[IMAGE_EXTRACTION_SUMMARY|Image Extraction Report]]
- [[ATTACK_CHAINS_EXTRACTION_REPORT|Attack Chains Report]]

### External Resources
- [MITRE ATT&CK Website](https://attack.mitre.org/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [LOLBAS Project](https://lolbas-project.github.io/)

---

## 🎯 Getting Started

**New to the vault?** Start here:
1. Review this Dashboard to understand the structure
2. Explore [[MITRE-Framework]] for tactic-based navigation
3. Browse [[Platforms/Windows]] for the most comprehensive content
4. Try the [[Queries/README]] for dynamic filtering
5. Set up [[RAG-Guide|AI integration]] for semantic search

**Have questions or contributions?**
- Check [[Templates/Bug-Report|Bug Report Template]]
- Submit verification tests with [[Templates/Verify-Procedure]]
- Add new content using [[Templates/New-Procedure]]

---

*Last updated: 2025-01-22*  
*Total vault size: 13,518 files | Images: 1,603 (237 MB)*
