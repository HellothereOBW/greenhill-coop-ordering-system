# Greenhill Food Co-op Ordering Management System

## Project Charter

## 1. General Project Information

| Item | Details |
| --- | --- |
| Project Name | Greenhill Food Co-op Ordering Management System |
| Project Manager | Yuhang Zheng |
| Project Sponsor | To be confirmed |
| Team Members | Yuhang Zheng – Team Lead; Xuan Xie – Financial Analyst; Bowen Zhou – Developer |
| Project Start | Project initiation/planning phase: August 2026; Sprint 1 starts 7 September 2026 |
| Target Completion | Core working system targeted before the October 2026 Harvest Day round |
| Delivery Format | Python web application delivered through a GitHub repository with source code and README |
| Methodology | Agile / Scrum-style three-week sprint, preceded by a two-week initiation and planning phase |

## 2. Project Overview

### 2.1 Background and Problem Statement

Greenhill Food Co-op currently relies on paper order forms and manual spreadsheet entry. Ngaire, the paid coordinator, spends approximately three to four hours every Sunday night typing paper orders into a spreadsheet. This creates a single point of failure and contributes to order errors, difficulty matching bank transfers to members, and discrepancies between packing sheets and the contents of crates.

### 2.2 Business Need / Justification

The project is needed to reduce the coordinator's manual order-entry workload and improve the accuracy and usability of the co-op's order-management process. A web-based ordering system will allow members to enter their own orders and will provide the coordinator with consolidated product totals and structured order information.

### 2.3 Project Purpose

The purpose of the project is to create a practical ordering management system that supports member and product management, accurate order processing, round management, and coordinator packing preparation without expanding into payment, banking, accounting, or inventory management.

## 3. Project Objectives

- Reduce reliance on manual transcription of paper orders by enabling members to enter orders through a web application.

- Provide accurate support for both per-unit and per-kilogram product pricing.

- Allow orders to be created, viewed, edited, and cancelled within an ordering round.

- Provide a product-totalled view that helps the coordinator prepare packing activities.

- Support proxy ordering for members who cannot place orders online.

- Preserve historical pricing by storing the unit price on each order line when the order is placed.

- Record actual packed quantities and substitutions so adjustments can be made when supply is short.

- Deliver a working core system before the October 2026 Harvest Day round.

## 4. Scope

### 4.1 In Scope

- Member management.

- Product management.

- Per-unit and per-kilogram pricing logic.

- Order creation, viewing, editing, and cancellation.

- Ordering-round state management.

- Coordinator product-totalled view.

- Proxy ordering by the coordinator or volunteer on behalf of a member.

- Packing-sheet support, including actual quantity packed and substitution notes.

- Storage of the price applicable at the time an order line is placed.

- Exact calculation and storage of order amounts without forced rounding.

### 4.2 Out of Scope

- Payment processing.

- Bank reconciliation.

- Accounting integration.

- SMS and email notifications.

- Delivery management.

- A full inventory-management system.

These items may remain in the product backlog for future consideration but are excluded from the current project scope.

## 5. Key Stakeholders

| Item | Details |
| --- | --- |
| Ngaire – Coordinator | Primary operational stakeholder; wants reduced manual work and an efficient ordering process. |
| Bao – Packing Volunteer | Needs accurate, practical packing sheets and a way to record actual quantities and substitutions. |
| Doug – Treasurer | Needs pricing accuracy, historical prices, exact totals, and an audit trail for adjustments. |
| Project Team | Responsible for requirements, design, development planning, documentation, and delivery. |
| Greenhill Food Co-op Members | Users who place orders; some members may require proxy ordering. |

## 6. Project Roles and Responsibilities

| Item | Details |
| --- | --- |
| Yuhang Zheng – Project Manager / Team Lead | Project coordination, planning, scope management, Confluence setup, GitHub/base framework, and team leadership. |
| Xuan Xie – Financial Analyst | Financial considerations, database/ER design, pricing and historical-price requirements, and WBS/Gantt chart. |
| Bowen Zhou – Developer | Technical development planning, project charter, Jira product backlog, and application development responsibilities. |
| All Team Members | Stakeholder/risk identification, requirements discussion, decisions, review, and project documentation. |

## 7. Proposed Methodology

The project will use an Agile / Scrum-style approach. The first two weeks are dedicated to project initiation and planning, with no coding planned during this phase. The team will complete the project charter, WBS and Gantt chart, Confluence space, and Jira product backlog. Sprint 1 then begins on 7 September 2026 and is planned as a three-week sprint focused on delivering a working core system.

## 8. Timeline and Milestones

| Milestone | Date | Notes |
| --- | --- | --- |
| Project initiation and planning documents completed | 4 September 2026 | Charter, WBS and Gantt chart |
| Product backlog completed | 4 September 2026 | Jira backlog and prioritisation |
| Sprint 1 starts | 7 September 2026 | Three-week sprint |
| Core working system ready | Before October 2026 Harvest Day | Required for the high-volume October round |

## 9. Expected Deliverables

- Project Charter.

- Work Breakdown Structure (WBS) and Gantt chart.

- Confluence project space and documentation.

- Prioritised Jira product backlog.

- Database ER diagram.

- Python web application for ordering management.

- GitHub repository containing the source code.

- README explaining how to run the application from a clean checkout.

- Packing-sheet functionality supporting actual quantities and substitution notes.

## 10. Success Criteria / Metrics

- The core ordering-management workflow is functional and usable before the October Harvest Day round.

- Members can create, view, edit, and cancel orders within an ordering round.

- Per-unit and per-kilogram pricing calculations produce correct totals, including mixed orders.

- Historical unit prices are retained on order lines.

- Exact order totals are stored and displayed without forced ten-cent rounding.

- The coordinator can view product-totalled order information for packing preparation.

- Proxy ordering is available for members who cannot order online.

- Packing records can capture actual quantities and substitution notes.

- The application can be obtained from GitHub and run from a clean checkout using the provided README.

## 11. Risks, Constraints, and Assumptions

### 11.1 Initial Risks

| Item | Details |
| --- | --- |
| Per-kilogram pricing logic may be implemented incorrectly | Use dedicated automated tests for mixed per-unit/per-kilogram orders and verify both individual-order and round totals. |
| Printed packing sheet may not be practical for the Thursday shift | Confirm required fields/layout with Bao and provide an early print preview for feedback. |
| Members who are not online cannot place their own orders | Provide proxy ordering so Ngaire or a volunteer can enter an order on behalf of a member. |
| Short supply may require changes to packed quantities | Record actual quantity packed and substitution notes and retain the records for charge adjustments. |

### 11.2 Constraints

- The current project scope is limited to order management.

- The system must support the operational requirement of printing/using packing information, including in a hall with no Wi-Fi.

- The project has a fixed operational deadline associated with the October Harvest Day round.

- The first two weeks are reserved for initiation and planning rather than coding.

### 11.3 Assumptions

- Stakeholders will provide feedback on requirements and packing-sheet design.

- The project team will have access to the required development tools and GitHub.

- The co-op's product, member, and order information required for development will be available to the team.

- The three-week sprint can deliver the core functionality required for the October round.

Note: These assumptions are planning assumptions derived from the project information; they should be confirmed with the project sponsor/stakeholders.

## 12. Required Tools and Resources

- Python development environment.

- Flask or Django web framework.

- GitHub repository.

- Confluence for project documentation.

- Jira for the product backlog.

- Database and ER-diagram design tools.

- Testing tools for pricing and order-total logic.

- Printing capability for packing sheets.

## 13. Initial Cost / Budget

A project budget or cost estimate was not specified in the provided meeting minutes. Therefore, the budget should be confirmed with the project sponsor before the charter is formally approved.

## 14. Governance and Approval

The project charter should be reviewed by the project team and approved by the project sponsor before being treated as the baseline for project execution.

| Item | Details |
| --- | --- |
| Project Sponsor | Name: To be confirmed<br>Signature: ____________________<br>Date: ____________________ |
| Project Manager | Yuhang Zheng<br>Signature: ____________________<br>Date: ____________________ |
| Team Lead | Yuhang Zheng<br>Signature: ____________________<br>Date: ____________________ |
| Team Member | Bowen Zhou<br>Signature: ____________________<br>Date: ____________________ |
| Team Member | Xuan Xie<br>Signature: ____________________<br>Date: ____________________ |

## 15. Charter Summary

This charter establishes the Greenhill Food Co-op Ordering Management System as an order-management project focused on reducing manual order entry and improving order accuracy. The project will use a Python web application and Agile-style delivery, with a three-week sprint beginning 7 September 2026. The core system is intended to be usable before the October Harvest Day round.