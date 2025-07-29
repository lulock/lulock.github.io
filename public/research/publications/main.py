from bs4 import BeautifulSoup
import requests

MYURL = "https://scholar.google.com/citations?hl=en&user=X5aaOeYAAAAJ&view_op=list_works&sortby=pubdate"
def main():
    print("Hello from publications!")
    try:
        url = MYURL
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for article in soup.select(".gsc_a_tr"):
            results.append({
                "title": article.select(".gsc_a_at")[0].text,
                "link": article.select(".gsc_a_at")[0]["href"],
                "authors": article.select(".gs_gray")[0].text,
                "venue": article.select(".gs_gray")[1].text,
                })

        print(results)

        markdown_out = f"---\ntitle: 'PhD Research'\ndescription: 'Learn about my research interests.'\ncascade:\n    showReadingTime: false\n---\n\nThis section contains all my research interests / projects\n\n## Publications\n"
        
        for article in results:
            markdown_out += f"- **[{article['title']}]({article['link']})**\n{article['authors']}\n_{article['venue']}_.\n"
        
        markdown_out += "\n### Talks \n\n"

        with open("../_index.md", "w") as f:
            f.write(markdown_out)
    
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
