import { Component, OnInit, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from '../../../core/api/api.service';

@Component({
  selector: 'app-create-family',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './create-family.component.html',
  styleUrl: './create-family.component.scss'
})
export class CreateFamilyComponent implements OnInit {
  private readonly api = inject(ApiService);
  private readonly formBuilder = inject(FormBuilder);
  private readonly router = inject(Router);
  existingFamily: { id: string; name: string } | null = null;
  errorMessage: string | null = null;

  form = this.formBuilder.nonNullable.group({
    name: ['', [Validators.required]]
  });

  ngOnInit(): void {
    this.api.listFamilies().subscribe({
      next: (families) => {
        const [family] = families;
        if (family) {
          this.existingFamily = { id: family.id, name: family.name };
          this.router.navigateByUrl(`/families/${family.id}/settings`);
        }
      },
      error: () => {
        this.errorMessage = 'Could not load your family. Please refresh and try again.';
      }
    });
  }

  submit(): void {
    if (this.form.invalid) {
      this.form.markAllAsTouched();
      return;
    }
    this.errorMessage = null;
    this.api.createFamily({ name: this.form.controls.name.value }).subscribe({
      next: (family) => {
        this.router.navigateByUrl(`/families/${family.id}/settings`);
      },
      error: () => {
        this.errorMessage =
          'Family creation failed. If you already have a family, open it from the dashboard.';
      }
    });
  }
}
