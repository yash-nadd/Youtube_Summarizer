import sys
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

def main():
    try:
        # Read the YouTube video ID from file
        with open('pages/texts/video_id.txt', 'r') as file:
            youtube_video = file.read().strip()
        print(f"Debug: YouTube Video URL: {youtube_video}")

        video_id = youtube_video.split("=")[-1]
        print(f"Debug: Extracted Video ID: {video_id}")

        # Fetch the transcript for the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        result = " ".join([t['text'] for t in transcript])
        print(f"Debug: Transcript Length: {len(result)} characters")

        # Initialize the summarizer pipeline
        summarizer = pipeline('summarization')
        print("Debug: Summarizer pipeline initialized.")

        # Get the desired summary length from command-line arguments
        desired_length = int(sys.argv[1]) if len(sys.argv) > 1 else 100
        print(f"Debug: Desired Summary Length: {desired_length}")

        # Summarize the transcript in chunks
        num_iters = len(result) // 1000 + 1
        summarized_text = []

        for i in range(num_iters):
            start, end = i * 1000, (i + 1) * 1000
            print(f"Debug: Summarizing from index {start} to {end}...")
            out = summarizer(result[start:end], max_length=desired_length, min_length=desired_length//2, do_sample=False)[0]['summary_text']
            summarized_text.append(out)

        # Combine the summarized text
        final_summary = " ".join(summarized_text)

        # Format the summary in bullet points
        bullet_points = final_summary.split('. ')
        formatted_summary = "\n".join([f"- {point.strip()}" for point in bullet_points if point])

        # Save the formatted summary to a file
        with open('pages/texts/summary.txt', 'w') as file:
            file.write(formatted_summary)
        print("Debug: Summary saved to pages/texts/summary.txt.")

    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
        print("Debugging information:")
        try:
            print(f"Video ID: {video_id}")
            print(f"Transcript Length: {len(result)}")
            print(f"Desired Length: {desired_length}")
        except NameError:
            print("Error: Unable to retrieve video ID or transcript length due to previous error.")
        sys.exit(1)

if __name__ == "__main__":
    main()
