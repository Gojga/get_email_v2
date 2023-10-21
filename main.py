from api import *


emails = []
for j in range(20):
    links = get_link(j)
    for i in range(len(links)):
        emails.append(get_mail(links[i]))
        
    output_file_name = "email_addresses.txt"

    # Open the text file for writing
    with open(output_file_name, "w") as file:
        # Write each email address as a separate line in the file
        for email in emails:
            if email is not None:
                file.write(email + "\n")

print("finished")