import { Component, inject } from '@angular/core';
import { RouterLink } from '@angular/router';
import { MockFeaturePageData } from './mock-feature-page.model';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-mock-feature-page',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './mock-feature-page.component.html',
  styleUrl: './mock-feature-page.component.scss'
})
export class MockFeaturePageComponent {
  private readonly route = inject(ActivatedRoute);
  readonly page = this.route.snapshot.data['page'] as MockFeaturePageData;
}
