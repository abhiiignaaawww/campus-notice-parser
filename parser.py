import re
import json

def parse_campus_notice(text):
    """
    Parses unstructured campus text notices to extract key dates, 
    times, and action items using regex pattern matching.
    """
    # Regex patterns for dates, emails, and URLs
    date_pattern = r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})\b'
    email_pattern = r'[a-zA-A0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    url_pattern = r'https?://[^\s]+'

    dates_found = re.findall(date_pattern, text, re.IGNORECASE)
    emails_found = re.findall(email_pattern, text)
    urls_found = re.findall(url_pattern, text)

    # Extract priority keywords
    priority = "NORMAL"
    if any(word in text.lower() for word in ["urgent", "mandatory", "deadline", "important"]):
        priority = "HIGH"

    extracted_data = {
        "priority": priority,
        "extracted_dates": list(set(dates_found)),
        "contact_emails": list(set(emails_found)),
        "links": list(set(urls_found)),
        "status": "Parsed Successfully"
    }

    return json.dumps(extracted_data, indent=4)

if __name__ == "__main__":
    sample_notice = """
    URGENT NOTICE: All students must register for the upcoming campus hackathon by 25 Oct 2026.
    Late submissions will not be accepted. Submit your queries to event@student.nitw.ac.in.
    Form Link: https://forms.gle/samplelink123
    """
    
    print("--- Input Notice ---")
    print(sample_notice.strip())
    print("\n--- Extracted Structured JSON ---")
    print(parse_campus_notice(sample_notice))
