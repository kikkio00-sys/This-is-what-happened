import { orderedExperiences } from './experiences';
export const primaryNavigation = orderedExperiences.filter((experience) => experience.id !== 'startup');
