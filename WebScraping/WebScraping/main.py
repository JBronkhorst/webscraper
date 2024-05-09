import requests
from bs4 import BeautifulSoup
import time

# User input for excluding jobs
print('Put a job that you want to exclude')
excluded_job = input('>')
print(f'Filtering out {excluded_job}')


def find_jobs():
    # Insert any URL here
    url = "#"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Use a session to retain cookies
    with requests.Session() as session:
        response = session.get(url, headers=headers)
    
        # If website exists/responds
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            jobs = soup.find_all('div', class_ = '')
            # If there are jobs available
            if jobs:
                for index, job in enumerate(jobs):
                    # Exclude the unwanted jobs
                    if excluded_job not in job:
                        # Insert any HTML div classes here to divide job elements
                        job_title = job.find('div', class_ = '').text
                        job_location = job.find('div', class_ = '').text
                        if job_title:
                            with open(f'posts/{index.txt}', 'w') as f:
                                f.write(f"Job title: {job_title.strip()} \n")
                                f.write(f"Job location: {job_location.strip()} \n")
                            print(f'File saved: {index}')    
            else:
                print("No jobs found.")
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)

# Call function every 10 minutes            
if __name__ == '__main__':
        while True:
            find_jobs()
            time_wait = 10
            print(f'Waiting {time_wait} minutes...')
            time.sleep(time_wait * 60)
            
