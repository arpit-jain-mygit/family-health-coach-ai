import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';

export interface FamilyPayload {
  name: string;
  goals?: Record<string, unknown> | null;
  preferences?: Record<string, unknown> | null;
}

export interface FamilyResponse extends FamilyPayload {
  id: string;
}

@Injectable({ providedIn: 'root' })
export class ApiService {
  private readonly baseUrl = environment.apiBaseUrl;

  constructor(private readonly http: HttpClient) {}

  health() {
    return this.http.get<{ status: string }>(`${this.baseUrl}/api/v1/health`);
  }

  listFamilies() {
    return this.http.get<FamilyResponse[]>(`${this.baseUrl}/api/v1/families`);
  }

  createFamily(payload: FamilyPayload) {
    return this.http.post<FamilyResponse>(`${this.baseUrl}/api/v1/families`, payload);
  }

  getFamily(familyId: string) {
    return this.http.get<FamilyResponse>(`${this.baseUrl}/api/v1/families/${familyId}`);
  }

  updateFamily(familyId: string, payload: Partial<FamilyPayload>) {
    return this.http.patch<FamilyResponse>(`${this.baseUrl}/api/v1/families/${familyId}`, payload);
  }

  deleteFamily(familyId: string) {
    return this.http.delete<void>(`${this.baseUrl}/api/v1/families/${familyId}`);
  }
}
