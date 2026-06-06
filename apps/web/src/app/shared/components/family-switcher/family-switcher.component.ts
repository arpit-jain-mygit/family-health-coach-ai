import { Component, Input } from '@angular/core';
import { FamilyResponse } from '../../../core/api/api.service';

@Component({
  selector: 'app-family-switcher',
  standalone: true,
  templateUrl: './family-switcher.component.html',
  styleUrl: './family-switcher.component.scss'
})
export class FamilySwitcherComponent {
  @Input() families: FamilyResponse[] = [];
  @Input() selectedFamilyId: string | null = null;
}
