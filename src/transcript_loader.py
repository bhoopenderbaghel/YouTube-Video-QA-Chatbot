from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

def get_transcript(video_id):

    try:
        
        languages = ['en', 'hi', 'es', 'fr']

        transcript_list = YouTubeTranscriptApi().fetch(video_id, languages=languages)

        transcript = " ".join(chunk.text for chunk in transcript_list)

        return transcript

    except TranscriptsDisabled:
        print("Transcripts are disabled for this video.")
        return None