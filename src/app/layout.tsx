import type { Metadata } from 'next';import './globals.css';import { AppShell } from '@/components/app-shell/AppShell';
export const metadata: Metadata={title:'LifeCove V0.1',description:'LifeCove immersive shell baseline'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body><AppShell>{children}</AppShell></body></html>}
