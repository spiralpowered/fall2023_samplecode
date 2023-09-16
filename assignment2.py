import argparse
import urllib.request
import logging
import datetime


def downloadData(url):
    """
        Reads data from a URL and returns the data as a string

        :param url:
        :return: the content of the URL
        """
    # read the URL
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response


def processData(file_content):
    """
    (from the assignment) write a function that takes the contents of the
    file as the first parameter, processes the file line by line,
    and returns a dictionary that maps a person’s ID to a tuple of the form (name, birthday).

    The birthday needs to be a Datetime object, not a string. The format "%d/%m/%Y"

    :param file_content:
    :return:
    """
    # configures log error level & creates log file
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    
    # result dict <id, (name, birthday)>
    result_dict = {}
    lines = file_content.split("\n")
    for i, record in enumerate(lines):
        # assigns each item to dict
        try:
            items = record.split(",")
            if items[0] == "id":
                continue
            id = int(items[0])
            name = items[1]
            date_str = items[2]
        except Exception as e:
            print(e)

        # checks date for correct format
        try:
            birthday = datetime.datetime.strptime(date_str, "%d/%m/%Y")
        # handles the ValueError by updating log when an invalid date is found
        except ValueError:
            logging.error(f"Error processing line {i} for ID {id}")
        # updates the dictionary
        else:
            # print(f"id = {id} | name = {name} | birthday = {birthday:%Y-%m-%d}")
            result_dict[id] = (name, birthday)

    return result_dict

def displayPerson(id, personData):
    # if the ID is not in the dictionary, print "No user found with that id
    # (There is going to be an exception that you need to handle)
    name, birthday = personData[id]
    print(f"{name} was born on {birthday:%Y-%m-%d}")


def main(url):
    print(f"Running main with URL = {url}...")
    url_data = downloadData(url)
    data_dict = processData(url_data)


    # If ID < 0, exit
    try:
        user_id = int(input("Enter an ID: "))
        if user_id <= 0:
            exit()

    # else, call displayPerson with that ID and the data dict
        else:
            displayPerson(user_id, data_dict)
    except Exception:
        print("No user found with that ID")

if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
