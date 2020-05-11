import requests
import json

data = []
headers = None #这里替换一下自己获取到的headers

def get_exercise_ids():
    print('cid(比如1515741) : ')
    cid = input()
    print('sign(比如THU08091000247): ')
    sign = input()
    params = (
        ('cid', cid),
        ('sign', sign),
        ('etag_id', 11), #etag参数可以用于过滤目录内容,11即只有作业
    )
    index_json_url = 'https://next.xuetangx.com/api/v1/lms/learn/course/chapter'
    index_dict = requests.get(index_json_url, headers = headers, params=params ).json()
    print(index_dict)

    #course_name = index_dict['data']['course_name']
    #course_id = index_dict['data']['course_id']
    course_chapters = index_dict['data']['course_chapter']
    for chapter in course_chapters:
        chapter_name = chapter['name']
        #chapter_id = chapter['id']
        course_sections = chapter['section_leaf_list'] #部分section下没有leaf 所以要下面加一个判定,这也是为什么这里叫section_leaf_list
        for section in  course_sections:
            if 'leaf_list' in section:
                course_leafs = section['leaf_list']
                for leaf in course_leafs:
                    leaf_name = leaf['name']
                    leaf_id = leaf['id']
                    data.append({"chapter_name": chapter_name, "exercise_name": leaf_name , "leaf_id":leaf_id})
                    #leaf_type = leaf['leaf_type']
            else:
                leaf_name = section['name']
                leaf_id = section['id']
                data.append({"chapter_name": chapter_name, "exercise_name": leaf_name, "leaf_id": leaf_id})
                #leaf_type = section['leaf_type']
    return cid, sign
def get_exercise_leaf_type_ids():
    cid, sign = get_exercise_ids()
    params = (
        ('sign', sign),
    )

    for each in data:
        leafinfo_url = 'https://next.xuetangx.com/api/v1/lms/learn/leaf_info/'+ str(cid) + '/' + str(each['leaf_id']) +'/'
        leafinfo_dict = requests.get(leafinfo_url, headers=headers, params=params).json()
        leaf_type_id = leafinfo_dict['data']['content_info']['leaf_type_id']
        each['leaf_type_id'] = leaf_type_id

def get_answers():
    for each in data:
        exercise_url = 'https://next.xuetangx.com/api/v1/lms/exercise/get_exercise_list/' + str(each['leaf_type_id']) + '/'
        exercise_dict = requests.get(exercise_url, headers=headers).json()
        #problem_name = problem_dict['data']['description']
        problems = exercise_dict['data']['problems']
        answers = {}
        for problem in problems:
            count =  str(problem['index'])
            problem_type = problem['content']['Type']
            if problem_type == 'SingleChoice':
                answer = problem['user']['answer'][0]
                answers[count] = answer
            elif problem_type == 'FillBlank':
                answer = problem['user']['answers'] # a dict
                answers[count] = answer
            elif problem_type == 'Judgement':
                answer = problem['user']['answer']
                answers[count] = answer[0]
            elif problem_type == 'MultipleChoice':
                answer = problem['user']['answer'] # a list
                answers[count] = answer
            else:
                print('题目类型未知，请反馈一下下面的ID\n')
                print(each['leaf_type_id'])
        each['answers'] = answers
def data2json(): #输出JSON备用
    with open("data.json", "w") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4, separators=(',', ':')))

get_exercise_leaf_type_ids()
get_answers()
data2json()