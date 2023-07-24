# this will be exam prep that will deal with
# creating module that will take test data from a list
# and by creating a module(s) you will be able to find the
# median, min, max, average, and number of scores evaluated
# use the test values provided to create the program
# have a function that can add new values to the list(int)
# the output should have both the median,min,max ,average of
# the initial scores and the new data from the new test values entered
# and a function to exit the main program after done using
import pickle
# test values to add to the mix: 49, 99, 22,10
test_values = [96, 29, 77, 50, 46, 43, 32, 28, 84, 26, 90, 69, 64, 42, 44, 79, 92, 86, 40, 98]

def add_value(test_values):
    print("Enter 'x' to exit score compiler")
    while True:
        try:
            new = input("Enter test score: ")
            if new.lower() != 'x':
                test_values.append(int(new))
            else:
                break
        except ValueError:
            print("Enter the test score as an integer")
    return test_values

def send_to_binary(filename, alldata):
    with open(filename, 'wb') as file:
        pickle.dump(alldata, file)

def read_binary(filename):
    with open(filename, 'rb') as file:
        alldata = pickle.load(file)
        print(alldata)

def crunch_data(test_values):
    total = sum(test_values)
    average = round(total / len(test_values))
    sorted_values = sorted(test_values)
    median_index = len(sorted_values) // 2
    median = sorted_values[median_index]
    minimum = min(sorted_values)
    maximum = max(sorted_values)
    return average, median, minimum, maximum

def display(test_values):
    avg, med, minimum, maximum = crunch_data(test_values)
    print(f"Average Score: {avg} \nMedian Score: {med}\nLowest score: {minimum}\nHighest Score: {maximum}")
    data = [avg, med, minimum, maximum]
    return [data]

def main():
    print("Test Score Program\n")
    filename = input("Please enter the filename: ")
    test_values = [96, 29, 77, 50, 46, 43, 32, 28, 84, 26, 90, 69, 64, 42, 44, 79, 92, 86, 40, 98]
    print("Initial Scores: ")
    initial_data = display(test_values)
    send_to_binary(filename, initial_data)
    read_binary(filename)

    print("The teacher did not include all of the scores, please add the ones they missed.")
    repeat = 'y'
    while repeat == 'y':
        new_values = add_value(test_values)
        updated_data = display(new_values)
        previous_data = []
        with open(filename, 'rb') as file:
            previous_data = pickle.load(file)
        send_to_binary(filename, previous_data + updated_data)
        read_binary(filename)
        repeat = input("Compile more? (y/n): ")
    read_binary(filename)
main()


