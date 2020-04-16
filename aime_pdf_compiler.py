import requests
# AIME PDF compiler


def write(file_url, yr):
    r = requests.get(file_url, stream=True)
    name = 'aime' + str(yr) + '.pdf'
    with open(name, "wb") as pdf:
        for part in r.iter_content(chunk_size=1024):
            if part:
                pdf.write(part)


for index in range(4880, 4912):
    pdf_url = "https://artofproblemsolving.com/downloads/printable_post_collections/" + str(index)
    year = index - 2897
    write(pdf_url, year)
