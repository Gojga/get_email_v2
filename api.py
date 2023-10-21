import requests
import re
def get_link(page):
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }
    params = {
        'was': "bureau d'architecte",
        'wo': 'vaud',
        'firma': '1',
        'pages': page,
    }

    response = requests.get('https://search.ch/tel/', params=params, headers=headers)
    pattern = r'<td\s+rowspan="2"\s+class="tel-result-left">\s*<a\s+href="([^"]+)">'

# Use re.findall() to extract all links into a list
    links = re.findall(pattern, response.text)
    return(links)

def get_mail(url):
    cookies = {
    'crustulum': '02e8009e32867044',
    'myosotis': '465eb8c352d8aba4166018b0f9da02f3',
}

    headers = {
        'authority': 'search.ch',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-GB,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': 'crustulum=02e8009e32867044; myosotis=465eb8c352d8aba4166018b0f9da02f3',
        'referer': 'https://search.ch/tel/?was=bureau+d%27architecte&wo=vaud&firma=1&pages=6',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    response = requests.get(
        f'https://search.ch/{url}',
        cookies=cookies,
        headers=headers,
    )
    email_pattern = r'<span class="tel-email-on">([^<]+)</span>'

# Define a regex pattern to check for advertising material
    advertising_pattern = r'\* No advertising material'

    # Use re.findall() to extract email addresses
    email_addresses = re.findall(email_pattern, response.text)

    # Check for advertising material and filter email addresses
    filtered_email_addresses = []
    for email in email_addresses:
        if not re.search(advertising_pattern, email):
            filtered_email_addresses.append(email)
        else:
            return 0
    title_pattern = r'<title>(.*?)</title>'
    title_match = re.search(title_pattern, response.text)

    # Extract the title if found
    title = title_match.group(1) if title_match else ""
    html = response.text.replace('\n', '').replace('  ', '')

# Define a regex pattern to match the text between "." and "&nbsp;* </noscript>"


    html = html.replace('</span><span class="tel-email-off">.OMIT</span>', '')
    html = html.replace('&nbsp;*', '')

    # Find and extract the email address
    email_pattern = r'<span class="tel-email-on">([^<]+)'

    # Use re.search() to find the email address in the HTML
    email_match = re.search(email_pattern, html)

    if email_match:
        email_address = email_match.group(1)
        return(f"{email_address},{title}")