import { Component, inject } from '@angular/core';
import { Router, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { FamilyResponse } from '../../../core/api/api.service';
import { AuthService } from '../../../core/services/auth.service';
import { FamilySwitcherComponent } from '../family-switcher/family-switcher.component';

@Component({
  selector: 'app-shell',
  standalone: true,
  imports: [RouterLink, RouterLinkActive, RouterOutlet, FamilySwitcherComponent],
  templateUrl: './app-shell.component.html',
  styleUrl: './app-shell.component.scss'
})
export class AppShellComponent {
  private readonly auth = inject(AuthService);
  private readonly router = inject(Router);

  readonly families: FamilyResponse[] = [
    {
      id: 'family-a',
      name: 'Family A',
      goals: null,
      preferences: null
    },
    {
      id: 'family-b',
      name: 'Family B',
      goals: null,
      preferences: null
    }
  ];

  readonly navItems = [
    { label: 'Dashboard', link: '/dashboard', icon: 'bi-grid-1x2-fill' },
    { label: 'Families', link: '/families/new', icon: 'bi-house-heart' },
    { label: 'Members', link: '/members', icon: 'bi-people' },
    { label: 'Chat', link: '/chat', icon: 'bi-chat-dots' },
    { label: 'Food logging', link: '/food-logs', icon: 'bi-journal-text' },
    { label: 'Meal plans', link: '/meal-plans', icon: 'bi-calendar2-week' },
    { label: 'Progress', link: '/progress', icon: 'bi-graph-up-arrow' },
    { label: 'Reports', link: '/reports', icon: 'bi-file-earmark-text' },
    { label: 'Leaderboard', link: '/leaderboard', icon: 'bi-trophy' },
    { label: 'Reminders', link: '/reminders', icon: 'bi-bell' },
    { label: 'Admin', link: '/admin', icon: 'bi-shield-lock' }
  ];

  readonly selectedFamilyId = 'family-a';

  logout(): void {
    this.auth.logout();
    this.router.navigateByUrl('/login');
  }
}
