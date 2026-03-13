from bs4 import BeautifulSoup


def clean_html(text: str) -> str:
    """
    Convert HTML medical notes into clean text
    """
    if not text:
        return ""

    soup = BeautifulSoup(text, "html.parser")
    cleaned_text = soup.get_text(separator=" ")

    return cleaned_text.strip()