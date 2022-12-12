
# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5


def start_of_packet(buffer):
    i = 0
    while i < len(buffer) - 4:
        start = 0 + i
        length = 4 + i
        chunk = buffer[start:length]

        # Remove duplicate characters from string
        if len(chunk) == len(''.join(dict.fromkeys(chunk))):
            # start of packet found
            return length

        i = i + 1


with open('input.txt') as f:
    lines = f.read().split("\n")
    for line in lines:
        if len(line.strip()) > 0:
            print(f"First marker after character: {start_of_packet(line)}")
