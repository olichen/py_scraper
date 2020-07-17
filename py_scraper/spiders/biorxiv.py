import scrapy
import w3lib.html


class BiorxivSpider(scrapy.Spider):
    name = 'biorxiv'

    def start_requests(self):
        url = 'https://www.biorxiv.org/search/'
        if search := getattr(self, 'search', None):
            url = url + search
        else:
            raise Exception('Please define a search term.')
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        paper_links = response.css('a.highwire-cite-linked-title')
        yield from response.follow_all(paper_links, self.parse_paper)

        next_page_link = response.css('a.link-icon-after')
        yield from response.follow_all(next_page_link, self.parse)

    def parse_paper(self, response):
        def extractmeta(query):
            query = f"//meta[@name='{query}']/@content"
            output = response.xpath(query).getall()
            return list(map(str.strip, output))

        output = {
            'title': extractmeta('DC.Title'),
            'date': extractmeta('DC.Date'),
            'email': extractmeta('citation_author_email'),
            'url': response.request.url,
        }

        query = "//div[contains(@class, 'author-tooltip-name')]/.."
        authors = response.xpath(query)
        for i, author in enumerate(authors, 1):
            def extract(query):
                output = author.css(query).getall()
                output = map(w3lib.html.remove_tags, output)
                return list(map(str.strip, output))
            output[i] = {
                'name': extract('div.author-tooltip-name::text'),
                'affiliation': extract('div.author-affiliation'),
                'email': extract('li.author-corresp-email-link>span>a::text'),
            }
        yield output
