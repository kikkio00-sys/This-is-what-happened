import { defineConfig, devices } from '@playwright/test';
export default defineConfig({testDir:'./src/tests',testMatch:['**/{e2e,accessibility}/**/*.spec.ts'],webServer:{command:'npm run dev',url:'http://127.0.0.1:3000',reuseExistingServer:!process.env.CI,timeout:120000},use:{baseURL:'http://127.0.0.1:3000',trace:'on-first-retry'},projects:[{name:'chromium',use:{...devices['Desktop Chrome']}}]});
