import { Component, inject } from '@angular/core';
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
export class CreateFamilyComponent {
  private readonly api = inject(ApiService);
  private readonly formBuilder = inject(FormBuilder);
  private readonly router = inject(Router);

  form = this.formBuilder.nonNullable.group({
    name: ['', [Validators.required]]
  });

  submit(): void {
    if (this.form.invalid) {
      this.form.markAllAsTouched();
      return;
    }
    this.api.createFamily({ name: this.form.controls.name.value }).subscribe((family) => {
      this.router.navigateByUrl(`/families/${family.id}/settings`);
    });
  }
}
