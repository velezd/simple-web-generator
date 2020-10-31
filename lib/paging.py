from lib.path import src_to_link


def paging_html(page_base_name, num_pages, page_num):
    """ Creates paging html

    :param page_name: path and base name of a page
    :type page_name: str
    :param num_pages: Number of pages
    :type num_pages: int
    :param page_num: Current page number
    :type page_num: int
    """
    html = '<ul class="paging">\n'
    for page in range(num_pages):
        if page == page_num:
            html += '    <li>%i</li>\n' % page
        else:
            page_path = src_to_link(page_base_name % page)
            html += '    <li><a href="%s">%i</a></li>\n' % (page_path, page)
    html += '</ul>'

    return html


def split_list(input_list, max_items):
    """ Splits input list into a multiple lists with maximum number of items in a list.

    :param input_list: Input list to be split
    :type input_list: list
    :param max_items: Maximum number of items per list
    :type max_items: int
    :return: list of lists
    :rtype: list
    """
    lists = list()
    index = 0
    item_num = 0

    for item in input_list:
        try:
            lists[index].append(item)
        except IndexError:
            lists.insert(index, [item])
        item_num += 1
        if item_num % max_items == 0:
            index += 1

    return lists