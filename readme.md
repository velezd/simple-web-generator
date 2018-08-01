# Simple web generator

Simple static web generator created for my own use. Creates static web from files containing html and special commands. Features include blogs, simple pages, links, gallery and download section.

## Directory structure
- **lib** - contains program functions and lookup tables for mimetypes and licenses
- **output** - finished web will be here
- **src** - source files for web generating
	- **downloads** - downloads used on the web
	- **images** - images used on the web
	- **misc** - other files, html files will be processed but will not added to the menu, 404.html, about.html...
	- **pages** - pages that will be shown in the menu
	- **scripts** - javascript goes here
	- **style** - css, and graphics like logos and icons
- **tests** - contains scripts for generating example content that can be used to test functionality

## Usage
- Web configuration like name, index page, web root and copyright information can be set in ./src/web_settings.json
- The main web template is in ./src/page.html
- To create simple page create new directory in ./src/pages. For example: "10-about", the number is required and determines position in the menu, then create index.html iside it.
- To create a blog, create a new directory as before, but inside it create a file blog.json containing { "name": "Blog name" } and a directory named posts, inside it you can then create blog posts... "10-post_name.html". As before the number is required and sets the position of the post in the blog.
- To create link in the menu, create a directory as before and inside it link.json:
	{"name": "GitHub",
	"link": "https://github.com/mygit/"}


### Special commands
**@name:Page Name** - Should be on every page
**@date:July 30 2018** - Only used in blog posts
**@post_image:image.jpg** - Only used in blog posts
**@post_text:This is about...** - Only used in blog posts
**@header_image:image.jpg** - Displays image on top of the page, must be on the first line
**@image:image.jpg:Image comment** - Creates a gallery of small images, generates thumbnail, there must be an empty line after the last image in the gallery
**@bigimage:image.jpg:Image comment** - Shows image scaled to the full with of the web
**@medimage:image comment** - Shows image scaled to about half of the web 
**@download:file.zip:license:link** - Shows download link, a license can be from the list ./lib/licenses.json or custom one - then you should also add link to it

For usage examples check content created by test.sh

The web is generated by running make_web.py

## 3rd party code and assets
- [jQuery](https://jquery.com/)
- [SimpleLightbox](http://simplelightbox.com/)
- [highlight.js](https://highlightjs.org/)
- [Breeze Icons](https://github.com/KDE/breeze-icons)


