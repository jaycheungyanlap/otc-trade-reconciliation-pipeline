\# Institutional OTC Derivatives Reconciliation Pipeline



# Institutional OTC Derivatives Reconciliation Pipeline

![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Domain](https://img.shields.io/badge/Domain-Middle%20Office%20%7C%20Ops%20Risk-orange)

An automated, modular, and audit-proof trade reconciliation engine built for Institutional Middle Office and Operational Risk management. It processes internal trade bookings against external broker feeds, auto-classifies discrepancies using in-memory SQL analytics, highlights large operational risks, and outputs structured Excel reports alongside `.eml` draft alerts.


\---



\## Key Features



\* \*\*In-Memory SQL Analytics Engine:\*\* Leverages `sqlite3` and `pandas` to execute `FULL OUTER JOIN` operations across trade populations, guaranteeing zero missing single-sided breaks.

\* \*\*Automated Risk-Based Categorization:\*\* Dynamically tags exceptions (`NOTIONAL\_MISMATCH`, `MISSING\_ON\_BROKER`, `MISSING\_IN\_HOUSE`) with configurable tolerance thresholds.

\* \*\*Large Break Alerting Mechanism:\*\* Automatically triggers `🚨 \[URGENT]` flags and deep-red visual highlights for high-exposure discrepancies ($500,000+).

\* \*\*Automated Visual Formatting:\*\* Employs `openpyxl` for dynamically formatted, color-coded executive reports with auto-fitted column dimensions.

\* \*\*Zero-Password EML Draft Launcher:\*\* Generates rich HTML `.eml` draft alerts with attached Excel workbooks for safe, human-in-the-loop review without managing raw credentials.

\* \*\*Audit Trail Compliance:\*\* Logs timestamps, execution statuses, and exception counts to `reco\_audit.log` for operational control.



\---



\## System Architecture



```text

&#x20;              ┌───────────────────────┐    ┌──────────────────────┐

&#x20;              │ internal\_trades.xlsx  │    │   broker\_feed.csv    │

&#x20;              └───────────┬───────────┘    └──────────┬───────────┘

&#x20;                          │                           │

&#x20;                          └─────────────┬─────────────┘

&#x20;                                        ▼

&#x20;                            ┌──────────────────────┐

&#x20;                            │  config.py (Rules)   │

&#x20;                            └───────────┬──────────┘

&#x20;                                        ▼

&#x20;                            ┌──────────────────────┐

&#x20;                            │  engine.py (SQLite)  │

&#x20;                            └───────────┬──────────┘

&#x20;                                        ▼

&#x20;                    ┌───────────────────┴───────────────────┐

&#x20;                    ▼                                       ▼

&#x20;        ┌───────────────────────┐               ┌───────────────────────┐

&#x20;        │  Daily\_Break\_Report   │               │   reco\_audit.log      │

&#x20;        │  (openpyxl Styled)    │               │   (Execution Trail)   │

&#x20;        └───────────┬───────────┘               └───────────────────────┘

&#x20;                    │

&#x20;                    ▼

&#x20;        ┌───────────────────────┐

&#x20;        │  notifier.py (.eml)   │

&#x20;        └───────────┬───────────┘

&#x20;                    ▼

&#x20;        ┌───────────────────────┐

&#x20;        │  Email Client Draft   │

&#x20;        │  (Large Break Alert)  │

&#x20;        └───────────────────────┘

