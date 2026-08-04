import { render,screen } from '@testing-library/react';import { vi,it,expect } from 'vitest';import { MainNavigation } from '@/components/navigation/MainNavigation';
vi.mock('next/navigation',()=>({usePathname:()=>'/headquarters'}));
vi.mock('next/link',()=>({default:({href,children,...p}:any)=><a href={href} {...p}>{children}</a>}));
it('renders required destinations',()=>{render(<MainNavigation/>);['Headquarters','Privacy','Living Library','Opportunity Center'].forEach(n=>expect(screen.getAllByText(new RegExp(n))[0]).toBeInTheDocument())});
