import sys
import os
import glob

import markdown

def generate_html(input_file, html_template):
	html_body = ""
	with open(input_file, "r", encoding="utf-8") as f:
		html_body = markdown.markdown(f.read(), extensions=['extra', 'codehilite'])
	
	return html_template.replace("{html_body}", html_body)

def main():
	exec_dir = os.path.dirname(os.path.abspath(__file__))

	files = glob.glob(os.path.join(exec_dir, 'statements/*.md'))
	output_dir = os.path.join(exec_dir, 'dist')
	if not output_dir:
		print("Error: Didn't provide output folder.")
		sys.exit(1)
		return
	
	html_template = ""
	with open(os.path.join(exec_dir, "template.html"), "r", encoding="utf-8") as f:
		html_template = f.read()
	
	for input_file in files:
		html = generate_html(input_file, html_template)

		page_name = os.path.basename(input_file).replace(".md", "")
		output_path = os.path.join(output_dir, f"{page_name}.html")

		os.makedirs(output_dir)
		with open(output_path, 'w', encoding='utf-8') as f:
			f.write(html)

if __name__ == "__main__":
	main()

