import json

from jsonpath import jsonpath

from test_requests.api.groupchat import GroupChat
from test_requests.api.tag import Tag
from test_requests.api.wework import WeWork
class TestTag:
    @classmethod
    def setup_class(cls):
        cls.tag = Tag()
        cls.reset()
    @classmethod
    def init(cls):
        cls.date = cls.tag.yaml_load("")

    def test_get(self):
        r=self.tag.get_tag()
        assert r['errcode']==0
    def test_add(self):
        r=self.tag.add_tag('demo1')
        assert r['errcode']==0

    def test_delete(self):
        self.tag.add_tag('demo2')
        r=self.tag.get()
        self.tag.jsonpath(r,)
        r=self.tag.deleate_tag()
