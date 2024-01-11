import os
import requests
from bs4 import BeautifulSoup

robots_url = "https://www.readyratios.com/robots.txt"
robots_response = requests.get(robots_url)
if robots_response.status_code == 200:
    user_agent = "User-agent: *"
    if user_agent in robots_response.text:
        print("Web scraping is allowed for all user-agents.")
        ticker = input("Enter the stock ticker symbol: ")
        url = f"https://www.readyratios.com/sec/{ticker}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            def parse_ratio(text):
                return float(text.replace('%', '').strip())
            ratio_name_elements = soup.find_all('td', class_="ratio-name")
            desktop_path = os.path.expanduser("~/Desktop")
            directory_path = os.path.join(desktop_path, ticker)
            os.makedirs(desktop_path, exist_ok=True)
            file_path = os.path.join(desktop_path, f"{ticker}_info.txt")
            with open(file_path, 'w') as file:
                for ratio_name in ratio_name_elements:
                    if "Debt ratio" in ratio_name.text:
                        print("Debt Ratio: Shows the percentage of a company's assets that are provided via debt. A lower ratio usually means less risk.")
                        file.write("Debt Ratio: Shows the percentage of a company's assets that are provided via debt. A lower ratio usually means less risk.\n")
                        company_score_td = ratio_name.find_next_sibling('td', class_="score")
                        if company_score_td:
                            company_score_span = company_score_td.find('span', class_="val", title="company ratio")
                            if company_score_span:
                                company_ratio = parse_ratio(company_score_span.text)
                                print(f"  Company Ratio: {company_ratio}")
                                file.write(f"  Company Ratio: {company_ratio}\n")

                            industry_score_div = company_score_td.find('div', class_="val-center", title="industry ratio")
                            if industry_score_div:
                                industry_ratio = parse_ratio(industry_score_div.text)
                                print(f"  Industry Average: {industry_ratio}")
                                file.write(f"  Industry Average: {industry_ratio}\n")

                            if company_ratio < industry_ratio:
                                print("  The company's Debt Ratio is lower than the industry average, which is a good thing.")
                                file.write("  The company's Debt Ratio is lower than the industry average, which is a good thing.\n")
                            elif company_ratio > industry_ratio:
                                print("  The company's Debt Ratio is higher than the industry average, which is a bad thing.")
                                file.write("  The company's Debt Ratio is higher than the industry average, which is a bad thing.\n")
                            else:
                                print("  The company's Debt Ratio is equal to the industry average.")
                                file.write("  The company's Debt Ratio is equal to the industry average.\n")

                        print()
                for ratio_name in ratio_name_elements:
                    if "Current Ratio" in ratio_name.text:
                        print("Current Ratio: Ratio that measures whether a firm has enough resources to meet its short-term obligations. A higher ratio typically means better short-term financial health.")
                        file.write("Current Ratio: Ratio that measures whether a firm has enough resources to meet its short-term obligations. A higher ratio typically means better short-term financial health.\n")
                        company_score_td = ratio_name.find_next_sibling('td', class_="score")
                        if company_score_td:
                            company_score_span = company_score_td.find('span', class_="val", title="company ratio")
                            if company_score_span:
                                company_ratio = parse_ratio(company_score_span.text)
                                print(f"  Company Ratio: {company_ratio}")
                                file.write(f"  Company Ratio: {company_ratio}\n")

                            industry_score_div = company_score_td.find('div', class_="val-center", title="industry ratio")
                            if industry_score_div:
                                industry_ratio = parse_ratio(industry_score_div.text)
                                print(f"  Industry Average: {industry_ratio}")
                                file.write(f"  Industry Average: {industry_ratio}\n")

                            if company_ratio > industry_ratio:
                                print("  The company's Current Ratio is higher than the industry average, which is a good thing.")
                                file.write("  The company's Current Ratio is higher than the industry average, which is a good thing.\n")
                            elif company_ratio < industry_ratio:
                                print("  The company's Current Ratio is lower than the industry average, which is a bad thing.")
                                file.write("  The company's Current Ratio is lower than the industry average, which is a bad thing.\n")
                            else:
                                print("  The company's Current Ratio is equal to the industry average.")
                                file.write("  The company's Current Ratio is equal to the industry average.\n")

                        print()
                for ratio_name in ratio_name_elements:
                    if "Profit margin" in ratio_name.text:
                        print("Profit Margin: A measure of how profitable a company is. A higher margin indicates the company is more efficient at converting sales into actual profit.")
                        file.write("Profit Margin: A measure of how profitable a company is. A higher margin indicates the company is more efficient at converting sales into actual profit.\n")
                        company_score_td = ratio_name.find_next_sibling('td', class_="score")
                        if company_score_td:
                            company_score_span = company_score_td.find('span', class_="val", title="company ratio")
                            if company_score_span:
                                company_ratio = parse_ratio(company_score_span.text)
                                print(f"  Company Ratio: {company_ratio}%")
                                file.write(f"  Company Ratio: {company_ratio}%\n")

                            industry_score_div = company_score_td.find('div', class_="val-center", title="industry ratio")
                            if industry_score_div:
                                industry_ratio = parse_ratio(industry_score_div.text)
                                print(f"  Industry Average: {industry_ratio}%")
                                file.write(f"  Industry Average: {industry_ratio}%\n")

                            if company_ratio > industry_ratio:
                                print("  The company's Profit Margin is higher than the industry average, which is a good thing.")
                                file.write("  The company's Profit Margin is higher than the industry average, which is a good thing.\n")
                            elif company_ratio < industry_ratio:
                                print("  The company's Profit Margin is lower than the industry average, which is a bad thing.")
                                file.write("  The company's Profit Margin is lower than the industry average, which is a bad thing.\n")
                            else:
                                print("  The company's Profit Margin is equal to the industry average.")
                                file.write("  The company's Profit Margin is equal to the industry average.\n")

                        print()

            print(f"Information saved to {file_path}")
        else:
            print("There is no data on this company. Please try another ticker.")
    else:
        print("Web scraping is not allowed for this website.")
else:
    print("Failed to fetch the 'robots.txt' file.")
