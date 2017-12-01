import re

def parse_nwodkram(text):

	# Changes italic and bold text from nwodkram to HTML
	text = re.sub(r"\*(\w+)\*", r"<i>\1</i>", text)  # italic
	text = re.sub(r"\\\*", r"*", text)   # makes sure that *-symbols are formatted correctly
	text = re.sub(r"\%(\w+)\%", r"<b>\1</b>", text)  # bold
	text = re.sub(r"\\\%", r"%", text)   # # makes sure that %-symbols are formatted correctly


	# Changes hyperlinks from nwodkram to HTML, both starting with www. and http/https
	# If the links doesn't contain http/https, this is added
	text = re.sub(r"\[(.+)\]\((www\..+)\)", r"<a href='http://\2'>\1</a>", text)
	text = re.sub(r"\[(.+)\]\((https?://.+)\)", r"<a href='\2'>\1</a>", text)

	#IMAGE
	text = re.sub(r"<(.+)>\(w=(.+),h=(.+)\)", r"<img src='\1' width='\2' height='\3'>", text)

	#BLOCKQUOTE
	text = re.sub(r">>(.+)", r"<blockquote>\1</blockquote>", text)

	#WIKIPEDIA SEARCH
	text = re.sub(r"\[wp:(.+)\]", r"https://en.wikipedia.org/w/index.php?title=Special:Search&search=\1", text)

	return text
