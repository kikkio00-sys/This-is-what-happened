import { z } from 'zod';
export const envSchema = z.object({ NEXT_PUBLIC_LIFECOVE_ENV: z.string().default('local') });
export const env = envSchema.parse({ NEXT_PUBLIC_LIFECOVE_ENV: process.env.NEXT_PUBLIC_LIFECOVE_ENV });
