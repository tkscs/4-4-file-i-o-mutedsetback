# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

####
#### YOUR CODE HERE 
with open("romeo_and_juliet.txt", "r") as f:
    text = f.read()
    print(text)
####

# Count how many times the word "Juliet" appears

####
#### YOUR CODE HERE 
with open("romeo_and_juliet.txt", "r") as f:
    text = f.read()
    count = text.count("Juliet")
    print(count)
####
