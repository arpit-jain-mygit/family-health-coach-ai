import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-family-settings',
  standalone: true,
  templateUrl: './family-settings.component.html',
  styleUrl: './family-settings.component.scss'
})
export class FamilySettingsComponent {
  readonly familyId = this.route.snapshot.paramMap.get('familyId');

  constructor(private readonly route: ActivatedRoute) {}
}
