#! /usr/bin/env python3
import os, sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 wordCount.py <input text file> <output file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if not os.path.exists(input_file):
        print("text file input %s doesn't exist! Exiting" % input_file)
        sys.exit(1)
    file_details = os.open(input_file, os.O_RDONLY)
    byte_buffer = os.read(file_details, 1)
    str_buffer = []
    word_counts = dict()
    while len(byte_buffer) > 0:
        tmp_str = byte_buffer.decode()
        if not tmp_str.isalpha():
            if len(str_buffer) == 0:
                byte_buffer = os.read(file_details, 1)
                continue
            word = "".join(l.lower() for l in str_buffer)
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
            str_buffer.clear()
        else:
            str_buffer.append(tmp_str)
        byte_buffer = os.read(file_details, 1)
    os.close(file_details)
    output_buffer = os.open(output_file, os.O_CREAT | os.O_WRONLY)
    for word in sorted(word_counts.keys()):
        os.write(output_buffer, (word + " " + str(word_counts[word]) + "\n").encode())
    os.close(output_buffer)
    
if __name__ == "__main__":
    main()
