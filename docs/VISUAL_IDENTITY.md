# Visual Identity Guide

<div align="center">

**Public GitHub visual system for a premium technical portfolio**

Readable · Structured · Technical · Employer-neutral · Evidence-first

![Visual System](https://img.shields.io/badge/Visual%20System-Premium%20GitHub-1F6FEB?style=flat)
![Public Evidence](https://img.shields.io/badge/Public-Technical%20Evidence%20Only-24292F?style=flat)
![No Applications](https://img.shields.io/badge/No-CV%20or%20Applications-DC143C?style=flat)

</div>

---

## Purpose

This guide defines the visual style for the public GitHub profile and related portfolio repositories.

The goal is to make each repository understandable in less than 60 seconds while keeping the public profile technical, sober and employer-neutral.

---

## Visual principles

| Principle | Rule |
|---|---|
| Premium but sober | Dark blue background, clean badges, no noisy graphics |
| Evidence-first | Visuals must support technical proof, not decoration only |
| Employer-neutral | No company logos, no application material, no company-specific claims |
| Consistent structure | Same README flow across repositories |
| Safe public profile | No private identifiers, no secrets, no application content |

---

## Color palette

| Token | Hex | Use |
|---|---|---|
| Deep navy | `#07111F` | Main background |
| Steel navy | `#0B1F3A` | Secondary background |
| Data blue | `#58A6FF` | Data / cloud / technical accents |
| Reliability green | `#2EA043` | quality, monitoring, operational controls |
| Governance purple | `#A371F7` | AI governance, model risk, documentation |
| Warning red | `#DC143C` | public-safety and no-application notes |
| Soft text | `#D8E2F0` | secondary text |
| Muted text | `#9FB3C8` | subtitles and helper text |

---

## README layout standard

Every important repository should follow this structure:

```text
1. Visual banner
2. One-line summary
3. Badges
4. Executive summary
5. Documentation index
6. Problem statement
7. Architecture
8. Key features
9. Tech stack
10. Setup
11. Quality / controls
12. Portfolio signal
13. Non-goals / public-safety note
```

---

## Badge groups

### Profile-level badges

- LinkedIn
- Switzerland / target ecosystem
- regulated and data-intensive systems
- public technical evidence only
- no CV / application material
- synthetic or open data only

### Repository-level badges

- primary language;
- runtime;
- data store;
- workflow / scheduler;
- CI status when available;
- public-safety note;
- maturity level when ready.

---

## Visual assets

| Asset | Repository | Purpose |
|---|---|---|
| `assets/profile-banner.svg` | `KinSushi/KinSushi` | Premium profile header |
| `assets/profile-ecosystem.svg` | `KinSushi/KinSushi` | Portfolio architecture visual |
| `assets/infra-lab-banner.svg` | `sovralys-infra-lab` | Infrastructure lab header |
| `assets/pty-pipeline-banner.svg` | `pty-flights-pricing` | Data pipeline header |

---

## Public-safety visual rule

Never use visual assets to display:

- real hostnames;
- real IP addresses;
- real email addresses beyond public contact links;
- secrets;
- certificates with identifiers;
- employer-specific material;
- salary targets;
- private documents.

---

## Future visual assets

To create when the new repositories exist:

| Future repo | Banner direction |
|---|---|
| `banking-dataops-monitoring` | SQL controls, monitoring dashboard, quality gates |
| `fraud-mlops-control-tower` | MLflow lifecycle, API serving, model governance |
| `database-migration-quality-lab` | source-to-target migration, validation, reconciliation |
| `secure-wealth-rag-assistant` | document retrieval, privacy controls, evaluation |
| `jedha-rncp35288-portfolio` | six-block evidence map |
