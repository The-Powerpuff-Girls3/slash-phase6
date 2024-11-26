<p align="center"><img width="500" src="assets/slash_new.png"></p>

[![DOI](https://zenodo.org/badge/891250312.svg)](https://doi.org/10.5281/zenodo.14213552)

[![GitHub Release](https://img.shields.io/badge/release-v1.0.1-blue)](https://github.com/The-Powerpuff-Girls3/slash-phase7)
[![Syntax Check](https://github.com/The-Powerpuff-Girls3/slash-phase7/actions/workflows/syntax.yml/badge.svg)](https://github.com/The-Powerpuff-Girls3/slash-phase7/actions/workflows/syntax.yml)
[![Python Application](https://github.com/The-Powerpuff-Girls3/slash-phase7/actions/workflows/python-app.yml/badge.svg)](https://github.com/The-Powerpuff-Girls3/slash-phase7/actions/workflows/python-app.yml)
[![codecov](https://codecov.io/gh/The-Powerpuff-Girls3/slash-phase7/branch/main/graph/badge.svg)](https://codecov.io/gh/The-Powerpuff-Girls3/slash-phase7/tree/main)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/The-Powerpuff-Girls3/slash-phase7/graphs/commit-activity)
[![Contributors Activity](https://img.shields.io/github/commit-activity/m/The-Powerpuff-Girls3/slash-phase7)](https://github.com/The-Powerpuff-Girls3/slash-phase7/pulse)
[![GitHub issues](https://img.shields.io/github/issues/The-Powerpuff-Girls3/slash-phase7.svg)](https://github.com/The-Powerpuff-Girls3/slash-phase7/issues?q=is%3Aopen+is%3Aissue)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/The-Powerpuff-Girls3/slash-phase7.svg)](https://github.com/The-Powerpuff-Girls3/slash-phase7/issues?q=is%3Aissue+is%3Aclosed)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
[![StyleCheck: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![Security Check: Bandit](https://img.shields.io/badge/security-bandit-orange)](https://bandit.readthedocs.io/en/latest/)
[![Code Formatter: black](https://img.shields.io/badge/formatter-black-black)](https://black.readthedocs.io/en/stable/)
![GitHub contributors](https://img.shields.io/github/contributors/The-Powerpuff-Girls3/slash-phase7)
![GitHub repo size](https://img.shields.io/github/repo-size/The-Powerpuff-Girls3/slash-phase7)

<p align="center">
    <a href="https://github.com/The-Powerpuff-Girls3/slash-phase7/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=">Report a Bug</a>
    ·
    <a href="https://github.com/The-Powerpuff-Girls3/slash-phase7/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=">Request a Feature</a>
</p>

<!-- ```diff
! All the latest changes in slash-phase7 are in "main" branch.
``` -->


# Slash: Your Ultimate Shopping Assistant

Do you love shopping? Are you in search of great deals while shopping online?! Slash is here to help you find the best bargains effortlessly!

Tired of visiting multiple websites to compare prices? **Slash** makes your online shopping experience smarter, faster, and more enjoyable!

**Slash** is a powerful web API framework that scrapes top e-commerce sites—[Walmart](https://www.walmart.com/), [Target](https://www.target.com/), [BestBuy](https://www.bestbuy.com/), [Costco](https://www.costco.com), and [EBay](https://www.ebay.com/)—to find and compare the best deals for you. Whether you're a student on a budget or a data analyst building real-time datasets, **Slash** is your go-to tool.

## Key Features:
- **Google Login Integration**: Securely log in using your Google account for a personalized experience.
- **Filter by Product Ratings**: Find items that match your expectations with our star-rating filter.
- **Price Distribution Visualization**: View a detailed price distribution chart to make informed purchasing decisions.
- **Fast**: Compare deals across platforms in seconds.
- **Easy**: User-friendly APIs to filter, sort, and customize search results.
- **Powerful**: Delivers tailored results in JSON format, perfect for seamless integration.

Save time, money, and effort with **Slash**—your all-in-one shopping assistant!

---

<p align="center">
  <a href="#movie_camera-checkout-our-video">Checkout our video</a>
  ::
  <a href="#rocket-installation">Installation</a>
  ::
  <a href="#computer-technology-used">Technology Used</a>
  ::
  <a href="#bulb-use-case">Use Case</a>
  ::
  <a href="#page_facing_up-why">Why</a>
  ::
  <a href="#golf-future-roadmap">Future Roadmap</a>
  ::
  <a href="#sparkles-contributors">Contributors</a>
  ::
  <a href="#Acknowledgement">Acknowledgement</a>
  ::
  <a href="#email-support">Support</a>
  
</p>

---

:movie_camera: Checkout our video list on Youtube channel!
---

[Youtube](https://www.youtube.com/playlist?list=PLiz2sL3f73DiGDU6hztb0sxBvc7_Ic-MF)


---

:rocket: Installation
---
1. Clone the Github repository to a desired location on your computer. You will need [git](https://git-scm.com/) to be preinstalled on your machine. Once the repository is cloned, you will then ```cd``` into the local repository.
```
git clone https://github.com/The-Powerpuff-Girls3/slash-phase7.git
cd slash-phase7
```
1. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those.
```
pip3 install -r requirements.txt
```
1. To run this project, you must install PostgreSQL on your system. If you haven't already installed it, you can download the latest version of PostgreSQL from the official website: [PostgreSQL Downloads](https://www.postgresql.org/download/).

### Configuring Database Connection

Once you've installed PostgreSQL, follow these steps to set up the database connection in your project:

i. Open the database.py file in your project directory.

ii. Locate the top section of the code where you define the database connection settings. It might look something like this:

   ```
   username = 'postgres'
   password = 'pass'
   ```
Replace username and password value from 'postgres', 'pass' with your PostgreSQL username password, respectively.

4. Once all the requirements are installed, you will have to enter the `src` folder. Once in the `src` folder, use the python command to run the `main.py` file.
```
cd src

For Mac
python3 main.py

For Windows
python main.py
```
5. While the above is running, go to new terminal and run streamlit application. Firstly go back to the root directory and run the following command:
```
cd ..

For Mac
python3 -m streamlit run slash_user_interface.py

For Windows
streamlit run slash_user_interface.py
```

:computer: Technology Used
---
- [Streamlit](https://streamlit.io/)
- [Fast API](https://fastapi.tiangolo.com)
- [Postgre SQL](https://www.postgresql.org)
- [Python](https://www.python.org)

:bulb: Use Case
---
* ***Students***: Students coming to university are generally on a budget and time constraint and generally spend hours wasting time to search for products on Websites. Slash is the perfect tool for these students that slashes all the unnecessary details on a website and helps them get prices for a product across multiple websites.Make the most of this tool in the upcoming Black Friday Sale.
* ***Data Analysts***: Finding data for any project is one of the most tedious job for a data analyst, and the datasets found might not be the most recent one. Using slash, they can create their own dataset in real time and format it as per their needs so that they can focus on what is actually important.

:page_facing_up: Why
---
- In a market where we are spoilt for choices, we often look for the best deals.  
- The ubiquity of internet access has leveled the retail playing field, making it easy for individuals and businesses to sell products without geographic limitation. In 2020, U.S. e-commerce sales, receiving a boost due to the COVID-19 pandemic, grew 44% and represented more than 21% of total retail sales, according to e-commerce information source Internet Retailer.
- The growth of e-commerce has not only changed the way customers shop, but also their expectations of how brands approach customer service, personalize communications, and provide customers choices.
- E-commerce market has prompted cut throat competition amongst dealers, which is discernable through the price patterns for products of major market players. Price cuts are somewhat of a norm now and getting the best deal for your money can sometimes be a hassle (even while online shopping).
- This is what Slash aims to reduce by giving you an easy to use, all in one place solution for finding the best deals for your products that major market dealers have to offer!
- Slash in its current form is for students who wish to get the best deals out of every e-commerce site and can be used by anyone who is willing to develop an application that consumes these web APIs.
- Future scope includes anything from a web application with a frontend or any Android or IOS application that utilises these Web APIs at their backend. Anyone can build their own custom application on top of these web APIs.

:golf: Phase 7 developments
---
1. **Google Login Feature**
---
We have added a Google login feature in the slash_user_interface.py script. This allows users to log in using their Google accounts for a more seamless and secure authentication experience.
<img src = https://github.com/The-Powerpuff-Girls3/slash-phase6/blob/main/media/login.png>

2. **Advanced Search Capabilities**
We have enhanced the search functionality by introducing advanced filters, including product ratings. The new option empowers users to refine their search results with precision, ensuring they find high-quality items that meet their preferences and needs.

<img src = https://github.com/The-Powerpuff-Girls3/slash-phase7/blob/main/media/rating.png>

4. **Price Distribution Plot✨**

   - **Price Distribution Visualization**: Displays a **histogram** with an overlaid **KDE** curve to understand how prices are distributed.
   - **Statistical Indicators**: Highlights key statistics such as:
     - **Mean Price**: The average price
     - **Median Price**: The middle value of the price data.
     - **Min/Max Prices**: The lowest and highest prices.
     - **Standard Deviation**: A measure of price variability.
   - **Interactive Plot**: The plot is rendered interactively, allowing users to easily analyze price trends.
   - **Customizable Aesthetics**: The visualization includes options to customize **labels**, **grid lines**, and **colors** for improved clarity and presentation.
   - **Market Analysis**: Compare prices across different sources or vendors.
   - **Pricing Strategy**: Help sellers set competitive prices.
   - **Consumer Insights**: Enable consumers to visualize and assess price ranges across various platforms.

<img src = https://github.com/The-Powerpuff-Girls3/slash-phase6/blob/main/media/exp1.png>
<img src = https://github.com/The-Powerpuff-Girls3/slash-phase6/blob/main/media/exp2.png>
<img src = https://github.com/The-Powerpuff-Girls3/slash-phase6/blob/main/media/exp3.png>
<img src = https://github.com/The-Powerpuff-Girls3/slash-phase6/blob/main/media/price_chart.png>

:golf: Future Roadmap
---
- Predictive Price Model: We plan to implement a machine learning-based predictive model that advises users on the optimal time to make purchases, based on historical price trends and forecasting.
- Pagination for Search Results: A pagination                  system to improve the display of search results,          particularly for large datasets is in progress.
- Voice Search Integration: Introduce voice-activated search functionality, allowing users to search for products using natural language voice commands for a more convenient shopping experience.
- Wishlist Price Alerts: Implement a notification system to alert users when the prices of products in their wishlists drop below a certain threshold, helping them make timely purchases.
- AI-Based Personal Shopping Assistant: Develop an AI-driven assistant that provides personalized product recommendations based on user preferences, browsing history, and current trends to enhance the shopping experience.

:sparkles: Contributors && Contribution
---
Building on the contributions of previous groups, this project has been expanded with the addition of three more talented teammates!

1. Yinan Wu (ywu92@ncsu.edu)
2. Xuntao Lyu (xlyu5@ncsu.edu)
3. Hua Yang (hyang45@ncsu.edu)




## 🙏 Acknowledgements <a name="Acknowledgement"></a>
<!-- We would like to thank Professor Dr Timothy Menzies for helping us understand the process of Maintaining a good Software Engineering project. We would also like to thank the teaching assistants for their support throughout the project. -->
We would like to thank the teaching assistants for their support throughout the project.
Some code in our project is modified from this [repo](https://github.com/DFY-NCSU/slash-phase6).

:email: Support
---
For any queries and help, please reach out to us at: slash7support@googlegroups.com

## Funding

Not funded

## Citation

The Powerpuff Girls3. slash-phase7. Version 1.0.1, 2024, GitHub, https://github.com/The-Powerpuff-Girls3/slash-phase7
