# crawl-jobs
crwl "https://www.infojobs.com.br/empregos.aspx?palabra=engenheiro+de+dados" -C crawler.yml -B browser.yml -e extract_css.yml -s css_schema.json --output json > jobs.json