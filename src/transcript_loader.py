from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi().fetch(video_id, languages=['en'])
        transcript = " ".join(chunk.text for chunk in transcript_list)
        return transcript
    except TranscriptsDisabled:
        return None