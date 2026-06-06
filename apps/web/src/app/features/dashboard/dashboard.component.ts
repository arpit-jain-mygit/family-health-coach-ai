import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss'
})
export class DashboardComponent {
  readonly featureCards = [
    {
      title: 'Families',
      link: '/families/new',
      icon: 'bi-house-heart',
      summary: 'Create the household and define the first goals.'
    },
    {
      title: 'Members',
      link: '/members',
      icon: 'bi-people',
      summary: 'Add parents, children, and grandparents.'
    },
    {
      title: 'Chat',
      link: '/chat',
      icon: 'bi-chat-dots',
      summary: 'Log meals and ask for plans in one conversation.'
    },
    {
      title: 'Food logging',
      link: '/food-logs',
      icon: 'bi-journal-text',
      summary: 'Use text, voice, or photo logging.'
    },
    {
      title: 'Meal plans',
      link: '/meal-plans',
      icon: 'bi-calendar2-week',
      summary: 'Generate vegetarian, Jain, or vegan plans.'
    },
    {
      title: 'Progress',
      link: '/progress',
      icon: 'bi-graph-up-arrow',
      summary: 'Review weight, waist, and marker trends.'
    },
    {
      title: 'Reports',
      link: '/reports',
      icon: 'bi-file-earmark-text',
      summary: 'Open daily, weekly, monthly, and family summaries.'
    },
    {
      title: 'Leaderboard',
      link: '/leaderboard',
      icon: 'bi-trophy',
      summary: 'Compare adherence, improvement, and consistency.'
    },
    {
      title: 'Reminders',
      link: '/reminders',
      icon: 'bi-bell',
      summary: 'Schedule meal, water, walking, and medication nudges.'
    },
    {
      title: 'Admin',
      link: '/admin',
      icon: 'bi-shield-lock',
      summary: 'Review roles, logs, and privacy controls.'
    }
  ];

  readonly setupSteps = [
    'Create the family.',
    'Add members and goals.',
    'Start logging meals in chat.',
    'Review progress, reports, and reminders.'
  ];
}
