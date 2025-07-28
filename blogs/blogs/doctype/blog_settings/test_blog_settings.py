# Copyright (c) 2020, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
from frappe.templates.includes.comments.comments import add_comment
from frappe.tests import IntegrationTestCase
from frappe.tests.test_model_utils import set_user
import frappe
from blogs.blogs.doctype.blog_post.test_blog_post import make_test_blog


class TestBlogSettings(IntegrationTestCase):
	@IntegrationTestCase.change_settings("Blog Settings", {"allow_guest_to_comment": 0})
	def test_guest_cannot_comment(self):
		some_system_user = frappe.db.get_value("User", {"name": ("not in", frappe.STANDARD_USERS)})
		print(some_system_user)
		test_blog = make_test_blog()
		with set_user("Guest"):
			self.assertRaises(
                frappe.ValidationError,
                add_comment,
                comment="Good comment with 10 chars",
                comment_email=some_system_user,
                comment_by="Good Tester",
				reference_doctype="Blog Post",
				reference_name=test_blog.name,
				route=test_blog.route,
			)
