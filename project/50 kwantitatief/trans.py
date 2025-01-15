import json

def transform_transcript(json_file, output_file):
    # Load JSON data
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract relevant data
    segments = data.get('segments', [])
    chunks = data.get('chunks', [])

    # Initialize the "prev" pointer
    prev = 0
    formatted_transcript = []

    # Iterate through each segment
    for segment in segments:
        label = segment.get('label', 'Unknown Speaker')
        start = segment.get('start', 0.0)
        end = segment.get('end', 0.0)
        if label == 'NO_SPEAKER':
            continue

        # Collect chunks within the current segment
        segment_chunks = []
        for i in range(prev, len(chunks)):
            chunk = chunks[i]
            chunk_start, chunk_end = chunk.get('timestamp', [0.0, 0.0])

            # Check if the chunk falls within the segment's time range
            if chunk_end <= end:
                segment_chunks.append(chunk.get('text', '').strip())
            else:
                # Update the prev pointer and exit the loop
                prev = i
                break

        # Add the formatted segment text
        if segment_chunks:
            speaker_text = f"{label}: {' '.join(segment_chunks)}"
            formatted_transcript.append(speaker_text)

    # Write the formatted transcript to a text file
    with open(output_file, 'w') as file:
        for line in formatted_transcript:
            file.write(line + '\n\n')

# Usage example
transform_transcript('transcript.json', 'transcript.txt')
