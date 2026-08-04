export type ExperienceStatus = 'commissioning' | 'available' | 'prototype';
export type ExperienceVisibility = 'personal-first' | 'workspace' | 'public-capable';
export type Experience = { id: string; name: string; shortDescription: string; route: string; status: ExperienceStatus; environment: string; chief: string; visibility: ExperienceVisibility; navigationOrder: number; };
export const experiences = [
  { id: 'startup', name: 'Startup and Commissioning', shortDescription: 'A guided beginning for the LifeCove prototype.', route: '/startup', status: 'commissioning', environment: 'arrival dock', chief: 'Paul', visibility: 'personal-first', navigationOrder: 1 },
  { id: 'headquarters', name: 'Headquarters', shortDescription: 'The calm home base after commissioning.', route: '/headquarters', status: 'available', environment: 'windowed lodge', chief: 'Paul', visibility: 'workspace', navigationOrder: 2 },
  { id: 'visible-privacy', name: 'Visible Privacy', shortDescription: 'Plain-language privacy states for content and sharing.', route: '/visible-privacy', status: 'available', environment: 'privacy porch', chief: 'Paul', visibility: 'personal-first', navigationOrder: 3 },
  { id: 'living-library', name: 'Living Library', shortDescription: 'A future home for organized memory, references, and meaning.', route: '/living-library', status: 'prototype', environment: 'library room', chief: 'Paul', visibility: 'personal-first', navigationOrder: 4 },
  { id: 'opportunity-center', name: 'Opportunity Center', shortDescription: 'Exceptional opportunities that may grow beyond ordinary creative products.', route: '/opportunity-center', status: 'prototype', environment: 'planning hall', chief: 'Paul', visibility: 'workspace', navigationOrder: 5 },
  { id: 'accidental-wonders', name: 'Accidental Wonders', shortDescription: 'The primary creative workshop for making and packaging creative products.', route: '/accidental-wonders', status: 'prototype', environment: 'workshop', chief: 'Paul', visibility: 'public-capable', navigationOrder: 6 },
  { id: 'this-is-what-happened', name: 'This Is What Happened', shortDescription: 'A connected storytelling destination for lived records and narrative.', route: '/this-is-what-happened', status: 'prototype', environment: 'story room', chief: 'Paul', visibility: 'personal-first', navigationOrder: 7 }
] as const satisfies readonly Experience[];
export const orderedExperiences = [...experiences].sort((a,b)=>a.navigationOrder-b.navigationOrder);
export function getExperienceByRoute(route: string) { return experiences.find((experience) => experience.route === route); }
