from urllib.parse import urlparse, parse_qs


def extract_video_id(url: str) -> str:
    """
    Extract the video ID from a YouTube URL.
    Supports both youtube.com and youtu.be formats.
    """

    parsed_url = urlparse(url)

    # Short URL format
    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]

    # Standard YouTube URL
    if parsed_url.hostname in ("www.youtube.com", "youtube.com"):
        query = parse_qs(parsed_url.query)
        return query.get("v", [None])[0]

    raise ValueError("Invalid YouTube URL")