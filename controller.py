from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content, scraping_df, parser

class Controller:
    link = None  
    parse_desc = (
    "You are a journalist summarizing this page. Extract the main news content only. "
    "Remove all html tags."
    "Divide the article into what happened, the context and its impact."
    "Remove any terms and conditions"
    "Remove any trademarks and copyrights"
    "Do not include unrelated content, code, or metadata. Return only the clean article text."
   
)
    @classmethod
    def get_link(cls, link_number, data):
        if link_number.isdigit():
                    link_number = int(link_number)
                    cls.link = scraping_df(link_number, data)
                    result = scrape_website(cls.link)
                    bc = extract_body_content(result)
                    cc = clean_body_content(bc)
                    body = split_dom_content(cc)
                    llmed = parser(body,cls.parse_desc)
                    #print(f"THE LINK IS HERE: {llmed}")
                    return llmed

    

    
    
                
