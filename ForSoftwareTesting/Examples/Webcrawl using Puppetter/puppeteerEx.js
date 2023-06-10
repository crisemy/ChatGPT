const puppeteer = require('puppeteer');

async function crawlWebsite() {
  // Launch the browser in the new headless mode
  const browser = await puppeteer.launch({ headless: "new" });

  // Open a new page
  const page = await browser.newPage();

  // Navigate to the website
  await page.goto('https://openai.com/');

  // Wait for the required content to load with an increased timeout
  await page.waitForSelector('.post .entry-title', { timeout: 60000 });

  // Extract the course names
  const courseNames = await page.evaluate(() => {
    const courseElements = document.querySelectorAll('.post .entry-title');
    const names = Array.from(courseElements).map((element) => element.innerText);
    return names;
  });

  // Display the course names
  console.log('Course Names:');
  courseNames.forEach((name) => console.log(name));

  // Close the browser
  await browser.close();
}

// Run the crawling function
crawlWebsite();