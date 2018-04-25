from stackapi import StackAPI
import time
import datetime


def find_question_count(language, startdate, enddate):
    SITE = StackAPI('stackoverflow')
    start = int(time.mktime(datetime.datetime.strptime(startdate, "%d/%m/%Y").timetuple()))
    end = int(time.mktime(datetime.datetime.strptime(enddate, "%d/%m/%Y").timetuple()))
    questions = SITE.fetch('questions', fromdate=start, todate=end, min=1, tagged=language, sort='votes')
    result = questions.get('items')
    return len(result)


if __name__ == "__main__":
    count_java = find_question_count('java', "25/3/2018", "24/4/2018")
    count_python = find_question_count('python', "25/3/2018", "24/4/2018")
    count_c = find_question_count('c', "25/3/2018", "24/4/2018")
    count_cplusplus = find_question_count('c++', "25/3/2018", "24/4/2018")
    count_php = find_question_count('php', "25/3/2018", "24/4/2018")
    count_ruby = find_question_count('ruby', "25/3/2018", "24/4/2018")
    print(count_java, count_php, count_cplusplus, count_python, count_ruby, count_c)
