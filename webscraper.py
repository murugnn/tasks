import requests
from bs4 import BeautifulSoup

def main():
    url = input("Enter the news website URL (include http/https): ").strip()
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching the URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    titles = []

    for h2 in soup.find_all('h2'):
        text = h2.get_text(strip=True)
        if text:
            titles.append(text)
    
    title_tag = soup.find('title')
    if title_tag:
        titles.append(title_tag.get_text(strip=True))

    if titles:
        with open('headlines.txt', 'w', encoding='utf-8') as f:
            for t in titles:
                f.write(t + '\n')
        print(f"Found {len(titles)} headlines. Saved to 'headlines.txt'.")
    else:
        print("No headlines found on the page.")

if __name__ == "__main__":
    main()
