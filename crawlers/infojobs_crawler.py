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
        scan_full_page=True,
        extraction_strategy=JsonCssExtractionStrategy(
            schema={
  "name": "JobListing",
  "baseSelector": "div.card.card-shadow.card-shadow-hover.text-break.mb-16.grid-row.js_rowCard",
  "fields": [
    {
      "name": "title",
      "selector": "h2.h3.font-weight-bold.text-body.mb-8",
      "type": "text"
    },
    {
      "name": "company",
      "selector": "a.text-body.text-decoration-none[href*='infojobs.com.br']",
      "type": "text"
    },
    {
      "name": "rating",
      "selector": "div.text-nowrap span.font-weight-bold.text-body",
      "type": "text"
    },
    {
      "name": "location",
      "selector": "div.small.text-medium.mr-24",
      "type": "text"
    },
    {
      "name": "job_type",
      "selector": "div.text-medium.caption",
      "type": "text"
    },
    {
      "name": "date_posted",
      "selector": "div.ml-auto.d-flex.flex-column.align-items-end.text-nowrap div.text-medium.small",
      "type": "text"
    },
    {
      "name": "description",
      "selector": "div.js_vacancyLoad div.small.text-medium",
      "type": "text"
    },
    {
      "name": "job_link",
      "selector": "a.text-decoration-none",
      "attribute": "href",
      "type": "attribute",
      "prefix": "https://www.infojobs.com.br"
    }
  ]
}
)
)


    # Example search URL (you should replace with your actual Amazon URL)
    url = "https://www.infojobs.com.br/vagas-de-emprego-engenheiro+de+dados.aspx?campo=griddate&orden=desc&poblacion=5211323"

    # Use context manager for proper resource handling
    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Extract the data
        result = await crawler.arun(url=url, config=crawler_config)

        # Process and print the results
        if result and result.extracted_content:
            # Parse the JSON string into a list of products
            products = json.loads(result.extracted_content)

            with open("resultado.json", "w", encoding="utf-8") as f:
                json.dump(products, f, ensure_ascii=False, indent=4)

            # Process each product in the list
            for product in products:
                print("\nProduct Details:")
                print(f"title: {product.get('title')}")
                # print(f"company: {product}")
                print("-" * 80)


if __name__ == "__main__":
    import asyncio

    asyncio.run(extract_jobs_list())