import { render,screen } from '@testing-library/react';import { it,expect } from 'vitest';import { PrivacyStates } from '@/components/privacy/PrivacyStates';
it('displays Personal, Invited, and Published',()=>{render(<PrivacyStates/>);['Personal','Invited','Published'].forEach(s=>expect(screen.getByRole('heading',{name:s})).toBeInTheDocument())});
