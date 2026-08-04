import { test, expect } from '@playwright/test';
const routes=['/startup','/headquarters','/visible-privacy','/living-library','/opportunity-center','/accidental-wonders','/this-is-what-happened'];
test('root route reaches Startup and Commissioning',async({page})=>{await page.goto('/');await expect(page).toHaveURL(/\/startup$/);await expect(page.getByRole('heading',{name:'Welcome to LifeCove'})).toBeVisible()});
test('commissioning flow can reach Headquarters',async({page})=>{await page.goto('/startup');for(let i=0;i<7;i++) await page.getByRole('button',{name:/continue/i}).click();await page.getByRole('button',{name:/enter headquarters/i}).click();await expect(page).toHaveURL(/\/headquarters$/);await expect(page.getByRole('heading',{name:'Headquarters'})).toBeVisible()});
test('core routes render successfully',async({page})=>{for(const route of routes){await page.goto(route);await expect(page.locator('h1')).toBeVisible()}});
