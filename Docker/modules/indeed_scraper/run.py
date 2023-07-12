# To run this script set the env variable $SCRAPFLY_KEY with your scrapfly API key:
# $ export $SCRAPFLY_KEY="your key from https://scrapfly.io/dashboard"
# poetry run python Docker/modules/indeed_scraper/run.py

import asyncio
import json
from pathlib import Path
import indeed

output = Path(__file__).parent / "results"
output.mkdir(exist_ok=True)


async def run(job_specification, location):
  # enable scrapfly cache for basic use
  indeed.BASE_CONFIG["cache"] = True

  print("running Indeed scrape and saving results to ./results directory")

  url = f"https://www.indeed.com/jobs?q={job_specification}&l={location}"
  result_search = await indeed.scrape_search(url, max_results=5)
  output.joinpath("search.json").write_text(json.dumps(result_search, indent=2, ensure_ascii=False))
  
  # Extract job keys from the search results
  job_keys = [job['jobkey'] for job in result_search]
      
  # Save the extracted job keys to a list
  job_keys_path = output.joinpath("job_keys.txt")
  job_keys_path.write_text('\n'.join(job_keys))
  print(f"Job keys saved to: {job_keys_path}")
  
  result_jobs = await indeed.scrape_jobs(job_keys)
  output.joinpath("jobs.json").write_text(json.dumps(result_jobs, indent=2, ensure_ascii=False))


if __name__ == "__main__":
  asyncio.run(run('python developer', 'washington'))