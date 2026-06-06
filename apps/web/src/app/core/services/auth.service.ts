import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';

@Injectable({ providedIn: 'root' })
export class AuthService {
  isAuthenticated(): boolean {
    return Boolean(localStorage.getItem('family_health_token'));
  }

  loginWithGoogle(): void {
    window.location.href = `${environment.apiBaseUrl}/api/v1/auth/google`;
  }

  logout(): void {
    localStorage.removeItem('family_health_token');
  }
}
