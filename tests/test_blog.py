import os


def test_blog():
    if os.path.exists('../src/pages'):
        if not os.path.exists('../src/pages/90-test_blog'):
            os.mkdir('../src/pages/90-test_blog')

        if not os.path.exists('../src/pages/90-test_blog/posts'):
            os.mkdir('../src/pages/90-test_blog/posts')

        data = '{\n    "name": "Test Blog"\n}'
        with open('../src/pages/90-test_blog/blog.json', 'w') as file:
            file.write(data)

        html = """
@header_image:test_horizontal.png
@name:First post
@date:March 20 2018
@post_image:test_horizontal.png
@post_text:Tests post containing post_image, header_image, post_text and date
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in magna velit. Vestibulum ante ipsum primis in 
faucibus orci luctus et ultrices posuere cubilia Curae; Cras sollicitudin lorem nec nibh pellentesque vestibulum. 
Vivamus euismod vel lacus id sollicitudin. Proin lobortis libero ut fringilla feugiat. Ut semper sem sit amet justo placerat, 
sed laoreet massa mollis. Pellentesque posuere varius ipsum, ac vestibulum ipsum malesuada ac. Pellentesque fringilla 
dictum sapien, ac sodales nibh mattis vel. Aenean luctus neque venenatis nunc porttitor blandit. Ut lacus ante, 
rhoncus ac hendrerit a, finibus in leo. </p>
        """
        with open('../src/pages/90-test_blog/posts/10-post_one.html', 'w') as file:
            file.write(html)

        # Create more posts for pageing testing
        for x in range(0, 20):
            html = """
@name:Minimal information %s
<p>The simplest post you can create.</p>
<p>Only name is defined.</p>
            """ % str(x)
            with open('../src/pages/90-test_blog/posts/2%s-minimal%s.html' % (str(x), str(x)), 'w') as file:
                file.write(html)

        html = """
@name:Typical post - longer name :)
@date:January 11 2027
@post_image:test_vertical.png
@post_text:Typical post with some example content
<p>Typical post with some example content, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in magna velit. 
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Cras sollicitudin lorem nec 
nibh pellentesque vestibulum. Vivamus euismod vel lacus id sollicitudin. Proin lobortis libero ut fringilla feugiat.</p>

@image:test_vertical.png:Vertical image
@image:test_horizontal.png
@image:test_square.png

<center>
<table>
    <tr><th>Header 1</th><th>Header 2</th><th>Header 3</th></tr>
    <tr><td>A</td><td colspan="2">B</td></tr>
    <tr><td>1</td><td>2</td><td>3</td></tr>
    <tr><td>A</td><td colspan="2">B</td></tr>
    <tr><td>1</td><td>2</td><td>3</td></tr>
</table>
</center>

<p>Vivamus euismod vel lacus id sollicitudin. Proin lobortis libero ut fringilla feugiat. Ut semper sem sit amet justo placerat, 
sed laoreet massa mollis. Pellentesque posuere varius ipsum, ac vestibulum ipsum malesuada ac. Pellentesque fringilla 
dictum sapien, ac sodales nibh mattis vel. Aenean luctus neque venenatis nunc porttitor blandit. Ut lacus ante, 
rhoncus ac hendrerit a, finibus in leo.</p>

@download:image-x-generic.svg:CC BY-SA
    
        """
        with open('../src/pages/90-test_blog/posts/30-typical.html', 'w') as file:
            file.write(html)

        html = """
Broken blog post
        """
        with open('../src/pages/90-test_blog/posts/40-broken.html', 'w') as file:
            file.write(html)


if __name__ == '__main__':
    test_blog()