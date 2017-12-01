import re, requests

def find_emails(text):

	name = r"\w*[.#$%&~'*+\-/=?`{}]?\w*"
	server = r"\w*[.#$%&~'*+\-/=?`{}]?\w*"
	domain = r"[a-zA-Z]+[.]*[a-zA-Z]+"

	# Pattern of a valid email adress
	regex = name + "@" + server + "\." + domain

	# Stores as matches in a list
	matches = re.findall(regex, text)

	return matches

def find_urls(text):

	#protocol = r"""https?://(?:www\.)?"""
	#host = r"""[\w.\-~]+"""
	#domain = host
	#path = r"""[\w\.\-~\/]+"""

	# Pattern of a valid URL
	regex1 = r"""<a href=("|')((?:https?://)(?:www\.)?[\w\.\-~]+[\w\.\-~\/]+)\1.*?</a>"""
	# Pattern that also matches relative hyperlinks
	regex2 = r"""<a href=("|')([\w\-~]+\.html)\1.*?</a>"""

	# Stores all matches in a list
	matches = re.findall(regex1, text, re.S)
	matches += re.findall(regex2, text, re.S)

	# The matches above are returning two matches groups: the adress itself and ('|") (needed for bactracking)
	# The following only stores the link
	if len(matches) > 0:
		matches = [matches[i][1] for i in range(len(matches))]

	return matches

def all_the_emails(url, depth, all_urls = [], all_emails = []):

	#Fetches the HTML document
	html = requests.get(url)

	# Finds the emails and urls found in the HTML (stored in lists)
	urls = find_urls(html.text)
	emails = find_emails(html.text)

	all_emails.extend(emails)

	# Saves the current url as a variable, needed when handling the relative hyperlinks
	parenturl = url

	for url in urls:

		# Default HTML, this is already searched
		if url == 'index.html':
			urls.remove(url)
			continue
		# Stops when the wanted depth is reached
		if depth == 0:
			continue

		# Doesn't search if it has already been seached
		if url in all_urls:
			continue

		# Adds the parentURL to the relative hyperlink
		url = re.sub(r"([\w\.\-~]+\.html)", parenturl + r"\1", url)
		print("Searching in:", url)
		all_urls.append(url)
		#The function calls itself, now with the new url
		all_the_emails(url, depth - 1, all_urls, all_emails)

	#Removing empty strings and duplicates, and sorting after email server
	return sorted(list(set(filter(None, all_emails))), key = lambda x: x.split("@")[1])

if __name__ == "__main__":
	print("Aquired emails:\n", all_the_emails('https://lucidtech.io/', 1))
