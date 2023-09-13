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
    # result dict <id, (name, birthday)>
    result_dict = {}
    lines = file_content.split("\n")
    for i, record in enumerate(lines):
        items = record.split(",")
        if items[0] == "id":
            continue
        id = int(items[0])
        name = items[1]
        date_str = items[2]
        birthday = datetime.datetime.strptime(date_str, "%d/%m/%Y")

        # print(f"id = {id} | name = {name} | birthday = {birthday:%Y-%m-%d}")
        result_dict[id] = (name, birthday)
        # get rid of the next two lines to process the whole file
        # if there are errors on the data, handle it (you will need to handle the exception)
        if i > 5:
            break

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
    # ask the user for an ID.
    # If ID < 0, exit
    # else, call displayPerson with that ID and the data dict
    displayPerson(3, data_dict)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
