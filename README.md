# Cover_Me

### Authors

Sarah Glass, Anthony Sinitsa, Dan Quinn, Logan Reese for seattle_c_py_401d22

## Description

This CLI app contains a web scraper from job search site indeed.com. The app collects data for job listings in the tech industry such as company name, skills, education level, salary detail, etc. and then allows users to search for jobs by keyword and location. The code runs a selected job's data along with the user's resume (uploaded via filepath) through AI to produce a sample cover letter tailored to the user, specifically for that job.

This program helps users find relevant and recent job listings in the tech industry, select listings they like, and prompt AI to process the listing's data to produce a sample cover letter for the given job posting.

## CLI wireframe - Our Initial Wireframe Walkthrough

__1. User launches the CLI app__

- The user opens their terminal or command prompt.
- They navigate to the directory where the CLI app is located.
- They execute a command to launch the app.
![Alt text](<midtermRun (2).jpg>)

__2. Main menu__

- The CLI app displays a main menu with several options.
- The user can select an option by entering a corresponding number or command.
```
Welcome to the Cover Me job scraper!

What would you like to do?

* Scrape job listings
* Search for jobs (keyword)
* Save jobs
* Generate cover letter
* Exit
```

__3. Scraping job listings__

If the user selects the "Scrape job listings" option:
- The app prompts the user to select a job search site (e.g., monster.com,   indeed.com).
- The app initiates the scraping process, collecting data for job listings in    the tech industry.
- As the app scrapes data, it provides a progress update in the terminal.
```
Please select a job search site:

* Monster.com
* Indeed.com
* Other
```
__4. Search for jobs__

If the user selects the "Search for jobs" option:
- The app prompts the user to enter a keyword or search term.
```
Please enter a keyword or search term:
```
- The app searches the scraped job data for listings that match the keyword.
- It displays the matching job listings, including company name, skills, education level, and salary details.
```
--------------------------------------
Job Title | Company Name | Skills | Education Level | Salary
------- | -------- | -------- | -------- | --------
Software Engineer | Google | Python, Java, C++ | Bachelor's degree | $100,000
Data Scientist | Facebook | SQL, R, Machine Learning | Master's degree | $120,000
UX Designer | Apple | Figma, Sketch, Adobe XD | Bachelor's degree | $90,000
```

__5. Save jobs__

If the user finds a job listing they are interested in:
- They can select the "Save job" option.
- The app prompts them to provide a name or identifier for the saved job.
```
Please enter a name or identifier for the saved job:
```
- The app saves the selected job listing with the provided name.

__6. Generate cover letter__

If the user selects the "Generate cover letter" option:
- The app prompts the user to select a saved job listing.
- Once a job is selected, the app runs its data through an AI model to generate a sample cover letter.
- The generated cover letter is displayed in the terminal.

```
=====================================
      COVER LETTER FOR Job X
=====================================

[Your Name]
[Your Address]
[City, State, ZIP Code]
[Email Address]
[Phone Number]
[Date]

[Recipient's Name]
[Recipient's Job Title]
[Company Name]
[Company Address]
[City, State, ZIP Code]

Dear [Recipient's Name],

I am writing to express my strong interest in the [Job Title] position at [Company Name], as advertised on [Job Listing Source]. 
With my solid background in the tech industry and a passion for [Specific Area of Tech], I believe I would be an excellent fit for your organization.

I have [X years] of experience working as a [Current or Most Recent Job Title] at [Current or Most Recent Company]. 
During my time there, I have successfully [Highlight Key Achievements or Responsibilities]. 
These experiences have equipped me with a deep understanding of [Relevant Technologies or Tools] and honed my ability to [Describe Relevant Skills or Expertise].

In addition to my technical skills, I am a highly motivated individual with a strong problem-solving mindset. I thrive in fast-paced environments and enjoy collaborating with cross-functional teams to deliver innovative solutions. 
I am confident in my ability to contribute to [Company Name]'s mission of [Company Mission or Values] and help drive its success in the tech industry.

I was particularly excited to learn about [Specific Achievement or Project] at [Company Name]. The opportunity to be part of such groundbreaking initiatives aligns perfectly with my career aspirations. 
I am eager to leverage my skills and knowledge to contribute to the continued growth and innovation of [Company Name].

Please find attached my resume for your review.
 I would welcome the opportunity to discuss how my skills and experience align with the [Job Title] position and learn more about [Company Name]'s vision for the future. Thank you for considering my application.

I look forward to the possibility of joining [Company Name] and contributing to its ongoing success. Thank you for your time and consideration.

Sincerely,

[Your Name]

=====================================
```

__7. Exit the app__

If the user selects the "Exit" option:

- The app terminates and the terminal session returns to the command prompt.

## User Stories

1. Tech job seeker: I want to search for job listings in tech industry by entering keywords, so that I can find relevant opportunities.
2. Job seeker who wants location and date: I want to filter job listings by location and date posted, so that I can view recent and localized job opportunities.
3. Job seeker who wants a sample cover letter: I want to generate a sample cover letter for a selected job listing using AI processing to help me kickstart my application process.
4. Job seeker who wants job details: I want to view detailed information about a job listing, including company name, required skills, education level, and salary details, so that I can assess if it aligns with my qualifications and expectations.
5. Job seeker with accessibility considerations: as a job seeker, I want to be able to access the job info and cover letter samples for free, and with an acceptable accessibility score (whatever the CLI version of Lighthouse is).

## Domain Model

![Domain Model](domainModel2.jpg)

### [Software Requirements](https://github.com/Cover-Me401/Team-Agreement/blob/main/requirements.md)

## Links and Resources

- [Job Scraping Github that spawned the idea/dream](https://github.com/Ashishkapil/Web-scraping-job-portal-sites)

- [How to Scrape Indeed in 2023](https://scrapeops.io/web-scraping-playbook/how-to-scrape-indeed/)

- [Automating Job Search with Python using BeautifulSoup and Selenium](https://www.chrislovejoy.me/job-scraper)

- [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

- [Scrape Ops Proxy Aggregator for anti-bot protection](https://scrapeops.io/proxy-aggregator/)

- [Scrape LinkedIn Using Selenium And Beautiful Soup in Python](https://www.geeksforgeeks.org/scrape-linkedin-using-selenium-and-beautiful-soup-in-python/)

- [Accessibility of Command Line Interfaces](https://dl.acm.org/doi/fullHtml/10.1145/3411764.3445544)

- [Command Line Tools to Test Accessibility](https://www.assist.vt.edu/web-accessibility/testing-tools/command-line-developer-tools.html)

- [Python Library automated-accessibility-testing](https://pypi.org/project/automated-accessibility-testing/)


## Setup

- ENV requirements:

```python
python3 -m venv .venv
source .venv/bin/activate
```


## How to initialize/run application

- `python Docker/modules/indeed_scraper/main.py``

## Libraries & Tools

aiofiles==23.1.0
aiohttp==3.8.4
aiosignal==1.3.1
anyio==3.7.1
async-timeout==4.0.2
attrs==23.1.0
bard==0.1
bardapi==0.1.24
beautifulsoup4==4.12.2
bs4==0.0.1
build==0.10.0
CacheControl==0.12.14
cachetools==4.2.4
Cerberus==1.3.4
certifi==2023.5.7
cffi==1.15.1
charset-normalizer==3.2.0
ci-info==0.3.0
cleo==2.0.1
click==8.1.4
colorama==0.4.6
configobj==5.0.8
configparser==6.0.0
coverage==7.2.7
crashtest==0.4.1
deep-translator==1.11.4
distlib==0.3.6
dulwich==0.21.5
etelemetry==0.3.0
filelock==3.12.2
fitz==0.0.1.dev2
frontend==0.0.3
frozenlist==1.4.0
future==0.18.3
google-api-core==1.34.0
google-auth==1.35.0
google-cloud-core==1.7.3
google-cloud-translate==2.0.1
googleapis-common-protos==1.59.1
grpcio==1.56.0
grpcio-status==1.48.2
h11==0.14.0
h2==4.1.0
hpack==4.0.0
html5lib==1.1
httpcore==0.17.3
httplib2==0.22.0
httpx==0.24.1
hyperframe==6.0.1
idna==3.4
importlib-metadata==6.8.0
iniconfig==2.0.0
installer==0.7.0
isodate==0.6.1
itsdangerous==2.1.2
jaraco.classes==3.3.0
jsonschema==4.18.3
jsonschema-specifications==2023.6.1
keyring==23.13.1
lockfile==0.12.2
looseversion==1.3.0
lxml==4.9.3
markdown-it-py==3.0.0
mdurl==0.1.2
more-itertools==9.1.0
msgpack==1.0.5
multidict==6.0.4
networkx==3.1
nibabel==5.1.0
nipype==1.8.6
numpy==1.25.1
openai==0.27.8
packaging==23.1
pandas==2.0.3
pathlib==1.0.1
pexpect==4.8.0
pkginfo==1.9.6
platformdirs==3.8.1
pluggy==1.2.0
poetry==1.5.1
poetry-core==1.6.1
poetry-plugin-export==1.4.0
protobuf==3.20.3
prov==2.0.0
ptyprocess==0.7.0
pyasn1==0.5.0
pyasn1-modules==0.3.0
pycparser==2.21
pydot==1.4.2
Pygments==2.15.1
PyMuPDF==1.22.5
pyparsing==3.1.0
pyproject_hooks==1.0.0
pytest==7.4.0
pytest-cov==4.1.0
python-dateutil==2.8.2
python-dotenv==1.0.0
pytils==0.4.1
pytz==2023.3
pyxnat==1.5
rapidfuzz==2.15.1
rdflib==6.3.2
referencing==0.29.1
requests==2.31.0
requests-toolbelt==1.0.0
rich==13.4.2
rpds-py==0.8.10
rsa==4.9
scipy==1.11.1
shellingham==1.5.0.post1
simplejson==3.19.1
six==1.16.0
sniffio==1.3.0
soupsieve==2.4.1
starlette==0.28.0
tomlkit==0.11.8
tools==0.1.9
tqdm==4.65.0
traits==6.3.2
trove-classifiers==2023.7.6
tzdata==2023.3
urllib3==1.26.16
uvicorn==0.22.0
virtualenv==20.23.1
webencodings==0.5.1
xattr==0.10.1
yarl==1.9.2
zipp==3.16.1

**API Keys:**

- BARD -  Backup AI
- OPENAI - AI
- SCRAPFLY - Scraper tool
- SCRAPEOPS - 403 forbidden error avoider

## Tests

- Coverage: 80% coverage with `pytest-cov'
- Testing using `pytest` and `unittest.mock`
