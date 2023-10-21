import re

# Example HTML
html = '''
<noscript>
    <span class="tel-email-on">mail@desarzens-arch</span>
    <span class="tel-email-off">.OMIT</span>
    .ch &nbsp;*
</noscript>
'''

# Remove line breaks and extra whitespace to make the HTML a single line
html = html.replace('\n', '').replace('  ', '')

# Define a regex pattern to match the text between "." and "&nbsp;* </noscript>"


html = html.replace('</span><span class="tel-email-off">.OMIT</span>', '')
html = html.replace('&nbsp;*', '')

# Find and extract the email address
email_pattern = r'<span class="tel-email-on">([^<]+)'

# Use re.search() to find the email address in the HTML
email_match = re.search(email_pattern, html)

if email_match:
    email_address = email_match.group(1)
    print(email_address)
else:
    print("Email address not found")
