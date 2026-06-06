# Screen Flow Reference

Use this as the quick map for what the app should do and in what order.

## Recommended User Flow

1. Login with Google.
2. If no family exists, create one.
3. Add members to the family.
4. Land on the dashboard.
5. Use chat, food logging, meal planning, progress, reports, leaderboard, reminders, and admin from the shell.
6. If the user already has a family, the create-family screen should redirect them to that family's settings instead of creating a second family.

## Screen To Module Map

| Screen | Module | Expected Behavior |
|---|---|---|
| Create Family | Module 3 | Create the single family for the user, or show the existing-family notice and open family settings if one already exists. |
| Add / Edit Members | Module 4 | Add household members, edit profiles, goals, and health info. |
| Member Profile | Module 4 | View one member’s details, health markers, and history. |
| Dashboard | Module 10 | Show daily calories, protein, water, exercise, steps, trends, and scores. |
| Chat | Module 7 | WhatsApp-style coach chat with memory and meal-plan requests. |
| Food Logging | Module 8 | Log meals with text, later photo and voice, and estimate calories/protein. |
| Meal Planning | Module 9 | Generate vegetarian, Jain, or vegan plans. |
| Progress | Module 11 | Show weight, waist, and health-marker trends. |
| Reports | Module 12 | Show daily, weekly, monthly, and family reports with PDF export. |
| Leaderboard | Module 13 | Rank family members by adherence, improvement, activity, and consistency. |
| Reminders | Module 14 | Meal, water, walking, and medication reminders. |
| Admin / Security | Module 16 | Roles, audit logs, privacy controls, and family-wide admin tools. |

## Behavior Rules

- One user belongs to one family only.
- Create Family is a single-family onboarding screen: it creates the family when none exists, and otherwise routes the user to the existing family settings page.
- End users only have Family Admin and Family Member roles.
- There is no separate App Admin role in the MVP user flow.
- The family admin can manage any action inside that family.
- The dashboard is a post-onboarding screen, not the first screen for a new user.
- The mock shell is a navigation scaffold until each module becomes real.
