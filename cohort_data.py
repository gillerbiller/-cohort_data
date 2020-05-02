"""Functions to parse a file containing student data."""


def all_houses(filename): 
    """Return a set of all houses"""
  
    unique_houses = open("cohort_data.txt")

    every_house = []

    for item in unique_houses:

      item = item.rstrip()

      sectioned_cohort_data = item.split('|')

      house_names = sectioned_cohort_data[2]

      if house_names == "":
        continue
      else:  
        every_house.append(house_names)
      
    houses = set(every_house)

    unique_houses.close()

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort."""

    students_and_cohorts = open("cohort_data.txt")

    students = []

    for item in students_and_cohorts:

      item = item.rstrip()

      split_cohort_data = item.split('|')

      student_first_name = split_cohort_data[0]

      student_last_name = split_cohort_data[1]

      student_cohort = split_cohort_data[4] #broke the code for hours by 
      #assigning this to cohort which was already a place in memory as the 
      #argument 

      student_full_name = student_first_name+ " " + student_last_name

      if student_cohort == "G" or student_cohort == "I":
        continue
    
      elif cohort ==  student_cohort:
        students.append(student_full_name)

      elif cohort == "All":
        students.append(student_full_name)

    return sorted(students)
    
def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors."""
    
    students_within_a_house = open("cohort_data.txt")

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    for item in students_within_a_house:

      item = item.rstrip()

      splitup_cohort_data = item.split('|')

      student_first_name = splitup_cohort_data[0]

      student_last_name = splitup_cohort_data[1]

      house_name = splitup_cohort_data[2]

      cohort_name = splitup_cohort_data[4]

      student_full_name = student_first_name+ " " + student_last_name

      if house_name == "" and cohort_name == "G":
        ghosts.append(student_full_name)

      elif house_name == "" and cohort_name == "I":
        instructors.append(student_full_name)

      elif house_name == "Dumbledore's Army":
        dumbledores_army.append(student_full_name)

      elif house_name == "Gryffindor":
        gryffindor.append(student_full_name)

      elif house_name == "Hufflepuff":
        hufflepuff.append(student_full_name)

      elif house_name == "Ravenclaw":
        ravenclaw.append(student_full_name)

      elif house_name == "Slytherin":
        slytherin.append(student_full_name)

    dumbledores_army.sort()
    gryffindor.sort()
    hufflepuff.sort()
    ravenclaw.sort()
    slytherin.sort()
    ghosts.sort()
    instructors.sort()

    all_houses = [dumbledores_army, gryffindor, hufflepuff, ravenclaw, 
    slytherin, ghosts, instructors]

    return (all_houses)


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
