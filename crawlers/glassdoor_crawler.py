"""
This example demonstrates how to use JSON CSS extraction to scrape product information 
from Amazon search results. It shows how to extract structured data like product titles,
prices, ratings, and other details using CSS selectors.
"""

from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
import json


async def extract_jobs_list():
    # Initialize browser config
    browser_config = BrowserConfig(browser_type="chromium", headless=False)

    # Initialize crawler config with JSON CSS extraction strategy
    crawler_config = CrawlerRunConfig(
        scan_full_page=False,
        delay_before_return_html=2,
        extraction_strategy=JsonCssExtractionStrategy(
            schema={
  "name": "JobListing",
  "baseSelector": "[class^='JobsList_jobListItem']",
  "fields": [
    {
      "name": "title",
      "selector": "[class^='JobCard_jobTitle']",
      "type": "text"
    },
    {
      "name": "company",
      "selector": "span[class^='EmployerProfile']",
      "type": "text"
    },
    {
      "name": "rating",
      "selector": "span.Rating_spanAverage",
      "type": "text"
    },
    {
      "name": "location",
      "selector": "div[class^='JobCard_location']",
      "type": "text"
    },
    {
      "name": "job_type",
      "selector": "span.JobCard_jobType",
      "type": "text"
    },
    {
      "name": "date_posted",
      "selector": "div[class^='JobCard_listingAge']",
      "type": "text"
    },
    {
      "name": "salary",
      "selector": "div[class^='JobCard_salaryEstimate']",
      "type": "text"
    },
    {
      "name": "job_link",
      "selector": "a[class^='JobCard_trackingLink']",
      "attribute": "href",
      "type": "attribute",
      "prefix": "https://www.glassdoor.com.br/"
    }
  ]
}
)
)


    # Example search URL (you should replace with your actual Amazon URL)
    url = "https://www.glassdoor.com.br/Vaga/brasil-engenheiro-de-dados-vagas-SRCH_IL.0,6_IN36_KO7,26.htm?fromAge=7&sortBy=date_desc"

    # Use context manager for proper resource handling
    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Extract the data
        result = await crawler.arun(url=url, config=crawler_config)

        # Process and print the results
        if result and result.extracted_content:
            # Parse the JSON string into a list of products
            products = json.loads(result.extracted_content)

            with open("resultado_glassdoor.json", "w", encoding="utf-8") as f:
                json.dump(products, f, ensure_ascii=False, indent=4)

            # Process each product in the list
            for product in products:
                print("\nProduct Details:")
                print(f"title: {product.get('title')}")
                print(f"company: {product.get('company')}")
                print(f"rating: {product.get('rating')}")
                print(f"location: {product.get('location')}")
                print(f"job_type: {product.get('job_type')}")
                print(f"date_posted: {product.get('date_posted')}")
                print(f"description: {product.get('description')}")
                print(f"job_link: {product.get('job_link')}")
                # print(f"company: {product}")
                print("-" * 80)


if __name__ == "__main__":
    import asyncio

    asyncio.run(extract_jobs_list())