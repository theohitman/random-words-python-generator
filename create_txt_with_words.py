import random

infile = "10000_words.txt"

def generate_the_word(infile):
    random_line = random.choice(open(infile).read().split('\n'))
    return random_line

#Αύξων αριθμός αρχείου
y=0

num_of_files = int(input ("Πόσα αρχεία θέλεις να δημιουργήσω; "))
num_of_files+=1
min_words = int(input ("Ελάχιστος αριθμός λέξεων; "))
#min_words+=1
max_words = int(input ("Μέγιστος αριθμός λέξεων; "))
#max_words+=1

for x in range (1,num_of_files):

    num_of_words = random.randint(min_words,max_words)
    y+=1
    #num_of_words+=1
    for i in range (1,num_of_words):
        f = open("random_file_{0}_with_{1}_words.txt".format(y,num_of_words - 1), "a")
        f.write (generate_the_word(infile))
        f.write (" ")
