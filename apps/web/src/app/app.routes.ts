import { Route, Routes } from '@angular/router';
import { authGuard } from './core/guards/auth.guard';
import { MockFeaturePageData } from './shared/components/mock-feature-page/mock-feature-page.model';

const mockFeaturePage = (path: string, page: MockFeaturePageData): Route => ({
  path,
  loadComponent: () =>
    import('./shared/components/mock-feature-page/mock-feature-page.component').then(
      (m) => m.MockFeaturePageComponent
    ),
  data: { page }
});

export const routes: Routes = [
  {
    path: 'login',
    loadComponent: () =>
      import('./features/auth/login/login.component').then((m) => m.LoginComponent)
  },
  {
    path: 'auth/callback',
    loadComponent: () =>
      import('./features/auth/callback/auth-callback.component').then(
        (m) => m.AuthCallbackComponent
      )
  },
  {
    path: '',
    canActivate: [authGuard],
    loadComponent: () =>
      import('./shared/components/app-shell/app-shell.component').then((m) => m.AppShellComponent),
    children: [
      {
        path: '',
        pathMatch: 'full',
        redirectTo: 'dashboard'
      },
      {
        path: 'dashboard',
        loadComponent: () =>
          import('./features/dashboard/dashboard.component').then((m) => m.DashboardComponent)
      },
      {
        path: 'families/new',
        loadComponent: () =>
          import('./features/family/create-family/create-family.component').then(
            (m) => m.CreateFamilyComponent
          )
      },
      {
        path: 'families/:familyId/settings',
        loadComponent: () =>
          import('./features/family/family-settings/family-settings.component').then(
            (m) => m.FamilySettingsComponent
          )
      },
      mockFeaturePage('members', {
        eyebrow: 'Module 4',
        title: 'Member management',
        description:
          'Add parents, children, and grandparents, then track health history, goals, and profile details in one flow.',
        summary: 'Member list, profile, health metrics, and edit flow.',
        primaryAction: {
          label: 'Open member profile',
          link: '/members/anna'
        },
        secondaryAction: {
          label: 'Create family',
          link: '/families/new'
        },
        cards: [
          {
            title: 'Member list',
            value: 'One household, many profiles',
            hint: 'Switch between family members and keep each health profile separated.'
          },
          {
            title: 'Health info',
            value: 'Vitals and markers',
            hint: 'Height, weight, waist, HbA1c, LDL, HDL, triglycerides, vitamin D, and hemoglobin.'
          },
          {
            title: 'Goals',
            value: 'Weight, waist, energy, stamina',
            hint: 'Each member can carry their own targets and history.'
          },
          {
            title: 'Access',
            value: 'Admin and member views',
            hint: 'Family admins edit; members view their own profile and reports.'
          }
        ],
        steps: [
          'Open the member list from the sidebar.',
          'Create or edit a profile with personal and health details.',
          'Move into a single member view for health tracking and reports.'
        ],
        links: [
          { label: 'Dashboard', link: '/dashboard' },
          { label: 'Chat', link: '/chat' },
          { label: 'Reports', link: '/reports' }
        ]
      }),
      mockFeaturePage('members/:memberId', {
        eyebrow: 'Member profile',
        title: 'Anna profile',
        description:
          'A single-member profile view for measurements, medications, goals, and daily trends.',
        summary: 'Profile details, health markers, and progress history.',
        primaryAction: {
          label: 'Edit member',
          link: '/members'
        },
        secondaryAction: {
          label: 'Review reports',
          link: '/reports'
        },
        cards: [
          {
            title: 'Current state',
            value: 'Ready for review',
            hint: 'This mock view stands in for the member detail screen.'
          },
          {
            title: 'Markers',
            value: 'Tracked over time',
            hint: 'Use this screen to follow HbA1c, LDL, waist, and weight trends.'
          }
        ],
        steps: [
          'Pick a member from the household list.',
          'Open the profile detail view.',
          'Review goals, logs, and health markers.'
        ],
        links: [
          { label: 'Members', link: '/members' },
          { label: 'Chat', link: '/chat' },
          { label: 'Progress', link: '/progress' }
        ]
      }),
      mockFeaturePage('chat', {
        eyebrow: 'Module 7',
        title: 'AI health coach chat',
        description:
          'A WhatsApp-style thread for meal logging, meal plans, reminders, and long-term memory for each member.',
        summary: 'Conversation history and personal coaching flow.',
        primaryAction: {
          label: 'Open meal log',
          link: '/food-logs'
        },
        secondaryAction: {
          label: 'Open meal plans',
          link: '/meal-plans'
        },
        cards: [
          {
            title: 'Conversation',
            value: 'Chat-first workflow',
            hint: 'Users type natural language and the AI responds in context.'
          },
          {
            title: 'Memory',
            value: 'Family and member context',
            hint: 'Every message can build on the household and health history.'
          },
          {
            title: 'Actions',
            value: 'Plan, review, and track',
            hint: 'Use chat to create plans or record meals without leaving the app.'
          },
          {
            title: 'Tone',
            value: 'Coach, tracker, partner',
            hint: 'The assistant nudges, reviews, and keeps people accountable.'
          }
        ],
        steps: [
          'Choose a family member.',
          'Type a meal or ask for a plan.',
          'Review the AI reply and keep the conversation history.'
        ],
        links: [
          { label: 'Food logging', link: '/food-logs' },
          { label: 'Meal plans', link: '/meal-plans' },
          { label: 'Reminders', link: '/reminders' }
        ]
      }),
      mockFeaturePage('food-logs', {
        eyebrow: 'Module 8',
        title: 'Food logging',
        description:
          'Log meals by typing, uploading a photo, speaking, or using natural language, then turn them into structured entries.',
        summary: 'Manual, voice, photo, and natural language logging.',
        primaryAction: {
          label: 'Start a log',
          link: '/chat'
        },
        secondaryAction: {
          label: 'Review meal plan',
          link: '/meal-plans'
        },
        cards: [
          {
            title: 'Natural language',
            value: 'Poha, tea, roti, dal',
            hint: 'The app can estimate calories and protein from simple text.'
          },
          {
            title: 'Photo input',
            value: 'Meal image upload',
            hint: 'Later modules add multimodal review and recognition.'
          },
          {
            title: 'Voice input',
            value: 'Speech to meal entry',
            hint: 'Speak the meal and store it as structured data.'
          },
          {
            title: 'Tracking',
            value: 'Daily totals',
            hint: 'Feeds the dashboard, reports, and progress views.'
          }
        ],
        steps: [
          'Capture or type the meal.',
          'Convert it into calories and protein.',
          'Save it into the daily log for the selected member.'
        ],
        links: [
          { label: 'Chat', link: '/chat' },
          { label: 'Daily dashboard', link: '/dashboard' },
          { label: 'Reports', link: '/reports' }
        ]
      }),
      mockFeaturePage('meal-plans', {
        eyebrow: 'Module 9',
        title: 'Meal planning',
        description:
          'Generate vegetarian, Jain, or vegan meal plans with calorie and protein targets tuned to the selected member.',
        summary: 'Personalized meal plans and daily suggestions.',
        primaryAction: {
          label: 'Open chat',
          link: '/chat'
        },
        secondaryAction: {
          label: 'Review progress',
          link: '/progress'
        },
        cards: [
          {
            title: 'Diet rules',
            value: 'Vegetarian, Jain, vegan',
            hint: 'No other diet modes are shown in the app.'
          },
          {
            title: 'Targets',
            value: 'Calories and protein',
            hint: 'Plans can respect the family goals and the member profile.'
          },
          {
            title: 'Timing',
            value: 'Meal windows',
            hint: 'Meal timing preferences can influence the plan layout.'
          },
          {
            title: 'Follow-up',
            value: 'Adherence review',
            hint: 'The coach can compare plan versus actual logs later in the flow.'
          }
        ],
        steps: [
          'Choose a family member.',
          'Ask for tomorrow’s plan.',
          'Review suggestions and send the result back to chat.'
        ],
        links: [
          { label: 'Food logging', link: '/food-logs' },
          { label: 'Dashboard', link: '/dashboard' },
          { label: 'Progress', link: '/progress' }
        ]
      }),
      mockFeaturePage('progress', {
        eyebrow: 'Module 11',
        title: 'Progress tracking',
        description:
          'Review weight, waist, energy, stamina, and health marker trends across time for each member.',
        summary: 'Trend charts and goal progress review.',
        primaryAction: {
          label: 'Open reports',
          link: '/reports'
        },
        secondaryAction: {
          label: 'Open leaderboard',
          link: '/leaderboard'
        },
        cards: [
          {
            title: 'Body metrics',
            value: 'Weight and waist',
            hint: 'Watch the most visible trend lines first.'
          },
          {
            title: 'Markers',
            value: 'HbA1c, LDL, HDL',
            hint: 'Add health-marker tracking as the data becomes available.'
          },
          {
            title: 'Energy scores',
            value: 'Daily check-ins',
            hint: 'Use short scores to track how the member feels and performs.'
          },
          {
            title: 'Goal movement',
            value: 'Trend over time',
            hint: 'Compare current state with the target set in the profile.'
          }
        ],
        steps: [
          'Pick a member.',
          'Review the latest measurements and scores.',
          'Compare the trend against the member’s goal set.'
        ],
        links: [
          { label: 'Reports', link: '/reports' },
          { label: 'Daily dashboard', link: '/dashboard' },
          { label: 'Member profile', link: '/members/anna' }
        ]
      }),
      mockFeaturePage('reports', {
        eyebrow: 'Module 12',
        title: 'Reports and PDF generation',
        description:
          'Daily, weekly, monthly, and family reports come together here with downloadable PDFs for admins.',
        summary: 'Reporting center and export flow.',
        primaryAction: {
          label: 'Open leaderboard',
          link: '/leaderboard'
        },
        secondaryAction: {
          label: 'Open family settings',
          link: '/families/1/settings'
        },
        cards: [
          {
            title: 'Daily',
            value: 'Meal and activity summary',
            hint: 'Short-form snapshot for each member.'
          },
          {
            title: 'Weekly',
            value: 'Adherence and progress',
            hint: 'Highlight what moved and what stalled.'
          },
          {
            title: 'Monthly',
            value: 'Goal review',
            hint: 'A larger view for family admins and coaches.'
          },
          {
            title: 'PDF export',
            value: 'Downloadable reports',
            hint: 'Shareable output for family records and review.'
          }
        ],
        steps: [
          'Choose the report window.',
          'Review the summary cards and trends.',
          'Export the PDF if the family admin needs a copy.'
        ],
        links: [
          { label: 'Progress', link: '/progress' },
          { label: 'Leaderboard', link: '/leaderboard' },
          { label: 'Admin', link: '/admin' }
        ]
      }),
      mockFeaturePage('leaderboard', {
        eyebrow: 'Module 13',
        title: 'Family leaderboard',
        description:
          'Compare adherence, improvement, activity, and consistency inside each family in a friendly ranking view.',
        summary: 'Healthy competition and consistency view.',
        primaryAction: {
          label: 'Open reminders',
          link: '/reminders'
        },
        secondaryAction: {
          label: 'Open reports',
          link: '/reports'
        },
        cards: [
          {
            title: 'Best adherence',
            value: 'Who followed the plan',
            hint: 'Rewards the most consistent daily behavior.'
          },
          {
            title: 'Most improved',
            value: 'Who moved the most',
            hint: 'Shows the biggest positive change over time.'
          },
          {
            title: 'Highest activity',
            value: 'Steps and movement',
            hint: 'Useful for walking and stamina goals.'
          },
          {
            title: 'Most consistent',
            value: 'Habit building',
            hint: 'Recognize the person who keeps showing up.'
          }
        ],
        steps: [
          'Collect daily and weekly scores.',
          'Rank each family member by the chosen metric.',
          'Show the leaderboard inside the family area.'
        ],
        links: [
          { label: 'Dashboard', link: '/dashboard' },
          { label: 'Progress', link: '/progress' },
          { label: 'Reminders', link: '/reminders' }
        ]
      }),
      mockFeaturePage('reminders', {
        eyebrow: 'Module 14',
        title: 'Reminders',
        description:
          'Schedule meal, water, walking, and medication reminders so the coach stays present throughout the day.',
        summary: 'Reminder center for the household.',
        primaryAction: {
          label: 'Open chat',
          link: '/chat'
        },
        secondaryAction: {
          label: 'Review family settings',
          link: '/families/1/settings'
        },
        cards: [
          {
            title: 'Meal reminders',
            value: 'Prompt to eat on time',
            hint: 'Useful for maintaining a steady routine.'
          },
          {
            title: 'Water reminders',
            value: 'Hydration check-ins',
            hint: 'Helps keep the day balanced and visible.'
          },
          {
            title: 'Walking reminders',
            value: 'Movement nudges',
            hint: 'Supports activity and stamina goals.'
          },
          {
            title: 'Medication reminders',
            value: 'Adherence prompts',
            hint: 'Keeps the medical routine in view.'
          }
        ],
        steps: [
          'Set reminder type and time.',
          'Choose which family member should receive it.',
          'Review the delivery status and feedback later.'
        ],
        links: [
          { label: 'Chat', link: '/chat' },
          { label: 'Reports', link: '/reports' },
          { label: 'Progress', link: '/progress' }
        ]
      }),
      mockFeaturePage('admin', {
        eyebrow: 'Module 16',
        title: 'Security, audit, and admin',
        description:
          'A mock admin surface for roles, audit logs, privacy settings, and family-wide access control.',
        summary: 'Admin and compliance controls.',
        primaryAction: {
          label: 'Open family settings',
          link: '/families/1/settings'
        },
        secondaryAction: {
          label: 'Open dashboard',
          link: '/dashboard'
        },
        cards: [
          {
            title: 'Roles',
            value: 'Admin and member',
            hint: 'Control who can edit the family and who can only view.'
          },
          {
            title: 'Audit logs',
            value: 'Review changes',
            hint: 'Keep a trace of sensitive updates and actions.'
          },
          {
            title: 'Privacy',
            value: 'HIPAA-inspired guardrails',
            hint: 'Keep access tight and transparent.'
          },
          {
            title: 'Tenancy',
            value: 'Family boundaries',
            hint: 'Each household stays isolated from the next.'
          }
        ],
        steps: [
          'Open the admin area from the sidebar.',
          'Review roles, settings, and access boundaries.',
          'Use it as the control plane for the household.'
        ],
        links: [
          { label: 'Families', link: '/families/new' },
          { label: 'Members', link: '/members' },
          { label: 'Reports', link: '/reports' }
        ]
      }),
      {
        path: '**',
        redirectTo: 'dashboard'
      }
    ]
  }
];
