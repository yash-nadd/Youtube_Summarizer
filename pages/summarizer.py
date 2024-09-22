import sys
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

try:
    # Read the YouTube video ID from file
    with open('texts/video_id.txt', 'r') as file:
        youtube_video = file.read().strip()

    video_id = youtube_video.split("=")[-1]

    # Fetch the transcript for the video
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    result = " ".join([t['text'] for t in transcript])

    # Initialize the summarizer pipeline
    summarizer = pipeline('summarization')

    # Get the desired summary length from command-line arguments
    desired_length = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    num_iters = len(result) // 1000 + 1
    summarized_text = []

    for i in range(num_iters):
        start, end = i * 1000, (i + 1) * 1000
        out = summarizer(result[start:end], max_length=desired_length, min_length=desired_length//2, do_sample=False)[0]['summary_text']
        summarized_text.append(out)

    # Combine the summarized text
    final_summary = " ".join(summarized_text)

    # Format the summary in bullet points
    bullet_points = final_summary.split('. ')
    formatted_summary = "\n".join([f"- {point.strip()}" for point in bullet_points if point])

    # Save the formatted summary to a file
    with open('texts/summary.txt', 'w') as file:
        file.write(formatted_summary)

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
