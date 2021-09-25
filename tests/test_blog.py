import unittest
from app.models import Blog, User


class BlogTest(unittest.TestCase):
    def setUp(self):
        self.user_id = User(username='Kipkorir', password='Benja312!', email='kipkorir1@gmail.com')
        self.new_blog = Blog(blog_title='Post-Blog',posted_at='5/5/2021', blog_content='new blog amazing', user_id=self.user_id.id)


    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.blog_title, 'Post-Blog')
        self.assertEquals(self.new_blog.blog_content, 'new blog amazing')
        self.assertEquals(self.new_blog.user_id, self.user_id.id)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(self)