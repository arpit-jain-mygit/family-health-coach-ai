import { Routes } from '@angular/router';
import { authGuard } from './core/guards/auth.guard';

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
      import('./features/dashboard/dashboard.component').then((m) => m.DashboardComponent)
  },
  {
    path: 'families/new',
    canActivate: [authGuard],
    loadComponent: () =>
      import('./features/family/create-family/create-family.component').then(
        (m) => m.CreateFamilyComponent
      )
  },
  {
    path: 'families/:familyId/settings',
    canActivate: [authGuard],
    loadComponent: () =>
      import('./features/family/family-settings/family-settings.component').then(
        (m) => m.FamilySettingsComponent
      )
  }
];
