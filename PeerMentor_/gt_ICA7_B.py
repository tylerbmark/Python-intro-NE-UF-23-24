# gt_ICA7_B.py
# Stors a list of birds along with a count of the number
# of times each bird has been spotted

# Input: filename, bird

# Output: display: name, count
import pickle

def read_binary(filename):
    try:
        with open(filename, 'rb') as file:
            alldata = pickle.load(file)
    except FileNotFoundError:
        alldata = {}
        print(f'Cannot find the file "{filename}"')
        send_to_binary(filename,alldata)
        print(f"Creating file named: {filename}.....")
    return alldata
def send_to_binary(filename, alldata):
    with open(filename, 'wb') as file:
        pickle.dump(alldata, file)

def display_birds(birds):
    sorted_birds = sorted(birds.items(), key=lambda x: x[0])
    print(f"{'Name:': <35} {'Count:'}")
    print(f"{'----'*7:<35} {'------'} ")
    for bird,count in sorted_birds:
        print(f"{bird.title():<35} {count}")

def main():
    filename = input("Enter a filename {.bin}:")
    birds = read_binary(filename)
    name = ''
    while name != 'x':
        name = input("Enter name of bird: ")
        if name.lower() !='x':
            name = name.title()
            birds[name] = birds.get(name,0) + 1
    send_to_binary(filename,birds)
    display_birds(birds)
main()

