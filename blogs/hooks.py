app_name = "blogs"
app_title = "Blogs"
app_publisher = "Frappe Technologies Pvt. Ltd."
app_description = "Write and publish blogs"
app_email = "developers@frappe.io"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [
	{
		"name": "blogs",
		"logo": "/assets/blogs/blogs.svg",
		"title": "Blogs",
		"route": "/app/blogs",
		"has_permission": "blogs.check_app_permission",
	}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/blogs/css/blogs.css"
# app_include_js = "/assets/blogs/js/blogs.js"

# include js, css files in header of web template
web_include_css = "/assets/blogs/css/blog.scss"
# web_include_js = "/assets/blogs/js/blogs.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "blogs/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "blogs/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "blogs.utils.jinja_methods",
# 	"filters": "blogs.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "blogs.install.before_install"
# after_install = "blogs.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "blogs.uninstall.before_uninstall"
# after_uninstall = "blogs.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "blogs.utils.before_app_install"
# after_app_install = "blogs.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "blogs.utils.before_app_uninstall"
# after_app_uninstall = "blogs.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "blogs.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {"Comment": {"after_insert": "blogs.blogs.doctype.blog_post.blog_post.send_email"}}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"blogs.tasks.all"
# 	],
# 	"daily": [
# 		"blogs.tasks.daily"
# 	],
# 	"hourly": [
# 		"blogs.tasks.hourly"
# 	],
# 	"weekly": [
# 		"blogs.tasks.weekly"
# 	],
# 	"monthly": [
# 		"blogs.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "blogs.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "blogs.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "blogs.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["blogs.utils.before_request"]
# after_request = ["blogs.utils.after_request"]

# Job Events
# ----------
# before_job = ["blogs.utils.before_job"]
# after_job = ["blogs.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"blogs.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
comment_rate_limit = "blogs.blogs.doctype.blog_settings.blog_settings.get_comment_limit"
has_comment_permission = {
	"doctype": "Blog Post",
	"method": "blogs.blogs.doctype.blog_settings.blog_settings.has_comment_permission",
}
