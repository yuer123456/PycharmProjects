from pprint import pprint
import requests

def test_requests():
    r = requests.get("https://home.testing-studio.com/categories.json")
    print(r.status_code)
    pprint(r)

    print(r.json())
    assert r.status_code==200
def test_get():
    r = requests.get("https://httpbin.testing-studio.com/get",
                     params={
                         "a":1,
                         "b":2,
                         "c":"cccc"

    })
    print(r.status_code)
    assert r.status_code==200
    pprint(r)
def test_post():
    r = requests.post("https://httpbin.testing-studio.com/post",
                      params={
                          "a": 1,
                          "b": 2,
                          "c": "cccc"
                      },
                      date={
                          "a": 1,
                          "b": 2,
                          "c": "cccc"
                      }
    )


    print(r.json())
    assert r.status_code==200
def test_upload():
    r=requests.post(
        "https://httpbin.testing-studio.com/post",
        files={"file": open("__init__.py",'rb')},
        headers={'Content-Type':""}
    )



