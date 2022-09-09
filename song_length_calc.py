import sys

key_sig = int(input("How many beats in a measure "))
type(key_sig)
num_of_measures = int(input("How many measures? "))
type(num_of_measures)
tempo = int(input("What is the tempo?"))
song_length = key_sig * num_of_measures / tempo * 60



print(f'{song_length}')