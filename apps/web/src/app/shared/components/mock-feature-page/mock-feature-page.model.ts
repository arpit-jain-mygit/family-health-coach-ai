export interface MockFeatureAction {
  label: string;
  link: string;
}

export interface MockFeatureCard {
  title: string;
  value: string;
  hint: string;
}

export interface MockFeaturePageData {
  eyebrow: string;
  title: string;
  description: string;
  summary: string;
  primaryAction?: MockFeatureAction;
  secondaryAction?: MockFeatureAction;
  cards: MockFeatureCard[];
  steps: string[];
  links: MockFeatureAction[];
}
