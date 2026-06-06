import { Component, inject } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';

@Component({
  selector: 'app-family-settings',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './family-settings.component.html',
  styleUrl: './family-settings.component.scss'
})
export class FamilySettingsComponent {
  private readonly route = inject(ActivatedRoute);
  readonly familyId = this.route.snapshot.paramMap.get('familyId');
}
