# the Python client for Grakn
# https://github.com/graknlabs/client-python
from grakn.client import GraknClient

# Python's built in module for dealing with .csv files.
# we will use it read data source files.
# https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters
import csv


def build_my_graph(inputs, data_path, keyspace_name):
    """
      gets the job done:
      1. creates a Grakn instance
      2. creates a session to the targeted keyspace
      3. for each input:
        - a. constructs the full path to the data file
        - b. loads csv to Grakn
      :param input as list of dictionaties: each dictionary contains details required to parse the data
    """
    with GraknClient(uri="localhost:48555") as client:  # 1
        with client.session(keyspace=keyspace_name) as session:  # 2
            for input in inputs:
                input["file"] = input["file"].replace(data_path, "")  # for testing purposes
                input["file"] = data_path + input["file"]  # 3a
                print("Loading from [" + input["file"] + ".csv] into Grakn ...")
                load_data_into_grakn(input, session)  # 3b


def load_data_into_grakn(input, session):
    """
      loads the csv data into our Grakn phone_calls keyspace:
      1. gets the data items as a list of dictionaries
      2. for each item dictionary
        a. creates a Grakn transaction
        b. constructs the corresponding Graql insert query
        c. runs the query
        d. commits the transaction
      :param input as dictionary: contains details required to parse the data
      :param session: off of which a transaction will be created
    """
    items = parse_data_to_dictionaries(input)  # 1

    for item in items:  # 2
        with session.transaction().write() as transaction:  # a
            graql_insert_query = input["template"](item)  # b
            print("Executing Graql Query: " + graql_insert_query)
            transaction.query(graql_insert_query)  # c
            transaction.commit()  # d

    print("\nInserted " + str(len(items)) +
          " items from [ " + input["file"] + ".csv] into Grakn.\n")

##
# Attribute insert definitions
#
#
def hour_template(hours):
    # insert integers
    return 'insert $num isa hour; $num "'+ hours["num"] + '";'

def minute_template(mins):
    # insert integers
    return 'insert $num isa minute; $num "'+ mins["num"] + '";'

def second_template(secs):
    # insert boolean
    return 'insert $num isa second; $num "'+ secs["num"] + '";'

def remain_template(remrem):
    # insert boolean
    return 'insert $num isa remainder; $num '+ remrem["rem"] + ';'



##
# Relationship insert definitions

def addh_template(addh):
    # match addee
    graql_insert_query = 'match $addee isa hour; $addee "' +  addh["addee"] + '";'
    # match addor
    graql_insert_query += ' $addor isa hour; $addor "' +  addh["addor"] + '";'
    # match resnum
    graql_insert_query += ' $resnum isa hour; $resnum "' +  addh["resnum"] + '";'
    # match remres
    graql_insert_query += ' $remres isa hour; $remres "' +  addh["remres"] + '";'
    # match remnum
    graql_insert_query += ' $remnum isa remainder; $remnum ' +  addh["remnum"] + ';'
    # match remrem
    graql_insert_query += ' $remrem isa remainder; $remrem ' +  addh["remrem"] + ';'
    # insert addi
    graql_insert_query += " insert (addeeh: $addee, addorh: $addor, resulth: $resnum, remresh: $remres, resrem: $remnum, remrem: $remrem) isa addhour;"
    return graql_insert_query
    

def addm_template(addm):
    # match addee
    graql_insert_query = 'match $addee isa minute; $addee "' +  addm["addee"] + '";'
    # match addor
    graql_insert_query += ' $addor isa minute; $addor "' +  addm["addor"] + '";'
    # match resnum
    graql_insert_query += ' $resnum isa minute; $resnum "' +  addm["resnum"] + '";'
    # match remres
    graql_insert_query += ' $remres isa minute; $remres "' +  addm["remres"] + '";'
    # match remnum
    graql_insert_query += ' $remnum isa remainder; $remnum ' +  addm["remnum"] + ';'
    # match remrem
    graql_insert_query += ' $remrem isa remainder; $remrem ' +  addm["remrem"] + ';'
    # insert addi
    graql_insert_query += " insert (addeem: $addee, addorm: $addor, resultm: $resnum, remresm: $remres, resrem: $remnum, remrem: $remrem) isa addmin;"
    return graql_insert_query

def adds_template(adds):
    # match addee
    graql_insert_query = 'match $addee isa second; $addee "' +  adds["addee"] + '";'
    # match addor
    graql_insert_query += ' $addor isa second; $addor "' +  adds["addor"] + '";'
    # match resnum
    graql_insert_query += ' $resnum isa second; $resnum "' +  adds["resnum"] + '";'
    # match remres
    graql_insert_query += ' $remres isa second; $remres "' +  adds["remres"] + '";'
    # match remnum
    graql_insert_query += ' $remnum isa remainder; $remnum ' +  adds["remnum"] + ';'
    # match remrem
    graql_insert_query += ' $remrem isa remainder; $remrem ' +  adds["remrem"] + ';'
    # insert addi
    graql_insert_query += " insert (addees: $addee, addors: $addor, results: $resnum, remress: $remres, resrem: $remnum, remrem: $remrem) isa addsec;"
    return graql_insert_query
    


def parse_data_to_dictionaries(input):
    """
      1. reads the file through a stream,
      2. adds the dictionary to the list of items
      :param input.file as string: the path to the data file, minus the format
      :returns items as list of dictionaries: each item representing a data item from the file at input.file
    """
    items = []
    with open(input["file"] + ".csv") as data:  # 1
        for row in csv.DictReader(data, skipinitialspace=True):
            item = {key: value for key, value in row.items()}
            items.append(item)  # 2
    return items


Inputs = [
    {
        "file": "numh",
        "template": hour_template
    },
    {
        "file": "numm",
        "template": minute_template
    },
    {
        "file": "nums",
        "template": second_template
    },
    {
        "file": "remain",
        "template": remain_template
     },
    {
        "file": "addh",
        "template": addh_template
    },
    {
        "file": "addm",
        "template": addm_template
    },
    {
        "file": "adds",
        "template": adds_template
    }
]

if __name__ == "__main__":
    build_my_graph(inputs=Inputs, data_path="data\\", keyspace_name = "time_trial")
