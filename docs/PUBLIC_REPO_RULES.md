# Public Repository Rules

This repository is public and must stay technical. It should not contain application material.

## Allowed in public GitHub

| Allowed | Examples |
|---|---|
| Technical documentation | architecture diagrams, ADRs, runbooks, README files |
| Portfolio projects | data pipelines, MLOps services, dashboards, synthetic datasets |
| Technical stack maps | Python libraries, cloud tools, DataOps/MLOps tooling |
| Certification mapping | public training/certification references without private documents |
| Governance evidence | model cards, data cards, risk assessment templates |
| Synthetic data | generated transactions, simulated client profiles, sample market notes |
| Security hygiene | `.gitignore`, `SECURITY.md`, sanitized examples |

## Not allowed in public GitHub

| Not allowed | Why |
|---|---|
| CV files | They are candidature material and should be customized privately |
| Cover letters | Employer-specific and not useful as public engineering evidence |
| Job application trackers | Private targeting and pipeline management |
| Salary targets | Poor public signal and not technical evidence |
| Recruiter messages | Private communication |
| Employer-specific strategy | Can create unnecessary bias or reduce neutrality |
| Real bank data | Confidentiality and compliance risk |
| Personal documents | Privacy and identity risk |
| Certificates with IDs | Private administrative evidence |
| Secrets and credentials | Security risk |

## Public style principle

Public GitHub should answer:

> Can this person build, document, operate and explain data/ML systems?

It should not answer:

> Which company is this person applying to this week?

## Sanitization checklist

Before every commit:

- [ ] no `.env` files;
- [ ] no API keys or tokens;
- [ ] no private SSH keys;
- [ ] no real hostnames or public IPs;
- [ ] no personal identity documents;
- [ ] no real client or bank data;
- [ ] no employer-specific applications;
- [ ] no salary targets;
- [ ] no screenshots with private data.

## Public wording rule

Use employer-neutral language:

> Swiss banking, regulated finance, financial infrastructure, large-scale data platforms.

Avoid public employer-specific claims:

> I am applying to X bank for Y position.

The employer-specific work belongs in private files, not public GitHub.
