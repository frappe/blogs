# Copyright (c) 2020, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
from frappe.tests import IntegrationTestCase
from frappe.templates.includes.comments.comments import add_comment
from blogs.blogs.doctype.blog_post.test_blog_post import make_test_blog
from frappe.tests.test_model_utils import set_user


class TestBlogSettings(IntegrationTestCase):
    @IntegrationTestCase.change_settings("Blog Settings", {"allow_guest_to_comment": 0})
    def test_guest_cannot_comment(self):
        test_blog = make_test_blog()
        with set_user("Guest"):
            self.assertEqual(
				add_comment(
					comment="Good comment with 10 chars",
					comment_email="mail@example.org",
					comment_by="Good Tester",
					reference_doctype="Blog Post",
					reference_name=test_blog.name,
					route=test_blog.route,
				),
				None,
			)
