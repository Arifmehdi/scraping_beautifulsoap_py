import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://driverbase.com/')
    await page.screenshot({'path':'screenshot.png'})
    # get title 
    title_html = await page.querySelector('h1')
    title = await (await title_html.getProperty('textContent')).jsonValue()
    print('title',title)
    # await browser.close()

asyncio.get_event_loop().run_until_complete(main())