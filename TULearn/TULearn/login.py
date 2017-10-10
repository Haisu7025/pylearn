from scrapy.http import FormRequest


def start_requests():
    return[
        FormRequest("https://learn.tsinghua.edu.cn/MultiLanguage/lesson/teacher/loginteacher.jsp",
                    formdata={"userid": "yuhs15", "userpass": "YyHhSs971027@"})
    ]
